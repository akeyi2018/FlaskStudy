import numpy as np
import pandas as pd
from  datetime import datetime
import os,csv
import socket
import json

class Roll():
    def __init__(self, user_name, page_name):
        if socket.gethostname() == 'akeyi2021':
            self.roll_folder = '.\message'
        self.roll_file = 'roll.csv'
        self.roll_path = os.path.join(os.getcwd(), self.roll_folder, self.roll_file)
        self.user_name = user_name
        self.page_name =page_name

    def get_roll(self):
        df = pd.read_csv(self.roll_path,encoding='utf-8')
        res = df.query('(user_name==@self.user_name)&(page_name==@self.page_name)')
        roll = 0
        if res.empty:
            roll = 0
        else:
            roll = list(res['roll'].values)[0]
        return roll        

if __name__ == "__main__":
    ins = Roll('J00588','index')
    re = ins.get_roll()
    print(re)

        