import numpy as np
import pandas as pd
from  datetime import datetime
import os,csv
import socket

class Messager():
    def __init__(self, target='KIX-M', author='admin', message='this is test message') -> None:
        if socket.gethostname() == 'akeyi2021':
            self.message_folder = './message'
        self.messager_file = 'messager.csv'
        self.messager_path = os.path.join(self.message_folder, self.messager_file)
        self.dt_now = datetime.now()
        self.target = target
        self.author = author
        self.message = message
        self.target_list = ['KIX-M','KIX-D','ITM-M','ITM-D']
        self.csv_col = ['date','target','author','message']

    # 新規作成
    def create_new(self):
        li = [self.dt_now, self.target, self.author, self.message]
        with open(self.messager_path, 'w', newline='') as f:
            w = csv.writer(f)
            w.writerow(self.csv_col)
            w.writerow(li)

    # 追記（更新）
    def update_data(self, message):
        li = [self.dt_now, self.target, self.author, self.message]
        with open(self.messager_path, 'a') as f:
            w = csv.writer(f)
            w.writerow(li)
    # 読み込み
    def read_data(self):
        d = {}
        df = pd.read_csv(self.messager_path,encoding='cp932')
        for k in self.target_list:
            res = df.query('target==@k')
            if res.empty:
                d[k] = ''
            else:
                d[k] = res['message'].to_list()[-1]
        return d

    def run(self):
        if os.path.exists(self.messager_path):
            self.update_data(self.message)
        else:
            self.create_new()

if __name__ == "__main__":
    ins = Messager(target='KIX-D',message='確認しました。')
    # ins.run()
    # 登録
    ins.run()

    # 確認
    d = ins.read_data()
    print(d)
        