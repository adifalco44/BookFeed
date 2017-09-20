#!/usr/bin/env python2.7
import os
import sys
import cStringIO
import pprint
import urllib2

search_field=""

for item in sys.stdin:
   data=item.split('+')
   for stuff in data:
	meta=stuff.split('_')
	for junk in meta:
		search_field=search_field+'+'+junk	

search_field=search_field+'+'+"Book"

from apiclient.discovery import build

service = build("customsearch", "v1",developerKey="AIzaSyBCUFX0i3c1fIqJ0uBKPa8i6UDueuqPqTg")

res = service.cse().list(
    q=search_field,
    cx='002294040637880126439:nfz7o5ajhri',
    searchType='image',
    num=3,
    imgType='clipart',
    fileType='png',
    safe= 'off'
).execute()
count = 0
match = "https"
if not 'items' in res:
    print 'No result !!\nres is: {}'.format(res)
else:
    for item in res['items']:
	print('{}:\n\t{}'.format(item['title'],item['link']))
	count=count+1
