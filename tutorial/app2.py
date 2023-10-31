from flask import Blueprint, jsonify, redirect, render_template, request, url_for
from save_message import Messager, Comment_flg, html_body
from flask_wtf import FlaskForm
import requests
import bs4
from wtforms import SelectField, SubmitField
from roll import Roll
# Formクラス及び使用するフィールドをインポート
from wtforms import SubmitField, TextAreaField
from common_form import MemberMonthlyForm, get_comment_data

# 自分自身をBlueprintに登録する
bp = Blueprint('app2', __name__)

# 権限の確認
def check_roll(user_name, func_name):
	print(user_name)
	print(func_name)
	return 0

@bp.get('/test')
def test():
	return render_template('register2.html')

@bp.get('/save_html')
def save_html():
	source = requests.get('http://localhost:5000/comment').text
	soup = bs4.BeautifulSoup(source, 'html.parser')
	ins = html_body()
	ins.write(soup)
	return 'Success', 200

# コメントページ表示
@bp.route('/comment/<user_name>',methods=['GET','POST'])
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

	if request.method == 'POST':
		t = form.multi.data
		print(t)

	return render_template('register4.html', form=form, d=ld, d_x=d_x, d_y=d_y, dd = zip(d_x,d_y), user_name=user_name,
			table_dd=zip(t_x,t_y,t_z,t_k))

# 個別のコメントを最新化する
@bp.get('/get_comment/<num>')
def get_comment(num):
	num = int(num)
	data = get_comment_data()[num]
	json = {"data": data}
	return jsonify(json)

# コメントを保存する
@bp.route('/save_comment/<num>', methods=['POST'])
def save_comment(num):
	res = request.get_json()
	value = res['comment']
	mail_add = res['mail']
	post_d = Messager(target=num, author=mail_add, message=value)
	post_d.update_data()
	# 書き込み権限を開放
	Comment_flg(num).update_flg(mail_add,0)
	return redirect(url_for('index'),200)

@bp.route('/write_flg/<num>', methods=['GET','POST'])
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
	
@bp.route('/confirm_test', methods=['GET','POST'])
def confirm_test():
	name = 'yamada'
	comment = 'test comment'
	if request.method =="POST":
		userInput = request.form.get("userInput")
		if userInput == "True":
			print('registed this name')
		else:
			print('cancel this regist name')
	return render_template('confirm.html', name=name, comment=comment)
