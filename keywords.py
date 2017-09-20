#!/usr/bin/env python2.7
# -*- coding=: utf-8 -*-


import os
import sys
import requests
import re
import string
from textblob import TextBlob

PUNCT = '!"#$%&\'()*+,./:;<=>?@[\\]^_`{|}~-'
# filename = 'common2.txt'

'''with open(filename, 'r') as f:
	common = f.readlines()
common = [x.strip() for x in common]
'''

for line in sys.stdin:
	line.translate(None, PUNCT)
	sentence = TextBlob(line)
	if sentence is not None:
		print ':'.join(sentence.noun_phrases)

'''	for word in words:
		word = word.translate(None, PUNCT).lower()
		word = re.sub(r'[^\x00-\x7f]',r'', word)
		if word not in common and re.search('[^0-9]$', word) is not None and re.search('[^s]$', word) is not None and re.search('[^ing]$', word) is not None and 
re.search('[^ed]$', word) is not None:
			print word
'''
