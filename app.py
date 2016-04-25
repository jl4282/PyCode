from flask import Flask, render_template, request, redirect, jsonify
import json
import runcode

app = Flask(__name__)
app.debug = True

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/api/run', methods=['POST'])
def run_code():
    print('orig request', request.form)
    code = ''
    mods = []

    for i in request.form:
        # code = i
        params = json.loads(i)
        print(params)
        for c in params['text']:
            code += c
        for m in params['modules'].split():
            mods.append(m.strip())
        print(code, mods)
    terminal = runcode.run_code(code, mods)
    print('running code: ', terminal)
    text = {'text': terminal}
    return jsonify(**text)
    # return 'hi'
app.run()