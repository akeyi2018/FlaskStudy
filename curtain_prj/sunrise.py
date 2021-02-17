# -*- encoding: utf-8 -*-
from datetime import datetime, timedelta
import requests
from bs4 import BeautifulSoup
import ephem
import json
import os

class sun_info:
    def __init__(self, path):
        self.path = path
        #緯度経度書き込み用Jsonファイル名
        self.location_json_file = os.path.join(self.path, 'location.json')
        self.sun_info_json_file = os.path.join(self.path, 'suninfo.json')
        self.status = 'init'

    def get_user_information_from_json(self):
        with open(self.location_json_file, 'r') as json_file:
            return json.load(json_file)

    def set_user_information_to_json(self, postal_code, adjust_time):
        res = self.get_latlon(postal_code)
        if res is None: return res
        json_data = {
            'post_code': postal_code,
            'adjust_time' : adjust_time,
            'lat': res[0],
            'lon': res[1]
        }
        with open(self.location_json_file, 'w') as json_file:
            json.dump(json_data, json_file, indent=4)
        return True

    def get_curtain_information_from_json(self):
        with open(self.sun_info_json_file, 'r') as json_file:
            return json.load(json_file)

    def set_curtain_information_to_json(self):
        res = self.get_user_information_from_json()
        if res is None:
            return res

        #緯度、経度をセット
        location = ephem.Observer()
        location.lat = res['lat']
        location.lon = res['lon']

        #現在時間UTCをセット
        location.date = datetime.utcnow()
        adjust_time = timedelta(minutes=int(res['adjust_time']))
        sun = ephem.Sun(location)
        #次の日の入りと日の出時間を取得
        sunrise_time = ephem.localtime(location.next_rising(sun)) + adjust_time
        sunset_time = ephem.localtime(location.next_setting(sun)) - adjust_time
        json_data = {
            'open': sunrise_time.strftime('%Y-%m-%d %H:%M'),
            'close': sunset_time.strftime('%Y-%m-%d %H:%M'),
            'status': 'init'
        }
        #計算結果をjsonファイルに書き込む
        with open(self.sun_info_json_file, 'w') as json_file:
            json.dump(json_data, json_file, indent=4)
    
    def get_openclose_time_from_user_setting(self):
        res = self.get_user_information_from_json()
        if res is None:
            return res

        #緯度、経度をセット
        location = ephem.Observer()
        location.lat = res['lat']
        location.lon = res['lon']

        #現在時間UTCをセット
        location.date = datetime.utcnow()
        adjust_time = timedelta(minutes=int(res['adjust_time']))
        sun = ephem.Sun(location)
        #次の日の入りと日の出時間を取得
        sunrise_time = ephem.localtime(location.next_rising(sun)) + adjust_time
        sunset_time = ephem.localtime(location.next_setting(sun)) - adjust_time
        
        return sunrise_time.strftime('%H:%M'), sunset_time.strftime('%H:%M')
        
    #郵便番号より経度、緯度を取得する（geocoding.jp)   
    def get_latlon(self, postal_code):
        try:
            url = f'https://www.geocoding.jp/?q={postal_code}'
            res = requests.get(url)
            soup = BeautifulSoup(res.content, 'html.parser')
            elems = soup.find('div', {'id': 'address'}).find_all("span")[0].find_all('b')
            return elems[0].text,elems[1].text
        except:
            return None

if __name__ == '__main__':
    suninfo = sun_info(os.path.dirname(os.path.realpath(__file__)))
    suninfo.set_user_information_to_json('252-0301', '60')
    suninfo.set_curtain_information_to_json()
    user = suninfo.get_user_information_from_json()
    curtain = suninfo.get_curtain_information_from_json()
    print(user)
    print(curtain)