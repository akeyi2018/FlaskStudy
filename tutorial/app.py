from flask import Flask, redirect, render_template, request, session, url_for, flash
from save_message import Messager
from flask_wtf import FlaskForm 
# Formクラス及び使用するフィールドをインポート
from wtforms import SubmitField, TextAreaField

app = Flask(__name__)

# セッションで使用するシークレットキーを設定。本来はランダムな文字列が望ましい
app.config['SECRET_KEY'] = 'secret_key'
   
# wtformsのFormクラスを継承。それぞれの入力項目に対してバリデーションチェックをかける
class Ragistration(FlaskForm):
    comment = TextAreaField('Input：',render_kw={"rows": 5, "cols": 50})
    submit = SubmitField('Submit')

# POSTかつバリデーションエラーがない場合は、セッションに入力内容を格納してregistered.htmlを表示
@app.route('/', methods=['GET', 'POST'])
def index():
    form = Ragistration()
    if form.validate_on_submit():
      Messager(message = form.comment.data).update_data()
    return render_template('register.html', form=form)
 
if __name__ == '__main__':
  app.run(debug=True)