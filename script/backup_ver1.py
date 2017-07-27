#!/usr/bin/python
# Filename:backup_ver1.py

import os
import time

source=['/home/bingo/test01','/home/bingo/test02']

target_dir='/root/backup/'

target=target_dir+time.strftime('%Y%m%d%H%M%S')+'.zip'

zip_command="zip -qr '%s' %s"%(target,' '.join(source))

if os.system(zip_command) == 0:
	print 'Successful backup to',target
else:
	print 'Backup FALIED'
