# -*- coding: UTF-8 -*-
#author:ailann

#调用nmap进行存活探测
#探测b段存活主机
#nmap -v -sn -PE -n --min-hostgroup 1024 --min-parallelism 1024 -oX nmap_output.xml www.lijiejie.com/16

import sys
import subprocess
import nmap_parse

def scan_alive(ipf_segment):
	#逐行读取ip段对对存活进行探测
	with open(ipf_segment) as f:
		for each in f:
			each = each.strip()
			cmd = 'nmap -v -sn -PE -n --min-hostgroup 1024 --min-parallelism 1024 -oX nmap_alive.xml %s' %each

			#执行命令
			print 'cmd : %s ' %cmd
			p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
			for line in p.stdout.readlines():
				#print line
				pass
			
			
			#判断命令是否执行完成
			print '%s scan dowm' %each
			#解析nmap_alive.xml
			nmap_parse.parse_alive('nmap_alive.xml')
			print '%s parse down' %each
			
