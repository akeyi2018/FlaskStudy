# -*- encoding: utf-8 -*-
from flask import Flask, render_template, request, redirect, url_for, jsonify
from controller import robot_controller, MoveBody, SensingDistance
import os
import json

app = Flask(__name__)
control = robot_controller(os.path.dirname(os.path.realpath(__file__)))
config = control.get_config()
control.set_robot_info(0)
move_body = MoveBody(control.get_config()['Robot'])
sensor = SensingDistance()
sensor.run()

def rapper(direction):
    control.set_robot_info(direction)
    move_body.run2(direction, 0.1)

@app.route('/', methods=['GET'])
def index():
    return render_template('front_back.html')

@app.route('/stop', methods=['POST'])
def stop():
    rapper(0)
    return '200'

@app.route('/move', methods=['POST'])
def move():
    if len(request.json) > 0 :
        rapper(int(request.json['d']))
        return '200'
    else:
        return '400'   

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)