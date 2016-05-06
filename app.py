from flask import Flask, render_template, request, redirect, jsonify
import json
import runcode
# from flask.ext.mongoengine import MongoEngine
# from mongoengine import *
# import datetime
import string, random


app = Flask(__name__)
app.debug = True

# db = MongoEngine(app)
# app.config['MONGODB_DB'] = 'python'



class Program_List():
    def __init__(self):
        self.programs_list = []
    def add_or_update_program(self, code, modules, result, slug):
        """
        Either updates an existing program, or creates a new program if the slug isn't found
        :param code: string of code
        :param modules: modules
        :param result: the result from a program
        :param slug: the url slug
        :return: nothing
        """
        # I know I should be using a dictionary for programs_list, but I didn't have time to change it :/ (as it would provide O(1)
        for p in self.programs_list:
            if p.get_slug() == slug:
                p.update_program(code, modules, result)
                return None
        self.programs_list.append(Program(code, modules, result, slug))
    def get_program(self, slug):
        for p in self.programs_list:
            if p.get_slug() == slug:
                return p
        return False
    def get_all_programs(self):
        return [p.get_json() for p in self.programs_list]

# Going to save programs so that it can save files and retrieve them, and keep track of modules used
class Program():
    def __init__(self, code, modules, result, slug):
        self.code = code
        self.modules = modules
        self.result = result
        self.slug = slug
    def get_code(self):
        return self.code
    def get_modules(self):
        return self.modules
    def get_result(self):
        return self.result
    def get_slug(self):
        return self.slug
    def update_program(self, code, modules, result):
        self.code = code
        self.modules = modules
        self.result = result
    def get_json(self):
        return {'code': self.code, 'modules': self.modules, 'result': self.result}
class Modules():
    def __init__(self):
        self.modules = {}
    def increment_module(self, module):
        self.modules[module] = self.module.get(module, 0) + 1

    def merge_dict(self, d):
        """
        Merges a dictionary of modules into this list of modules
        :param d: dictionary
        :return: None
        """
        for key, value in d.items():
            self.modules[key] = self.modules.get(key, 0) + value

    def get_all_modules(self):
        return self.modules

# Storing programs
programs = Program_List()
# Storing module data
all_modules = Modules()

@app.route('/')
def home():
    #stackoverflow ftw -> http://stackoverflow.com/questions/2257441/random-string-generation-with-upper-case-letters-and-digits-in-python
    def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))
    return redirect('/' + id_generator(6))
@app.route('/<slug>')
def slugged(slug):
    print(slug)
    # check if program exists, and then load the the text
    p = programs.get_program(slug)
    if p:
        print('program: ', p.get_json())
        return render_template('home.html', program=p.get_json())
    return render_template('home.html', program={'code': '', 'modules': ''})
@app.route('/api/run', methods=['POST'])
def run_code():
    # print('orig request', request.form)
    path = request.form['path'][1:]
    code = request.form['text']
    # Getting all the modules used (and List Comprehension)
    mods = [m.strip() for m in request.form['modules'].split()]
    terminal = runcode.run_code(code, mods, path)
    # print('running code: ', terminal)

    # DICTIONARY COMPREHENSION
    mod_dict = {key: 1 for key in mods}
    all_modules.merge_dict(mod_dict)

    # Adding new program to program list
    programs.add_or_update_program(code, mods, terminal, path)

    text = {'text': terminal}
    return jsonify(**text)


# test if works
@app.route('/api/stats')
def stats():
    stats = {}
    stats['programs'] = programs.get_all_programs()
    stats['modules'] = all_modules.get_all_modules()
    return jsonify(stats)

app.run()