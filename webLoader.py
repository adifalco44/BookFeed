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

os.system("rm url* search*.txt *.html")

if (WORLD_NEWS):
	#Compiles sports page
	os.system("./topreddit1.py -n 0 | tee reddits.txt | ./keywords.py | tee keys.txt | ./strip.py | ./search.py | ./shuffle.py | head -n 5 > data1.txt 2> /dev/null") 
	os.system("./callGoogleImg.py -n 1")
	os.system("./readData1.py")
	os.system("cat data1.txt | ./createWorldnewsPage.py")

if (POLITICS):
	#Compiles science page
	os.system("./topreddit1.py -n 1 | tee reddits.txt | ./keywords.py | tee keys.txt | ./strip.py | ./search.py | ./shuffle.py | head -n 5 > data2.txt 2> /dev/null")
        os.system("./callGoogleImg.py -n 2")
        os.system("./readData2.py")
	os.system("cat data2.txt | ./createPoliticsPage.py")

if (TECHNOLOGY):
	#Compiles politics page
	os.system("./topreddit1.py -n 2 | tee reddits.txt | ./keywords.py | tee keys.txt | ./strip.py | ./search.py | ./shuffle.py  2> /dev/null | head -n 5 > data3.txt 2> /dev/null")
        os.system("./callGoogleImg.py -n 3")
        os.system("./readData3.py")
	os.system("cat data3.txt | ./createTechnologyPage.py")

if (FUTUROLOGY):
	#Compiles futurology page
	os.system("./topreddit1.py -n 3 | tee reddits.txt | ./keywords.py | tee keys.txt | ./strip.py | ./search.py| ./shuffle.py  2> /dev/null | head -n 5  > data4.txt 2> /dev/null")
        os.system("./callGoogleImg.py -n 4")
        os.system("./readData4.py")
	os.system("cat data4.txt | ./createFuturologyPage.py")

if (SCIENCE):
	#Compiles tech page
	os.system("./topreddit1.py -n 4 | tee reddits.txt | ./keywords.py | tee keys.txt | ./strip.py | ./search.py | ./shuffle.py  2> /dev/null | head -n 5 > data5.txt 2> /dev/null")
        os.system("./callGoogleImg.py -n 5")
        os.system("./readData5.py")
	os.system("cat data5.txt | ./createSciencePage.py")

if (BOOKS):
	#Compiles news page
	os.system("./topreddit1.py -n 5 | tee reddits.txt | ./keywords.py | tee keys.txt | ./strip.py |./search.py | ./shuffle.py  2> /dev/null | head -n 5 > data6.txt 2> /dev/null")
        os.system("./callGoogleImg.py -n 6")
        os.system("./readData6.py")
	os.system("cat data6.txt | ./createBooksPage.py")

if (SPORTS):
	#Compiles books page
	os.system("./topreddit1.py -n 6 | tee reddits.txt | ./keywords.py | tee keys.txt | ./strip.py | ./search.py | shuffle.py  2> /dev/null | head -n 5 > data7.txt 2> /dev/null")
        os.system("./callGoogleImg.py -n 7")
        os.system("./readData7.py")
	os.system("cat data7.txt | ./createSportsPage.py")

if (MEMES):
     #Compiles books page
	os.system("./topreddit1.py -n 7 -s {} | tee reddits.txt | ./keywords.py | tee keys.txt | ./strip.py | ./search.py | ./shuffle.py  2> /dev/null | head -n 5 > data8.txt 2> /dev/null".format(csub))
        os.system("./callGoogleImg.py -n 8")
        os.system("./readData8.py")
	os.system("cat data8.txt | ./createCustomPage.py")

os.system("./test_output.py 2> /dev/null")
