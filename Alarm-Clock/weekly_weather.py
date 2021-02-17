import requests
import re
import urllib3
from bs4 import BeautifulSoup
from weather import prefecture

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class week_weather:

    def __init__(self, prefectureLink):

        self.prefectureLink = prefectureLink

        res = requests.get("https://www.jma.go.jp/jp/week/" + self.prefectureLink, verify=False)
        soup = BeautifulSoup(res.text,"html.parser")

        self.title = soup.find("caption").text
        self.days = soup.find("table", {"id": "infotablefont"}).find_all("tr")[0].find_all("th")
        self.weatherinfo = soup.find("table", {"id": "infotablefont"}).find_all("tr")[1].find_all("td")
        self.max_temp = soup.find("table", {"id": "infotablefont"}).find_all("tr")[4].find_all("td")
        self.min_temp = soup.find("table", {"id": "infotablefont"}).find_all("tr")[5].find_all("td")
        self.hiduke = ['日付','最高','最低','／']

    def getInfo(self):

        weather = []
        weeklist = []

        maxtemplist = []
        for maxtemp in self.max_temp:
            maxtemp = maxtemp.text

            if self.hiduke[1] not in maxtemp:
                maxtemp = maxtemp.replace('\n', '').replace('\t', '').replace('(', '{').replace(')', '}')
                maxtemp = re.sub('{.*?}', '', maxtemp)

                if self.hiduke[3] in maxtemp:
                    maxtemp = None
                else:
                    maxtemp = int(maxtemp)

                maxtemplist.append(maxtemp)

        mintemplist = []
        for mintemp in self.min_temp:
            mintemp = mintemp.text

            if self.hiduke[2] not in mintemp:
                mintemp = mintemp.replace('\n', '').replace('\t', '').replace('(', '{').replace(')', '}')
                mintemp = re.sub('{.*?}', '', mintemp)

                if self.hiduke[3] in mintemp:
                    mintemp = ""
                else:
                    mintemp = int(mintemp)

                mintemplist.append(mintemp)

        weather.append(self.title)
        weather.append([infotemp.text.replace('\n','') for infotemp in self.weatherinfo[0:7]])
        weather.append([dat.text[:-1] + '(' + dat.text[-1] + ')' for dat in self.days if self.hiduke[0] not in dat.text])
        weather.append(maxtemplist)
        weather.append(mintemplist)

        return weather

if __name__ == "__main__":

    wt = prefecture()
    pre = wt.getPrefecture()[19][0]
    print(pre)
    wk = today_weather(pre)
    print(wk.getInfo())
