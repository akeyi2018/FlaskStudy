from flask import Flask, redirect, render_template, request, session, url_for, flash,jsonify
from save_message import Messager, Comment_flg, html_body
from flask_wtf import FlaskForm
import requests
import bs4
from wtforms import SelectField, SubmitField
import sys
from roll import Roll

# Formクラス及び使用するフィールドをインポート
from wtforms import SubmitField, TextAreaField

app = Flask(__name__)

# セッションで使用するシークレットキーを設定。本来はランダムな文字列が望ましい
app.config['SECRET_KEY'] = 'secret_key'

class MemberMonthlyForm(FlaskForm):
    # 月別ラベル取得
    start_month = SelectField('Start', choices=['2023-04','2023-05','2023-06'])
    submit = SubmitField('Submit')

def get_comment_data():
	module = Messager().read_data()
	return module

# 権限の確認
def check_roll(user_name, func_name):
	print(user_name)
	print(func_name)
	return 0

@app.get('/test')
def test():
	return render_template('register2.html')

@app.get('/')
def main():
	ld = get_comment_data()
	current_user = {"username":"J00588","email":"test001@test.com"}

	return render_template('side.html',d=ld, current_user=current_user)

@app.get('/save_html')
def save_html():
	source = requests.get('http://localhost:5000/comment').text
	soup = bs4.BeautifulSoup(source, 'html.parser')
	ins = html_body()
	ins.write(soup)
	return 'Success', 200

# コメントページ表示
@app.route('/comment/<user_name>',methods=['GET','POST'])
def index(user_name):
	res = Roll(user_name, index.__name__).get_roll()
	if res == 1:
		pass
	else:
		return 'アクセスできません。',200

	form = MemberMonthlyForm()

	ld = get_comment_data()
	d_x = [80, 50, 90]
	d_y = [30, 40, 50]
	
	t_x = ["X", 50, 90]
	t_y = ["Y", 50, 90]
	t_z = ["Z", 50, 90]
	t_k = ["K", 50, 90]

	return render_template('register4.html', form=form, d=ld, d_x=d_x, d_y=d_y, dd = zip(d_x,d_y), user_name=user_name,
			table_dd=zip(t_x,t_y,t_z,t_k))

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