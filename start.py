#!/usr/bin/python
# encoding=utf-8
from bs4 import BeautifulSoup
import time
import send_email
import snkrs_get_info


i = 0
FLAG = -1
send_time = 0
shoe_name_list = ['414571_104', 'AV2405_900', '555088_302', '555088_501', 'AQ3816_056', 'AV6683_200']
while i > FLAG:
    i = i + 1
    print('the', i, 'times')
    res = snkrs_get_info.get_shoe_info()
    soup = BeautifulSoup(res.text, 'html.parser')
    print(len(res.text))
    print(res.text)
    # print(res.text[0: 200])
    for num in shoe_name_list:
        print(num)
        if res.text.find(num) >= 0:
            print(num, 'exist')
            if send_time <= 2:
                send_time = send_time + 1
                send_email.sendEmail()
                print(num)
            else:
                shoe_name_list.remove(num)
                send_time = 0
            print(shoe_name_list)
            print(num, 'sendtime', send_time)
        else:
            print('result not found')
            print(shoe_name_list)
            print('sendtime', send_time)
    time.sleep(3)

