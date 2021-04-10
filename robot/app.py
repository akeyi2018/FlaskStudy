# -*- encoding: utf-8 -*-
from flask import Flask, render_template, request, redirect, url_for, jsonify
from controller import robot_controller, MoveBody, SensingDistance
from gpiozero import LED
import os
import json

app = Flask(__name__)
control = robot_controller(os.path.dirname(os.path.realpath(__file__)))
config = control.get_config()
move_body = MoveBody(control.get_config()['Robot'])
led = LED(5)
sensor = SensingDistance(led)
sensor.run()

@app.route('/', methods=['GET'])
def index():
    return render_template('front_back.html')

@app.route('/move', methods=['POST'])
def move():
    if len(request.json) > 0 and led.value == 0:
        move_body.run(int(request.json['d']), 1)
        return '200'
    else:
        return '400'   

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)