# -*- coding: utf-8 -*-
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    my_dic = {}
    my_dic['name'] = name
    my_dic['univ'] = "TOKYO Univ."
    return render_template('dict.html', message=my_dic)

#モジュールを実行する場合の処理
if __name__ == "__main__":
    app.run(debug=True)
