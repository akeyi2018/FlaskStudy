from flask import Flask, render_template, request, redirect, url_for, jsonify
from common_form import SelectMultiStore

app = Flask(__name__)
app.config['SECRET_KEY'] = 'do not write key in here.'

@app.get('/')
def index():
    # 変数
    user_name = 'yamada takao'
    # 辞書型変数
    dict_data = {"name":"gao jun", "age": 25}
    # 1次元リスト
    li_01 = [10,20,30,40,50]
	# 2次元リスト
    li_02 = [[1,2,3],[4,5,6],[7,8,9]]
    # Form
    form = SelectMultiStore()
    # 表示Flag
    flag = 0
    return render_template('index.html',
                           user_name=user_name,
                           dict_data=dict_data,
                           li_01=li_01,
                           li_02=li_02,
                           flag = flag,
                           form=form
                           )

@app.route('/show_data', methods=['POST'])
def show_data():
    # これを使うと先頭のみしか取得できない
    kb = request.form['category']
    # 複数選択する場合の戻り値を取得する
    res = request.form.getlist('stores')
    st = ''
    for s in res:
        st = st + s + ' / '
    return 'your selected store name : ' + st + '<br>' + 'category :' + kb


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
