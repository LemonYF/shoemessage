from email.mime.text import MIMEText
from email.header import Header
import smtplib
import yagmail

def sendEmail() :
    server = yagmail.SMTP(user='919024797@qq.com', password='xfmnhxzewbxibeca', host='smtp.qq.com', port=25,
                          smtp_starttls=True, smtp_ssl=False)
    content = ['有新的鞋款发售，请注意APP！！！！！！！', 'used for yagmail']
    server.send('919024797@qq.com', '突袭发售啦！打开SNKRS！', content)  # 对方邮箱，主题，邮件内容
    server.send('yefan1_test@163.com', '突袭发售啦！打开SNKRS！', content)  # 对方邮箱，主题，邮件内容
    server.send('1054273874@qq.com', '宝贝儿，突袭发售啦！打开SNKRS！', content)  # 对方邮箱，主题，邮件内容
    server.send('136610832@qq.com', '死胖子，突袭发售啦！打开SNKRS！', content)  # 对方邮箱，主题，邮件内容
    # # 输入Email地址和口令:
    # from_addr = 'yefan1_test@163.com'
    # password = 'yezhizi1994421'
    # # 输入收件人地址:
    # to_addr = '919024797@qq.com'
    # # 输入SMTP服务器地址:
    # smtp_server = 'smtp.163.com'
    # subject = '发售提醒'
    #
    # # 发件邮箱和收件邮箱需要真实地址，否则无法发送
    # msg = MIMEText('hello, 有一款突击发售，请打开APP查看', 'plain', 'utf-8')
    # msg['Subject'] = Header(subject, 'utf-8')
    # msg['From'] = 'yefan1_test@163.com'
    # msg['To'] = '919024797@qq.com'
    #
    # server = smtplib.SMTP_SSL(smtp_server, 587)  # SMTPSSL协议默认端口是587
    # server.set_debuglevel(1)
    # server.login(from_addr, password)
    # server.sendmail(from_addr, [to_addr], msg.as_string())
    # server.quit()
