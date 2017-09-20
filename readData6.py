#!/usr/bin/env python2.7

import sys
import os
import GoogleImg

urls = []

with open('search6.txt','r') as f:
	for line in f.readlines():
		url = os.popen(line).read()
		urls.append(url)

with open('url6.txt','wb') as f:
	for url in urls:
		f.write(url+'\n')
