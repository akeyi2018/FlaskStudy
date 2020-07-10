# FlaskStudy
Flask学習

##### 環境設定(Python3+debian)(インストール）  
```Text
$ mkdir projectname  
$ cd projectname  
$ python3 -m venv venv  
$ . venv/bin/activate
(venv) $ pip install Flask
```  
##### 開発手順  
```YAML
$ cd projectname   
$ . venv/bin/activate
(venv) $ git clone http://github.com/akeyi2018/FlaskStudy
(venv) $ cd FlaskStudy
(venv) $ pip install bs4
```  

##### GET/POSTテスト    
```Text
(venv) $ python hello.py
```
##### ブラウザから以下のURLを入力して動作確認  
http://ip_address/showpostpage  

##### 天気予報(週間)（地域選択機能）を追加  
```Text
(venv) $ python ShowWeekWeather.py
```
##### ブラウザから以下のURLを入力して動作確認  
http://ip_address/showweekweather

##### 表示例
<img src="https://github.com/akeyi2018/FlaskStudy/blob/master/weather.JPG" width="600">

##### 参考動画  
- [4分半で分かるFlask環境構築](https://youtu.be/M_U0AC_oBXQ)
- [0.0.0.0と127.0.0.1とlocalhostの違いについて](https://youtu.be/yL8zces3hKg)

##### 参考文献  
https://qiita.com/bookun/items/7ae5de21307d101b4759
