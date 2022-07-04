from flask import Blueprint, redirect, render_template, url_for

Api = Blueprint('api', __name__)

@Api.route('/login')
def hoge():

    return render_template('login.html')


@Api.route('/goto_main')
def gotomain():
    # メイン画面へリダイレクト
    return redirect(url_for('home'))