#!/usr/bin/env python2.7 
import sys
import os
import string
	#Compiles sports page	
os.system("cat test.txt | ./createSportsPage.py")

	#Compiles science page
os.system("cat test.txt | ./createSciencePage.py")

	#Compiles politics page
os.system("cat test.txt | ./createPoliticsPage.py")

	#Compiles futurology page
os.system("cat test.txt | ./createFuturologyPage.py")

	#Compiles tech page
os.system("cat test.txt | ./createTechnologyPage.py")

	#Compiles news page
os.system("cat test.txt | ./createWorldnewsPage.py")

	#Compiles books page
os.system("cat test.txt | ./createBooksPage.py")

os.system("./test_output.py")
