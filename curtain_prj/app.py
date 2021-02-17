import os
from flask import Flask, render_template, request, redirect, url_for
from sunrise import sun_info
from curtain_move import Curtain

app = Flask(__name__)

def get_user_information():
    res = sun_info(os.path.dirname(os.path.realpath(__file__)))
    return res.get_user_information_from_json()

def get_curtain_information():
    res = sun_info(os.path.dirname(os.path.realpath(__file__)))
    res.set_curtain_information_to_json()
    return res.get_curtain_information_from_json()

def set_user_information(post_code, adjust_time):
    res = sun_info(os.path.dirname(os.path.realpath(__file__)))
    return res.set_user_information_to_json(post_code, adjust_time)
    
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/open', methods=['GET','POST'])
def open_curtain():
    driver = Curtain(os.path.dirname(os.path.realpath(__file__)))
    driver.open()
    return render_template('index.html')

@app.route('/close')
def close_curtain():
    driver = Curtain(os.path.dirname(os.path.realpath(__file__)))
    driver.close()
    return render_template('index.html')

@app.route('/getinfo')
def get_curtain_info():
    curtain = get_curtain_information()
    return render_template('index.html', curtain = curtain)
    
@app.route('/user_info')
def get_user_info():
    user = get_user_information()
    return render_template('index.html', user = user)

@app.route('/set_user_info', methods=['POST'])
def set_user_info():
    if request.method == 'POST':
        post_code = str(request.form['post_code'])
        adjust_time = str(request.form['adjust_time'])
        if set_user_information(post_code, adjust_time) is None:
            return render_template('index.html', err = True)
        else:
            return redirect(url_for('get_user_info'))

if __name__ == '__main__':
    app.run(debug=False, host="0.0.0.0", port=5000)