from flask import Flask, render_template, request, redirect, jsonify
import json
import runcode
# from flask.ext.mongoengine import MongoEngine
# from mongoengine import *
# import datetime

app = Flask(__name__)
app.debug = True

# db = MongoEngine(app)
# app.config['MONGODB_DB'] = 'python'



# save program somewhere...

# Going to save programs so that it can save files and retrieve them, and keep track of modules used
class Program():
    def __init__(self, code, modules, result):
        self.code = code
    #     add list comprehension here?
        self.modules = modules
        self.result = result
    def get_code(self):
        return self.code
    def get_modules(self):
        return self.modules
    def get_result(self):
        return self.result

class Modules():
    def __init__(self):
        self.modules = {}
    def increment_module(self, module):
        self.modules[module] = self.module.get(module, 0) + 1

    def merge_dict(self, d):
        for key, value in d.items():
            self.modules[key] = self.modules.get(key, 0) + value

    def get_all_modules(self):
        return self.modules
    # def __str__(self):
    #     {}

programs = []
all_modules = Modules()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/api/run', methods=['POST'])
def run_code():
    print('orig request', request.form)
    code = request.form['text']
    mods = []
    # print(request.form['modules'])
    mods = [m.strip() for m in request.form['modules'].split()]
    terminal = runcode.run_code(code, mods)
    print('running code: ', terminal)

    mod_dict = {key: 1 for key in mods}
    # for m in mod_dict:
    #     modules
    all_modules.merge_dict(mod_dict)

    programs.append(Program(code, mods, terminal))

    text = {'text': terminal}
    print('all modules: ', all_modules.get_all_modules())
    print('Programs: ', programs[0].get_code())
    return jsonify(**text)
    # return 'hi'


# test if works
@app.route('/api/stats')
def stats():
    stats = {}
    stats['programs'] = [{'code': p.get_code(), 'modules': p.get_modules(), 'results': p.get_result()} for p in programs]
    stats['modules'] = all_modules.get_all_modules()
    return jsonify(stats)

app.run()