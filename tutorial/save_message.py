import numpy as np
import pandas as pd
from  datetime import datetime
import os,csv
import socket

class Messager():
    def __init__(self, target=0, author='admin', message='this is test message') -> None:
        if socket.gethostname() == 'akeyi2021':
            self.message_folder = '.\message'
        self.messager_file = 'messager.csv'
        self.messager_path = os.path.join(os.getcwd(), self.message_folder, self.messager_file)
        self.dt_now = datetime.now()
        self.target = int(target)
        self.author = author
        self.message = message
        self.target_list = ['KIX-M','KIX-D','ITM-M','ITM-D']
        self.csv_col = ['date','target','author','message']

    # 新規作成
    def create_new(self):
        # メッセージの改行マークの置換
        # m = self.message.replace('\r\n','&#13;')
        m = self.message
        out = [self.dt_now, self.target_list[self.target], self.author, m]
        with open(self.messager_path, 'w', newline='', encoding='cp932') as f:
            w = csv.writer(f)
            w.writerow(self.csv_col)
            w.writerow(out)

    # 追記（更新）
    def update_data(self):
        out = [self.dt_now, self.target_list[self.target], self.author, self.message.strip()]
        with open(self.messager_path, 'a', newline='') as f:
            w = csv.writer(f)
            w.writerow(out)

    # 読み込み
    def read_data(self):
        d = []
        df = pd.read_csv(self.messager_path,encoding='cp932')
        for k in self.target_list:
            res = df.query('target==@k')
            if res.empty:
                # d[k] = ''
                d.append('')
            else:
                li = self.create_out_message(res.tail(1))
                # d[k] = li
                d.append(li)
        return d
    
    def create_out_message(self, df):
        li = df.values.tolist()[0][3]
        return li

    def run(self):
        if os.path.exists(self.messager_path):
            self.update_data()
        else:
            self.create_new()

if __name__ == "__main__":
    ins = Messager()
    # 登録
    # ins.run()

    # 確認
    d = ins.read_data()
    print(d)
        