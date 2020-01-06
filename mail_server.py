#!/usr/bin/python

import imaplib
import pprint
import json
import os

# 读取json文件中的邮箱信息
email_json = open("mail_login_info.json", "r")
email_info = json.loads(email_json.read())

# 获取邮箱服务器地址、端口、邮箱地址、登陆密钥
imap_host = email_info['IMAP']['address']
imap_SSL_port = email_info['IMAP']['SSL_port']
imap_user = email_info['email']
imap_pass = email_info['authority_code']

# connect to host using SSL
imap = imaplib.IMAP4_SSL(imap_host)

## login to server
imap.login(imap_user, imap_pass)

imap.select('Inbox')

tmp, data = imap.search(None, 'ALL')
for num in data[0].split():
	tmp, data = imap.fetch(num, '(RFC822)')
	print('Message: {0}\n'.format(num))
	pprint.pprint(data[0][1])
	break
imap.close()

