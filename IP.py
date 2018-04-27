#coding:utf-8
#filename:*.py
#author:h4ck0ne
#2017- 1 1 1
#!/usr/bin/env python

import netaddr
import sys

#
def ip_segment(ip_file):
	try:
		f_segemt = open("ipf_segment.txt",'w')
	except:
		print 'open ipf_segemt error'
		sys.exit()

	with open(ip_file, "r") as f:
    		for line in f:
        		ip = line.strip().split()
        		print ip
        		prx = netaddr.IPRange(ip[0],ip[1]).cidrs()[0].prefixlen
        		ip = ip[0] +'/' +str(prx) +'\n'
        		f_segemt.writelines(ip)




