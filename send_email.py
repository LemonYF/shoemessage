#!/usr/bin/python
# encoding=utf-8
import yagmail


def sendEmail() :
    server = yagmail.SMTP(user='919024797@qq.com', password='xfmnhxzewbxibeca', host='smtp.qq.com', port=25,
                          smtp_starttls=True, smtp_ssl=False)
    content = ['Open SNKRS APP！！！！！！！', 'used for yagmail']
    # server.send('919024797@qq.com', 'SNKRS!!!', content)
    try:
        s = server.send('yefan1_test@163.com', 'SNKRS!!!!', content)
        print('this is send result', s)
    except (NameError, IndexError)  as e:
        print(e)
    # server.send('1054273874@qq.com', 'Baby Open SNKRS!!！', content)
    # server.send('136610832@qq.com', 'Come! Come! SNKRS!!!', content)
    return 0
