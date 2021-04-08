# -*- encoding: utf-8 -*-
from flask import Flask, render_template, request, redirect, url_for, jsonify
from controller import robot_controller, MoveBody
import os
import json

app = Flask(__name__)
control = robot_controller(os.path.dirname(os.path.realpath(__file__)))
config = control.get_config()
move_body = MoveBody(control.get_config()['Robot'])

@app.route('/', methods=['GET'])
def index():
    return render_template('front_back.html')

@app.route('/move', methods=['POST'])
def move():
    res = request.json['d'] if len(request.json) > 0 else 0
    print(res)
    if res > 0:
        move_body.run(int(res))
        return '200'
    else:
        return '400'

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)