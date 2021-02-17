# -*- encoding: utf-8 -*-
from flask import Flask, render_template, request, redirect, url_for, jsonify
from controller import motor_contorller
# from gpiozero_stepping import C28BYJ48 as stepping_motor
from multiprocessing import Process
import os
import json
from time import sleep

app = Flask(__name__)
control = motor_contorller(os.path.dirname(os.path.realpath(__file__)))
config = control.get_config()
angle_list = config['angle_table']
time_list = config['time_table']

# def process_stepping_motor():
#     motor = stepping_motor()
#     motor.run(angle,time,1)

# 初期設定
def set_configs_param():
    select_info = config['settings']
    return select_info

# 撮影設定値をjsonに書き込む
def rapper_set_status(status:int):
    set_info = request.form.to_dict()
    select_info = {
                    'angle': set_info['angle'],
                    'time': set_info['time'],
                    'direction': int(set_info['direction']),
                    'status': status,
                    'running': 1
                    }
    control.set_motor_status(select_info)
    return select_info

def testFun():
    print('Starting')
    for cn in range(10):
        print(str(cn) + ' Seconds Later')
        control.set_motor_progress(cn+1)
        sleep(1)
    control.set_motor_active(0)
    control.set_motor_progress(0)    
    print('Stopped')
    return 'OK'

def rapper_get_status():
    return control.get_motor_status()

@app.route('/', methods=['GET'])
def index():
    select_info = set_configs_param()
    return render_template('index.html', select_info = select_info, input_angle = angle_list, input_time = time_list)

@app.route('/get_status')
def get_status():
    select_info = rapper_get_status()
    return render_template('index.html', select_info = select_info, input_angle = angle_list, input_time = time_list)
        
@app.route('/set_interval_info', methods=['POST'])
def set_interval():
    if control.get_motor_status()['running'] == 0:
        select_info = rapper_set_status(1)
        # StepMotor = stepping_motor(14, 15, 18, 23)
        # StepMotor.run(angle, time, 1)
        global backProc
        backProc = Process(target=testFun, args=())
        backProc.start()
        return render_template('index.html', select_info = select_info, input_angle = angle_list, input_time = time_list)
    else:
        return redirect(url_for('get_status'))

@app.route('/get_json', methods=['GET'])
def get_json():
    select_info = rapper_get_status()
    print(select_info)
    return jsonify(select_info)

@app.route('/reset_json', methods=['POST'])
def reset_json():
    select_info = config['settings']
    control.set_motor_status(select_info)
    return "200"

@app.route('/stop', methods=['POST'])
def stop():
    if control.get_motor_status()['running'] == 1:
        backProc.terminate()
        control.set_motor_active(0)
        control.set_motor_progress(0)
    return "200"

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
