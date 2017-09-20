#!/usr/bin/env python2.7
import string
import sys
#import StrinIO
#import csv
import re
import requests
import GoogleImg

pageTemplate= '''<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html style="background-color:darkviolet">
<head>
<meta content="text/html; charset=ISO-8859-1"http-equiv="content-type">
<title> Science Page </title>
<h1 style="color:red"> Trending in Science ... </h1>
</head>
<body style="background-color:darkviolet">


<h2 style="color:blue" href="https://www.google.com"> Articles </h2>

<h4 style="color:blue" href="https://www.google.com"> TO_FORMAT_W_REDDIT_LINKS </h4>

<h4 style="color:blue" href="https://www.google.com"> TO_FORMAT_W_REDDIT_LINKS </h4>

<h4 style="color:blue" href="https://www.google.com"> TO_FORMAT_W_REDDIT_LINKS </h4>


<h3 style="color:blue"> Recommended Entry 1 </h3>

<p style="color:green">  Title: {T1} </p>
<p style="color:green">  Author: {A1} </p>
<p style="color:green"><img src="sciJP1.png" alt="Image 1" width="100" height="100" align="right"/>  Title: {S1} </p>

<h3 style="color:blue"> Recommended Entry 2 </h3>

<p style="color:green">  Title: {T2} </p>
<p style="color:green">  Author: {A2} </p>
<p style="color:green"><img src="sciJP2.png" alt="Image 2" width="100" height="100" align="right"/>  Title: {S2} </p>

<h3 style="color:blue"> Recommended Entry 3 </h3>

<p style="color:green">  Title: {T3} </p>
<p style="color:green">  Author: {A3} </p>
<p style="color:green"><img src="sciJP3.png" alt="Image 3" width="100" height="100" align="right"/>  Title: {S3} </p>

<h3 style="color:blue"> Recommended Entry 4 </h3>

<p style="color:green">  Title: {T4} </p>
<p style="color:green">  Author: {A4} </p>
<p style="color:green"><img src="sciJP4.png" alt="Image 4" width="100" height="100" align="right"/>  Title: {S4} </p>

<h3 style="color:blue"> Recommended Entry 5 </h3>

<p style="color:green">  Title: {T5} </p>
<p style="color:green">  Author: {A5} </p>
<p style="color:green"><img src="sciJP5.png" alt="Image 5" width="100" height="100" align="right"/>  Title: {S5} </p>

<p></p>
<a href="file:///Users/rental/HACKATHON/tempBrowseLocal.html"> previous_link</a>

</body>
</html>
'''

def main():
    #VARIABLES TO BE USED IN FUNCTIONS
    T1 = " "
    A1 = " "
    T2 = " "
    A2 = " "
    T3 = " "
    A3 = " "
    T4 = " "
    A4 = " "
    T5 = " "
    A5 = " "

    S1 = " "
    S2 = " "
    S3 = " "
    S4 = " "
    S5 = " "

    linecount = 1
    for line in sys.stdin:
	string = "cat {} | tee science".format(line)
	os.system(string)
	print(line)
 #       linecount=linecount + 1
        line.strip()
        if (linecount == 1):
            line = line.split(':$:')
            T1 = line[0]
            A1 = line[1]
            A1 = A1.translate(None, ' ,').rstrip()
            T1 = T1.translate(None, ' ,').rstrip()
            full = A1 +  '+' + T1
            string = 'cat {} | ./GoogleImg.py | head -n 2 | tail -n 1 > science'.format(full)
            os.popen(string)
#           response = requests.get(JP1)
#           with open('sciJP1.png', 'wb') as pic:
#                 for chunk in JP1:
#                      pic.write(chunk)

        if (linecount == 2):
            line = line.split(':$:')
            T2 = line[0]
            A2 = line[1]
            A2 = A2.translate(None, ' ,').rstrip()
            T2 = T2.translate(None, ' ,').rstrip()
            full = A2 +  '+' + T2
            string = 'cat {} | ./GoogleImg.py | head -n 2 | tail -n 1 '.format(full)
            JP2 = os.popen(string)
            response = requests.get(JP2)
            with open('sciJP2.png', 'wb') as pic:
                 for chunk in JP2:
                      pic.write(chunk)

        if (linecount == 3):
            line = line.split(':$:')
            T3 = line[0]
            A3 = line[1]
            A3 = A3.translate(None, ' ,').rstrip()
            T3 = T3.translate(None, ' ,').rstrip()
            full = A3 +  '+' + T3
            string = 'cat {} | ./GoogleImg.py | head -n 2 | tail -n 1 '.format(full)
            JP3 = os.popen(string)
            response = requests.get(JP3)
            with open('sciJP3.png', 'wb') as pic:
                 for chunk in JP3:
                      pic.write(chunk)
        if (linecount == 4):
            line = line.split(':$:')
            T4 = line[0]
            A4 = line[1]
            A4 = A4.translate(None, ' ,').rstrip()
            T4 = T4.translate(None, ' ,').rstrip()
            full = A4 +  '+' + T4
            string = 'cat {} | ./GoogleImg.py | head -n 2 | tail -n 1 '.format(full)
            JP4 = os.popen(string)
            response = requests.get(JP4)
            with open('sciJP4.png', 'wb') as pic:
                 for chunk in JP4:
                      pic.write(chunk)

        if (linecount == 5):
            line = line.split(':$:')
            T5 = line[0]
            A5 = line[1]
            A5 = A5.translate(None, ' ,').rstrip()
            T5 = T5.translate(None, ' ,').rstrip()
            full = A5 +  '+' + T5
            string = 'cat {} | ./GoogleImg.py | head -n 2 | tail -n 1 '.format(full)
            JP5 = os.popen(string)
            response = requests.get(JP5)
            with open('sciJP5.png', 'wb') as pic:
                 for chunk in JP5:
                      pic.write(chunk)
    print(T5)
    contents = pageTemplate.format(**locals())
    browseLocal(contents)

def strToFile(text, filename):
    output = open("ScienceSub.html","w")
    output.write(text)
    output.close()

def browseLocal(webpageText, filename='ScienceSub.html'):
    import webbrowser, os.path
    strToFile(webpageText, filename)

main()
