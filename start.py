import requests
from bs4 import BeautifulSoup
import time
import send_email

i = 0
FLAG = -1
send_time = 0
shoe_name_list = ['AA3830-100', '414571-104', 'Presto Off White \'White ', 'AV2405-900']
while i > FLAG:
    i = i + 1
    nike_url = 'https://www.nike.com/cn/launch/'
    try:
        res = requests.get(nike_url)
    except:
        print('waring')
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'html.parser')
    print('\n')
    print('第', i, '次查询结果')
    print(len(res.text))
    print(res.text[0: 200])
    for num in shoe_name_list:
        if res.text.find(num) >= 0:
            if send_time <= 2:
                send_time = send_time + 1
                send_email.sendEmail()
                print(num)
            else:
                shoe_name_list.remove(num)
                send_time = 0
            print(shoe_name_list)
            print('sendtime',send_time)
        else:
            print('result not found')
            print(shoe_name_list)
            print('sendtime', send_time)
    time.sleep(3)
