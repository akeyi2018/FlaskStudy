# -*- coding: utf-8 -*-
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    my_dic = {}
    my_dic['name'] = name
    my_dic['univ'] = "TOKYO Univ."
    return render_template('chart.html', message=my_dic)

@app.route('/showgraph/')
def showgraph():
    d_list = ['3月25日', '3月26日','3月27日','3月28日','3月29日','3月30日']
    high_temp_list = [16,18,21,21,11,14]
    low_temp_list = [7,9,17,7,7,9]
    return render_template('chart.html', message=d_list, temp=high_temp_list, lowtemp=low_temp_list)

#日本語
if __name__ == "__main__":
    app.run(debug=True)
