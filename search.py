#!/usr/bin/env python2.7
# search.py


import sys
import os
import requests
import subprocess
import urllib2
import string
import re
from lxml import etree

URL = 'https://5q2kx9wux7.execute-api.us-east-1.amazonaws.com/dev/search?query='

keyword = []

for line in sys.stdin:
	words = line.split(':')
	for word in words:
		keyword.append(word.rstrip())

headers = {'x-api-key': 'WyOS4BNZ3K4h8WwbqGwfO57Y1MqXmwgI8RGWalEs'}


for word in keyword:
	print word
	word = word.replace(" ", "_")
	if os.path.isfile('./caches/'+word+'.txt'):
		pass
	else:
		with open('./caches/'+word+'.txt','w') as x:
			word = word.replace("_", " ")
			url = URL + word
			f = requests.get(url, headers=headers)
			x.write(f.content)

	word = word.replace(" ", "_")

	f = open('./caches/'+word+'.txt', 'r')
	data = f.read().replace('\n', '')

	sorts = re.findall('<sort>[\s\S]*?</sort>', data, re.DOTALL)
	sorts = "\n".join(sorts)

	titles = []
	authors = []

	for x in sorts.split('\n'):
		if re.match('.*<author>.*', x) and re.match('.*<title>.*', x):
			try:
				temp1 = re.findall('<title>[^<|&]*<', x, re.DOTALL)[0]
			except:
				temp1 = 'N\/A'
			try:
				temp2 = re.findall('<author>[^<|&]*<', x, re.DOTALL)[0]
			except:
				temp2 = 'N\/A'
			if temp1 != 'N\/A' and temp2 != 'N\/A':
				titles.append(temp1)
				authors.append(temp2)

	#titles = re.findall('<title>[^<|&]*<', sorts, re.DOTALL)
	#titles = list(set(titles))

	#authors = re.findall('<author>[^<|&]*<', sorts, re.DOTALL)
	#authors = list(set(authors))

	titles = [line.translate(None, '<>$/').replace('title', '') for line in titles]
	titles = [re.sub(' +$', '', line) for line in titles]
	authors = [line.translate(None, '<>$/1234567890-.').replace('author', '') for line in authors]
	authors = [re.sub(', +$', '', line) for line in authors]

	counter = 0
	while counter < len(titles) and counter < len(authors):
		print titles[counter] + ' :$: ' + authors[counter]
		counter += 1
