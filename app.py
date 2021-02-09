#!/usr/bin/python
from flask import Flask
import flask
from flask import Response
from flask import request
import json
from compatibility_study import Compatibility_study
import os

port = int(os.environ.get('PORT', 5000))
app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "<h1>Compatibility study!</h1>"

@app.route('/compatibility', methods=['POST'])
def compatibile():
    data = request.get_json()
    t1_A = data[0]["t1"]
    t2_A = data[0]["t2"]
    t1_B = data[1]["t1"]
    t2_B = data[1]["t2"]
    compatibility_study = Compatibility_study(t1_A,t2_A,t1_B,t2_B)
    result = compatibility_study.compatibility()
    return str(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, debug=True)