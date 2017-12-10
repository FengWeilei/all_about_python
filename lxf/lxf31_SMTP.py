# -*- coding: utf-8 -*-

from email.mime.text import MIMEText
# 第一个参数是邮件正文， 第二个参数'plain'表示纯文本，最后使用'utf-8'编码
msg = MIMEText('hello, send by Python...','plain','utf-8')

from_addr = input('From: ')
password = input('Password: ')

to_addr = input('To: ')

smtp_server = input('SMTP server: ')

import smtplib
server = smtplib.SMTP(smtp_server, 25)  # SMTP 默认端口是25
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()



# some bugs I couldn't find
