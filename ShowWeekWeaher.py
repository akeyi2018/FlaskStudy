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

    title = str(wt[0])
    d_list = []
    for winfo, days in zip(wt[1],wt[2]):
        d_list.append(days + '(' + winfo +')')
    high_temp_list = wt[3]
    low_temp_list = wt[4]

    return render_template('chart.html', selectedval = selectval, preflink=getpref(), mes=title, message=d_list, temp=high_temp_list, lowtemp=low_temp_list)

if __name__ == "__main__":
    app.run(debug=True)
