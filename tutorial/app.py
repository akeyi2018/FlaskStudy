from flask import Flask, redirect, render_template, request, session, url_for, flash,jsonify
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
	return render_template('register.html', d=ld, test="1")

@app.route('/save_comment/<num>/<k>', methods=['POST'])
def save_comment(num, k):
	if k == 1:
		value = request.form.get('comment')
		post_d = Messager(target=num, message=value)
		post_d.update_data()
	else:
		value = request.form.get('comment')
		post_d = Messager(target=num, message=value)
		post_d.correct_data()

	return redirect(url_for('index'))

@app.route('/write_flg/<num>', methods=['GET','POST'])
def testfn(num):
    print(num)
    # GET request
    if request.method == 'GET':
        print('test')
        message = {'flag':1}
        return jsonify(message)  # serialize and use JSON headers
    
    # POST request
    if request.method == 'POST':
        print(request.get_json())  # parse as JSON
        return 'Success', 200

if __name__ == '__main__':
  	app.run(debug=True)