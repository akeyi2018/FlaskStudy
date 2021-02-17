import requests
import subprocess
import urllib3
from bs4 import BeautifulSoup

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class today_weather:
    def __init__(self, prefectureLink):
        self.prefectureLink = prefectureLink
        res = requests.get("https://www.jma.go.jp/jp/yoho/" + self.prefectureLink + ".html", verify=False)
        soup = BeautifulSoup(res.text,"html.parser")
        self.target_table = soup.find("table", {"id": "forecasttablefont"}).find_all("th", {"class": "weather"})[0]
        self.time_table = self.target_table.text.replace("\n","")
        self.today_info = self.target_table.img['title']
        #temp
        self.target_temp = soup.find("table", {"id": "forecasttablefont"}).find_all("td", {"class": "max"})[0].text.replace("\n","").replace("\t","")

    def getInfo(self):
        weather = []
        weather.append(self.time_table)
        weather.append('、' + self.today_info)
        weather.append('、、最高気温は、' + self.target_temp + 'です')
        return weather
class prefecture:

    def __init__(self):
        #各府県のデータを取得する
        res1 = requests.get("https://www.jma.go.jp/jp/yoho/", verify=False)
        self.soup1 = BeautifulSoup(res1.text, "html.parser")

    def getPrefecture(self):
        prelist = self.soup1.find("form", {"name": "fukenlist"}).find_all("option")
        return [[pre.get("value"), pre.text] for pre in prelist]
class voice:
    def __init__(self):
        self.open_jtalk = ['open_jtalk']
        self.mech = ['-x','/var/lib/mecab/dic/open-jtalk/naist-jdic']
        self.htsvoice=['-m','/usr/share/hts-voice/mei/mei_normal.htsvoice']
        self.speed=['-r','1.5']
        self.outwav=['-ow','test.wav']
        self.cmd = self.open_jtalk + self.mech + self.htsvoice + self.speed + self.outwav

    def run(self, voice_text):
        voice_creater = subprocess.Popen(self.cmd, stdin=subprocess.PIPE)
        voice_creater.stdin.write(voice_text.encode('utf-8'))
        voice_creater.stdin.close()
        voice_creater.wait()
        self.aplay = ['aplay', '-q', 'test.wav', '-Dhw:1,0']
        wr = subprocess.Popen(self.aplay)
        wr.wait()

if __name__ == "__main__":

    wt = prefecture()
    pre = wt.getPrefecture()
    # print(pre[20][1])
    wk = today_weather(pre[20][0])
    voice_text = wk.getInfo()[0] + wk.getInfo()[1] + wk.getInfo()[2]
    vc = voice()
    vc.run(voice_text)
