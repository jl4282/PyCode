from flask import Flask, render_template, request, redirect, jsonify
import runcode
from flask_assets import Bundle, Environment

app = Flask(__name__)
app.debug = True

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/api/run', methods=['POST'])
def run_code():
    # print(request.form)
    code = ''
    for i in request.form:
        code = i
    terminal = runcode.run_code(code)
    print('running code: ', terminal)
    text = {'text': terminal}
    return jsonify(**text)



app.run()