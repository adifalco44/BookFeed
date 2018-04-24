#!/usr/bin/env python2.7
# reddit.py
# fetches data from reddit

import os
import sys
import requests
import re

FIELD = 'title'
LIMIT = 5
SUBREDDITS = ['worldnews', 'politics', 'technology', 'Futurology', 'science', 'books', 'sports']
CUSTOM = ''
NUM = 0


regex = '.' # default regex if none is specified

def usage(status=0):
    print '''Usage: {} [ -f FIELD -s SUBREDDIT ] regex
    -1 LIMIT        Limit number of articles to report (default: {})
    -c SUBREDDIT    Custom Subreddit
    -n NUM		Which subreddit to search'''.format(os.path.basename(sys.argv[0]), LIMIT)
    sys.exit(status)



# Parse command line options

args = sys.argv[1:]

while len(args) and args[0].startswith('-') and len(args[0]) > 1:
    arg = args.pop(0)
    if arg == '-1':
          LIMIT = int(args.pop(0))
    elif arg == '-s':
          CUSTOM = args.pop(0)
    elif arg == '-n':
		NUM = int(args.pop(0))
    elif arg == '-h':
          usage(0)
    else:
          usage(1)

if len(args) == 1:
	regex = args[0]
elif len(args) > 1:
	usage(0)

# Main execution

if NUM is not 7:
	URL = 'https://www.reddit.com/r/' + SUBREDDITS[NUM] + '/.json' # set URL using subreddit
# check custom, if exists
elif NUM is 7:
	URL = 'https://www.reddit.com/r/' + CUSTOM + '/.json'
	try:
		reponse = requests.get(URL)
		URL = 'https://www.reddit.com/r/' + CUSTOM + '/.json' # set URL using subreddit
	except:
		pass

headers  = {'user-agent': 'reddit-{}'.format(os.environ['USER'])}

response = requests.get(URL, headers=headers)
data = response.json()

index = 1
for resource in data['data']['children']:

	fields = resource['data'] # set fields to set of data from "data"

	try:
		# search returned true
		if re.search(regex, fields[FIELD]) is not None and re.search('/r/', fields[FIELD]) is None:
			if index <= LIMIT:
				# print output
				print fields[FIELD].encode('utf-8')
				index += 1
			else:
				continue

	# catch KeyErrors
	except KeyError:
		continue
