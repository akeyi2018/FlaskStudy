from flask import Flask, redirect, render_template, request, session, url_for
 
# Formクラス及び使用するフィールドをインポート
from wtforms import (
    Form, BooleanField, IntegerField, PasswordField, StringField,
    SubmitField, TextAreaField)
 
# 使用するvalidatorをインポート
from wtforms.validators import DataRequired, EqualTo, Length, NumberRange

app = Flask(__name__)

# セッションで使用するシークレットキーを設定。本来はランダムな文字列が望ましい
app.config['SECRET_KEY'] = 'secret_key'

# wtformsのFormクラスを継承。それぞれの入力項目に対してバリデーションチェックをかける
class Ragistration(Form):
    comment = TextAreaField('コメント：')
    submit = SubmitField('Submit')

# POSTかつバリデーションエラーがない場合は、セッションに入力内容を格納してregistered.htmlを表示
@app.route('/', methods=['GET', 'POST'])
def index():
    form = Ragistration(request.form)
    if request.method == 'POST' and form.validate():
      session['comment'] = form.comment.data
    return render_template('register.html', form=form)

@app.route('/r')
def registerd():
  print('保存しました')
  pass
 
@app.route('/save_comment', methods=['GET','POST'])
def save_comment():
   
if __name__ == '__main__':
  app.run(debug=True)