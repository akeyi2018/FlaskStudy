# -*- encoding: utf-8 -*-
from flask import Flask, render_template, request, redirect, url_for, jsonify, send_file
from controller import robot_controller, MoveBody, SensingDistance
import os
import json
from time import sleep
import picamera
import datetime
from glob import glob 
from ras_picamera import remote_camera

app = Flask(__name__)

control = robot_controller(os.path.dirname(os.path.realpath(__file__)))
config = control.get_config()['settings']
control.set_robot_status(config['STATUS_ZERO'])
move_body = MoveBody(control)
sensor = SensingDistance(control)
sensor.run()
camera = remote_camera()

def rapper(move_direction):
    control.set_robot_status(config['STATUS_ZERO'])
    while True:
        if control.get_robot_info()['status'] == 0:
            move_body.run(move_direction, config['moving_time'])
        else:
            move_body.run(config['STOP_ROBOT'], config['stop_time'])
            break

@app.route('/', methods=['GET'])
def index():
    return render_template('remote_control.html', img_file='')

@app.route('/stop', methods=['POST'])
def stop():
    control.set_robot_status(config['STATUS_ONE'])
    return '200'

@app.route('/check', methods=['GET'])
def check_image():
    
    return send_file(fn)

@app.route('/capture/')
def show_image():
    camera.take_photo()
    fn = camera.get_latest_modified_file_path()
    print(fn)
    return send_file(fn)

@app.route('/move', methods=['POST'])
def move():
    control.set_robot_status(config['STATUS_ONE'])
    if len(request.json) > 0 :
        rapper(int(request.json['d']))
        return '200'
    else:
        return '400' 

@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate, public, max-age=0"
    response.headers["Expires"] = '0'
    response.headers["Pragma"] = "no-cache"
    return response

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)