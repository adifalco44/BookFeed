#!/usr/bin/env python2.7
# reddit.py
# fetches data from reddit

import os
import sys
import requests
import re
import GoogleImg

SPORTS='true'
SCIENCE='true'
FUTUROLOGY='true'
TECHNOLOGY='true'
WORLD_NEWS='true'
POLITICS='true'
BOOKS='true'
CUSTOM='true'

csub = "memes" # custom subreddit

# Main execution

# POST STEPHEN / USER INTERFACE GENERATION
# USING container data 1-8 for formatting

if (WORLD_NEWS):
	#Compiles sports page	
	os.system("./topreddit1.py -n 0 | ./keywords.py | ./strip.py | ./search.py | ./shuffle.py | head -n 5 > data1.txt") 
	os.system("cat data1.txt | ./callGoogleImg.py")
	os.system("cat data1.txt | ./createWorldnewsPage.py")

if (POLITICS):
	#Compiles science page
	os.system("./topreddit1.py -n 1 | ./keywords.py | ./strip.py | ./search.py | ./shuffle.py | head -n 5 > data2.txt")
	os.system("cat data2.txt | ./callGoogleImg.py")
	os.system("cat L2.txt | ./PNGget.py")
	os.system("cat data2.txt | ./createPoliticsPage.py")

if (TECHNOLOGY):
	#Compiles politics page
	os.system("./topreddit1.py -n 2 | ./keywords.py | ./strip.py | ./search.py | ./shuffle.py | head -n 5 > data3.txt")
	os.system("cat data3.txt | ./callGoogleImg.py")
	os.system("cat L3.txt | ./PNGget.py")
	os.system("cat data3.txt | ./createTechnologyPage.py")

if (FUTUROLOGY):
	#Compiles futurology page
	os.system("./topreddit1.py -n 3 | ./keywords.py | ./strip.py | ./search.py| ./shuffle.py | head -n 5  > data4.txt")
	os.system("cat data4.txt | ./callGoogleImg.py")
	os.system("cat L4.txt | ./PNGget.py")
	os.system("cat data4.txt | ./createFuturologyPage.py")

if (SCIENCE):
	#Compiles tech page
	os.system("./topreddit1.py -n 4 | ./keywords.py | ./strip.py | ./search.py | ./shuffle.py | head -n 5 > data5.txt")
	os.system("cat data5.txt | ./callGoogleImg.py")
	os.system("cat L5.txt | ./PNGget.py")
	os.system("cat data5.txt | ./createSciencePage.py")

if (BOOKS):
	#Compiles news page
	os.system("./topreddit1.py -n 5 | ./keywords.py | ./strip.py |./search.py | ./shuffle.py | head -n 5 > data6.txt")
	os.system("cat data6.txt | ./callGoogleImg.py")
	os.system("cat L6.txt | ./PNGget.py")
	os.system("cat data6.txt | ./createBooksPage.py")

if (SPORTS):
	#Compiles books page
	os.system("./topreddit1.py -n 6 | ./keywords.py | ./strip.py | ./search.py | shuffle.py | head -n 5 > data7.txt")
	os.system("cat data7.txt | ./callGoogleImg.py")
	os.system("cat L7.txt | ./PNGget.py")
	os.system("cat data7.txt | ./createSportsPage.py")

if (CUSTOM):
        #Compiles books page
	os.system("./topreddit1.py -n 7 -s {} | ./keywords.py | ./strip.py | ./search.py | ./shuffle.py | head -n 5 > data8.txt".format(csub))
	os.system("cat data8.txt | ./callGoogleImg.py")
	os.system("cat L8.txt | ./PNGget.py")
        os.system("cat data8.txt | ./createCustomPage.py")

os.system("./test_output.py")
