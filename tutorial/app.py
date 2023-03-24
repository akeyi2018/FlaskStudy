from flask import Flask, redirect, render_template, request, session, url_for, flash
from save_message import Messager
from flask_wtf import FlaskForm 
# Formクラス及び使用するフィールドをインポート
from wtforms import SubmitField, TextAreaField

app = Flask(__name__)

# セッションで使用するシークレットキーを設定。本来はランダムな文字列が望ましい
app.config['SECRET_KEY'] = 'secret_key'

def get_comment_data():
	module = Messager().read_data()
	return module

@app.route('/comment', methods=['GET'])
def index():
	ld = get_comment_data()
	return render_template('register.html', d=ld)

@app.route('/save_comment/<num>', methods=['POST'])
def save_comment(num):
	value = request.form.get('comment')
	post_d = Messager(target=num, message=value)
	post_d.update_data()

	return redirect(url_for('index'))

if __name__ == '__main__':
  	app.run(debug=True)