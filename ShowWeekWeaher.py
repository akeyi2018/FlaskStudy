# -*- coding: utf-8 -*-
from flask import Flask, render_template
from weekweather import Weather

app = Flask(__name__)

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    my_dic = {}
    my_dic['name'] = name
    my_dic['univ'] = "TOKYO Univ."
    return render_template('chart.html', message=my_dic)

@app.route('/showweekweather/')
def showgraph():
    wt = Weather().getInfo()
    title = str(wt[0])
    d_list = wt[1]
    high_temp_list = wt[2]
    low_temp_list = wt[3]
    print(title)
    return render_template('chart.html', mes=title, message=d_list, temp=high_temp_list, lowtemp=low_temp_list)

#日本語
if __name__ == "__main__":
    app.run(debug=True)
