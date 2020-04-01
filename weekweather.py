import requests
import re
import urllib3
from bs4 import BeautifulSoup

class Weather:

    def __init__(self):

        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

        res = requests.get("https://www.jma.go.jp/jp/week/319.html", verify=False)
        soup = BeautifulSoup(res.text,"html.parser")
        self.title = soup.find("caption").text
        self.days = soup.find("table", {"id": "infotablefont"}).find_all("tr")[0].find_all("th")
        self.weatherinfo = soup.find("table", {"id": "infotablefont"}).find_all("tr")[1].find_all("td")
        self.max_temp = soup.find("table", {"id": "infotablefont"}).find_all("tr")[4].find_all("td")
        self.min_temp = soup.find("table", {"id": "infotablefont"}).find_all("tr")[5].find_all("td")
        self.hiduke = '日付'

    def getInfo(self):

        weather = []
        daylist = []
        weeklist = []
        info = []

        for daytemp in self.days:
            daytemp = daytemp.text

            if self.hiduke not in daytemp:
                daylist.append(daytemp[:-1] + '(' + daytemp[-1] + ')')

        targetInfo = self.weatherinfo[0:7]
        for infotemp in targetInfo:
            infotemp = infotemp.text
            info.append(infotemp.replace('\n',''))

        maxtemplist = []
        for maxtemp in self.max_temp:
            maxtemp = maxtemp.text

            if '最高' not in maxtemp:
                maxtemp = maxtemp.replace('\n', '').replace('\t', '').replace('(', '{').replace(')', '}')
                maxtemp = re.sub('{.*?}', '', maxtemp)

                if '／' in maxtemp:
                    maxtemp = None
                else:
                    maxtemp = int(maxtemp)

                maxtemplist.append(maxtemp)

        mintemplist = []
        for mintemp in self.min_temp:
            mintemp = mintemp.text

            if '最低' not in mintemp:
                mintemp = mintemp.replace('\n', '').replace('\t', '').replace('(', '{').replace(')', '}')
                mintemp = re.sub('{.*?}', '', mintemp)

                if '／' in mintemp:
                    mintemp = None
                else:
                    mintemp = int(mintemp)

                mintemplist.append(mintemp)

        weather.append(self.title)
        weather.append(info)
        weather.append(daylist)
        weather.append(maxtemplist)
        weather.append(mintemplist)

        return weather

if __name__ == "__main__":

    wt = Weather()
    print(wt.getInfo()[1])
