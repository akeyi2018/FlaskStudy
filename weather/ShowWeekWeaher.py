# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
from weekweather import Weather, prefecture

app = Flask(__name__)

#各府県情報を取得する
def getpref():
    wp = prefecture()
    return wp.getPrefecture()

@app.route('/s', methods=['GET','POST'])
def showgraph():
    selectval = "千葉県"
    wt = Weather(selectval).addInfo()
    if request.method == 'POST':
        # print(str(request.form["pref"]))
        wt = Weather(str(request.form["pref"])).addInfo()
        selectval = str(request.form["pref"])
        print(wt)
    # _が使えない
    return render_template('chart.html', da1 = wt, preflink = getpref(), selectedval = selectval)

@app.route('/u', methods = ['GET','POST'])
def set_date():
    if request.method == 'POST':
        fr = str(request.form["from"])
        to = str(request.form["to"])
        res = f'from:{fr},to:{to}'
        return res

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
