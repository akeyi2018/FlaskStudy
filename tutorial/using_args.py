from flask import Flask, redirect, render_template, request, session, url_for, flash,jsonify
from save_message import Messager, Comment_flg
from flask_wtf import FlaskForm 
# Formクラス及び使用するフィールドをインポート
from wtforms import SubmitField, TextAreaField

app = Flask(__name__)

# セッションで使用するシークレットキーを設定。本来はランダムな文字列が望ましい
app.config['SECRET_KEY'] = 'secret_key'

def get_comment_data():
	module = Messager().read_data()
	return module

@app.get('/')
def main():
	a = [10,20,30,40,50]
	b = {"name":"gao jun", "age": 25}
	return render_template('dict.html', **locals())

# コメントページ表示
@app.get('/comment')
def index():
	ld = get_comment_data()
	return render_template('register.html', d=ld)

# 個別のコメントを最新化する
@app.get('/get_comment/<num>')
def get_comment(num):
	num = int(num)
	data = get_comment_data()[num]
	json = {"data": data}
	return jsonify(json)

# コメントを保存する
@app.route('/save_comment/<num>', methods=['POST'])
def save_comment(num):
	res = request.get_json()
	value = res['comment']
	mail_add = res['mail']
	post_d = Messager(target=num, author=mail_add, message=value)
	post_d.update_data()
	# 書き込み権限を開放
	Comment_flg(num).update_flg(mail_add,0)
	return redirect(url_for('index'),200)

@app.route('/write_flg/<num>', methods=['GET','POST'])
def write_flg(num):
	# GET request
	if request.method == 'GET':
		flg, mail_add = Comment_flg(num).get_flg()
		message = {'flag': flg, 'mail' : mail_add}
		return jsonify(message)
    
    # POST request
	if request.method == 'POST':
		res = request.get_json()
		print(res)
		flg = res['param']
		mail_add = res['mail']
		Comment_flg(num).update_flg(mail_add, flg)
		return 'Success', 200

if __name__ == '__main__':
  	app.run(debug=True)