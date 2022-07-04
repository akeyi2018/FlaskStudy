from flask import Flask, redirect, url_for

from admin.api import Api

app = Flask(__name__)

app.register_blueprint(Api, url_prefix='/admin')

@app.route("/")
def home():
    return 'Home'

@app.route('/go')
def go():
    # BluePrint先へリダイレクト
    return redirect(url_for('api.hoge'))

if __name__ == '__main__':
    app.run(debug=True)

