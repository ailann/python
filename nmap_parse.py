# -*- coding: UTF-8 -*-
#author:ailann

#对nmap结果进行解析获取需要的保存

import os
import sys
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

reload(__import__('sys')).setdefaultencoding('utf-8')

def parse_alive(nmap_alive):
	try:
		alive_content = open(nmap_alive,'r').read()
		root = ET.fromstring(alive_content)
	except:
		print 'open nmap_alive.xml error!'
		sys.exit()
	try:
		alive_result = open('al_result.txt','a+') 
	except:
		print 'create alive_result.txt error'
		sys.exit()

	for host in root.findall('host'):
		if len(host) > 3:
 			 pass
            #print '\n', str(len(host)),  # 打印host标签中子元素个数
    		if host[0].get('state') == "up":  # 判断IP是否存活
        		ip = host[1].get('addr')  # 提取IP地址
        		ip_ =  ip + '\n'
        		alive_result.writelines(ip_)
