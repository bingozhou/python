# coding=utf-8

import os
import sys

if os.getuid() == 0:
    pass
else:
    print '当前用户不是root用户，请以root用户执行脚本'
    sys.exit(1)

version = raw_input('请输入你想安装的python版本3.6.2/2.7.13:\n')
if version == '3.6.2':
    url = 'http://www.file.alimmdn.com/python/Python-3.6.2.tgz'
elif version == '2.7.13':
    url = 'http://www.file.alimmdn.com/python/Python-2.7.13.tgz'
else:
    print '您输入的版本号有误，请输入3.6.2或者2.7.13'
    sys.exit(1)

cmd = 'wget '+url
res = os.system(cmd)
if res != 0:
    print '下载源码包失败，请检查网络'
    sys.exit(1)

if version == '3.6.2':
    package_name = 'Python-3.6.2'
else:
    package_name = 'Python-2.7.13'

cmd = 'tar xf '+package_name+'.tgz'
res = os.system(cmd)
if res != 0:
    os.system('rm '+package_name+'.tgz')
    print '解压源码包失败，请重新运行脚本下载'
    sys.exit(1)


