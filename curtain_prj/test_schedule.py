import schedule
from time import sleep, ctime
from datetime import datetime, timedelta
from sunrise import sun_info
from curtain_move import Curtain
import os

class curtain_scheduling:

    def __init__(self):
        self.initial_time = "23:30"
        self.test_init = (datetime.now() + timedelta(minutes=1)).strftime('%H:%M')
        self.test_open = (datetime.now() + timedelta(minutes=2)).strftime('%H:%M')
        self.test_close = (datetime.now() + timedelta(minutes=3)).strftime('%H:%M')

    def open(self):
        print("do open curtain." + ctime())
        driver = Curtain(os.path.dirname(os.path.realpath(__file__)))
        driver.open()
        
    def close(self):
        print("do close curtain." + ctime())
        driver = Curtain(os.path.dirname(os.path.realpath(__file__)))
        driver.close()
    

    def set_schedule(self):
        print("start job. " + ctime())
        res = sun_info(os.path.dirname(os.path.realpath(__file__)))
        open_time, close_time = res.get_openclose_time_from_user_setting()
        print("set open time at " + open_time)
        print("set close time at " + close_time)
        schedule.every().day.at(open_time).do(self.open)
        schedule.every().day.at(close_time).do(self.close)
        print("finish set time schedule " + ctime())
    
    def test_set(self):
        print("start job. " + ctime())
        schedule.every().day.at(self.test_open).do(self.open)
        schedule.every().day.at(self.test_close).do(self.close)
        print("finish set time schedule " + ctime())

if __name__ == '__main__':
    scd = curtain_scheduling()
    # schedule.every().day.at(scd.initial_time).do(scd.set_schedule)
    #test
    schedule.every().day.at(scd.test_init).do(scd.test_set)
    while True:
        schedule.run_pending()
        sleep(30)
