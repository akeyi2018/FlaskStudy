from flask import Flask, redirect, render_template, url_for
# Formクラス及び使用するフィールドをインポート
from app2 import bp
from view.view_graph import bp_view

# Flaskアプリ宣言
app = Flask(__name__)

# Blueprint分割先を登録する
app.register_blueprint(bp)
app.register_blueprint(bp_view, url_prefix='/view')

# セッションで使用するシークレットキーを設定。本来はランダムな文字列が望ましい
app.config['SECRET_KEY'] = 'secret_key'

@app.route('/')
def main():
	current_user = {"username":"J00588","email":"test001@test.com"}
	return render_template('side.html', current_user=current_user)

if __name__ == '__main__':
  	app.run(debug=True)