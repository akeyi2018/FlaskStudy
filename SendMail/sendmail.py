# -*- coding: utf-8 -*-

import smtplib
from datetime import datetime
from email.mime.text import MIMEText
from email.header import Header
from dynaconf import settings

class send_email:
    
    def __init__(self, _body, _subject, _from, _to):
        ENCODE = 'ISO-2022-JP' # for Japanese character
        TEXT_FORMAT = 'plain'
        self.body = _body
        self.msg = MIMEText(self.body, TEXT_FORMAT, ENCODE)
        self.msg['Subject'] = Header(_subject, ENCODE)
        self.msg['From'] = _from
        self.msg['To'] = _to

    def run(self):
        server = smtplib.SMTP(settings['host'], settings['port'])
        print(server)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(settings['email_user'], settings['email_passwd'])
        server.send_message(self.msg)
        server.close()

if __name__ == '__main__':
    _from = 'raspberry_pi@raspi.com'
    _to = 'akeyi2016@gmail.com'
    body = 'this mail is send from raspi in ' + datetime.now()
    test_mail = send_email(body, subject, _from, _to)
    test_mail.run()
