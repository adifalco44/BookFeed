#!/usr/bin/env python2.7
import os
import sys
import cStringIO
import pprint
import urllib2
import string

search_field=""

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
	print('{}:\n{}'.format(item['title'], item['link']))

