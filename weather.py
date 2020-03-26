import requests
import re
import urllib3
from bs4 import BeautifulSoup


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

res = requests.get("https://www.jma.go.jp/jp/week/319.html", verify=False)

soup = BeautifulSoup(res.text,"html.parser")

city = soup.find("th", {"class": "cityname"}).text
days = soup.find("table", {"id": "infotablefont"}).find_all("tr")[0].find_all("th")
max_temp = soup.find("table", {"id": "infotablefont"}).find_all("tr")[4].find_all("td")
min_temp = soup.find("table", {"id": "infotablefont"}).find_all("tr")[5].find_all("td")
print(days)
print(max_temp)
print(min_temp)
