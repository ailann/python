# -*- coding: UTF-8 -*-
#author:ailann

import requests

try:
	f1 = open('tttt.txt','a+')
except:
	print 'error'

def check_weblogic_wlst(file_ip):
	with open(file_ip,'r') as f:
		for each in f :
			each = 'http://' + each.strip() +':7001/wls-wsat/CoordinatorPortType'
			print each
			try:
				res = requests.get(each,timeout=1)
				if res.status_code == 200:
					f1.writelines(each+'\n')
			except:
				pass

check_weblogic_wlst('al_result.txt')
