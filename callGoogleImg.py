#!/usr/bin/env python2.7

import string
import sys
import csv
import os
import re
import requests
#import GoogleImg
import requests

PUNCT = '!"#$%&\'()*+,./:;<=>?@[\\]^_`{|}~'

NUM = 1

args = sys.argv[1:]

while len(args) and args[0].startswith('-') and len(args[0]) > 1:
    arg = args.pop(0)
    if arg == '-n':
          NUM = int(args.pop(0))

filename = ''
out = ''

if NUM == 1:
	filename = 'data1.txt'
	out = 'search1.txt'
elif NUM == 2:
	filename = 'data2.txt'
	out = 'search2.txt'
elif NUM == 3:
	filename = 'data3.txt'
	out = 'search3.txt'
elif NUM == 4:
	filename = 'data4.txt'
	out = 'search4.txt'
elif NUM == 5:
	filename = 'data5.txt'
	out = 'search5.txt'
elif NUM == 6:
	filename = 'data6.txt'
	out = 'search6.txt'
elif NUM == 7:
	filename = 'data7.txt'
	out = 'search7.txt'
elif NUM == 8:
	filename = 'data8.txt'
	out = 'search8.txt'

urls = []

with open(filename, 'r') as f:
	for line in f.readlines():
		line = line.split(':$:')
		line = [x.translate(None, PUNCT) for x in line]
		line = '+'.join(line)
		line = line.replace(" ", "+")
		line = line.translate(None, ' ').rstrip()
		line = line.replace('+++','+')
		line = line.replace('++','+')
		str = "echo {} | ./GoogleImg.py | grep http".format(line)
		urls.append(str)

with open(out, 'wb') as f:
	for url in urls:
		f.write(url+'\n')
