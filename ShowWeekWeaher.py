# -*- coding: utf-8 -*-
from flask import Flask, render_template
from weekweather import Weather

app = Flask(__name__)

@app.route('/showweekweather/')
def showgraph():
    wt = Weather().getInfo()
    title = str(wt[0])
    d_list = []
    for winfo, days in zip(wt[1],wt[2]):
        d_list.append(days + '(' + winfo +')')
    high_temp_list = wt[3]
    low_temp_list = wt[4]
    print(d_list)
    return render_template('chart.html', mes=title, message=d_list, temp=high_temp_list, lowtemp=low_temp_list)

if __name__ == "__main__":
    app.run(debug=True)
