#!/usr/bin/env python2.7
# reddit.py
# fetches data from reddit

import os
import sys
import requests
import re

SPORTS='true'
SCIENCE='true'
FUTUROLOGY='true'
TECHNOLOGY='true'
WORLD_NEWS='true'
POLITICS='true'
BOOKS='true'
MEMES='true'

csub = "memes" # custom subreddit

# Main execution

# POST STEPHEN / USER INTERFACE GENERATION
# USING container data 1-8 for formatting

if (MEMES):
     #Compiles books page
        os.system("rm url*  *.html")
	os.system("./topreddit1.py -n 7 -s {} | tee reddits.txt | ./keywords.py | tee keys.txt | ./strip.py | ./search.py | ./shuffle.py  2> /dev/null | head -n 5 > data8.txt 2> /dev/null".format(csub))
        os.system("./callGoogleImg.py -n 8")
        os.system("./readData8.py")
	os.system("cat data8.txt | ./createCustomPage.py")
os.system("./test_output.py 2> /dev/null")
