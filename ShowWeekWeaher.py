# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
from weekweather import Weather, prefecture

app = Flask(__name__)

#各府県情報を取得する
def getpref():
    wp = prefecture()
    pref = {}
    for pre in wp.getPrefecture():
        pref[str(pre[0])] = str(pre[1])

    return pref

@app.route('/showweekweather', methods=['GET','POST'])
def showgraph():

    wt = Weather("319.html").getInfo()
    selectval = "319.html"
    if request.method == 'POST':
        wt = Weather(str(request.form["pref"])).getInfo()
        selectval = str(request.form["pref"])

    return render_template('chart.html', selectedval = selectval,
                           preflink=getpref(),
                           mes=str(wt[0]), message=wt[2], weatherinfo=wt[1],
                           temp=wt[3], lowtemp=wt[4])

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
