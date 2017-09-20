#!/usr/bin/env python2.7
import string
import sys
import re
import requests
import os

pageTemplate= '''<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html style="background-color:lightblue">
<head>
<meta content="text/html; charset=ISO-8859-1"http-equiv="content-type">
<title> World News Page </title>
<h1 style="color:red"> Trending in World News ... </h1>
</head>
<body style="background-color:lightblue">


<h2 style="color:blue" href="https://www.google.com"> Articles </h2>

<h4 style="color:blue" href="https://www.google.com"> {R1} </h4>

<h4 style="color:blue" href="https://www.google.com"> {R2} </h4>

<h4 style="color:blue" href="https://www.google.com"> {R3} </h4>

<h4 style="color:blue" href="https://www.google.com"> {R4} </h4>

<h4 style="color:blue" href="https://www.google.com"> {R5} </h4>


<h3 style="color:blue"> Recommended Entry 1 </h3>

<p style="color:black" align="center">  Title: {T1} </p>
<p style="color:black" align="center">  Author: {A1} </p>
<p style="color:black" align="center">  Tags: {S1} </p>
<img src={P1}  alt="https://s-media-cache-ak0.pinimg.com/originals/83/0b/dc/830bdcaa5487b17913cc218b627d98f0.png" width="128" height="128" align="center"/>

<h3 style="color:blue"> Recommended Entry 2 </h3>

<p style="color:black" align="center">  Title: {T2} </p>
<p style="color:black" align="center">  Author: {A2} </p>
<p style="color:black" align="center">  Tags: {S2} </p>
<img src={P2} alt="https://s-media-cache-ak0.pinimg.com/originals/83/0b/dc/830bdcaa5487b17913cc218b627d98f0.png" width="128" height="128" align="center"/>

<h3 style="color:blue"> Recommended Entry 3 </h3>

<p style="color:black" align="center">  Title: {T3} </p>
<p style="color:black" align="center">  Author: {A3} </p>
<p style="color:black" align="center">  Tags: {S3} </p>
<img src={P3} alt="https://s-media-cache-ak0.pinimg.com/originals/83/0b/dc/830bdcaa5487b17913cc218b627d98f0.png" width="128" height="128" align="center"/>

<h3 style="color:blue"> Recommended Entry 4 </h3>

<p style="color:black" align="center">  Title: {T4} </p>
<p style="color:black" align="center">  Author: {A4} </p>
<p style="color:black" align="center">  Tags: {S4} </p>
<img src={P4} alt="https://s-media-cache-ak0.pinimg.com/originals/83/0b/dc/830bdcaa5487b17913cc218b627d98f0.png" width="128" height="128" align="center"/>

<h3 style="color:blue"> Recommended Entry 5 </h3>

<p style="color:black" align="center">  Title: {T5} </p>
<p style="color:black" align="center">  Author: {A5} </p>
<p style="color:black" align="center">  Tags: {S5} </p>
<img src={P5} alt="https://s-media-cache-ak0.pinimg.com/originals/83/0b/dc/830bdcaa5487b17913cc218b627d98f0.png" width="128" height="128" align="center"/>


<p></p>
<a href="file:///Users/rental/HACKATHON/tempBrowseLocal.html"> previous_link</a>

</body>
</html>
'''

def strToFile(text, filename):
    output = open("WorldnewsSub.html","w")
    output.write(text)
    output.close()

def browseLocal(webpageText, filename='WorldnewsSub.html'):
    import webbrowser, os.path
    strToFile(webpageText, filename)

with open('reddits.txt','r') as f:
    head = [next(f) for x in xrange(5)]

R1 = head[0]
R2 = head[1]
R3 = head[2]
R4 = head[3]
R5 = head[4]

tags = []
big = ''

with open('keys.txt','r') as f:
    for line in f.readlines():
        line = line.split(':')
        for word in line:
            big = big + '#' + word.translate(None, ' ')
        tags.append(big)
        big = ''

S1 = tags[0]
S2 = tags[1]
S3 = tags[2]
S4 = tags[3]
S5 = tags[4]

urls = []

with open('url1.txt','r') as f:
    for line in f.readlines():
        line = line.rstrip()
        line = '\"' + line + '\"'
        urls.append(line)

P1 = urls[0]
P2 = urls[1]
P3 = urls[2]
P4 = urls[3]
P5 = urls[4]

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

strings = []

linecount = 0
for line in sys.stdin:
    linecount=linecount + 1
    if (linecount == 1):
        line = line.split(':$:')
        T1 = line[0]
        A1 = line[1]
        A1 = A1.translate(None, ',').rstrip()
        T1 = T1.translate(None, ',').rstrip()
        full = A1 +  '+' + T1
        string = 'cat {} | ./GoogleImg.py | head -n 2 | tail -n 1 '.format(full)
        strings.append(string)
    if (linecount == 2):
        line = line.split(':$:')
        T2 = line[0]
        A2 = line[1]
        A2 = A2.translate(None, ',').rstrip()
        T2 = T2.translate(None, ',').rstrip()
        full = A2 +  '+' + T2
        string = 'cat {} | ./GoogleImg.py | head -n 2 | tail -n 1 '.format(full)
        strings.append(string)
    if (linecount == 3):
        line = line.split(':$:')
        T3 = line[0]
        A3 = line[1]
        A3 = A3.translate(None, ',').rstrip()
        T3 = T3.translate(None, ',').rstrip()
        full = A3 +  '+' + T3
        string = 'cat {} | ./GoogleImg.py | head -n 2 | tail -n 1 '.format(full)
        strings.append(string)
    if (linecount == 4):
        line = line.split(':$:')
        T4 = line[0]
        A4 = line[1]
        A4 = A4.translate(None, ',').rstrip()
        T4 = T4.translate(None, ',').rstrip()
        full = A4 +  '+' + T4
        string = 'cat {} | ./GoogleImg.py | head -n 2 | tail -n 1 '.format(full)
        strings.append(string)
    if (linecount == 5):
        line = line.split(':$:')
        T5 = line[0]
        A5 = line[1]
        A5 = A5.translate(None, ',').rstrip()
        T5 = T5.translate(None, ',').rstrip()
        full = A5 +  '+' + T5
        string = 'cat {} | ./GoogleImg.py | head -n 2 | tail -n 1 '.format(full)
        strings.append(string)

contents = pageTemplate.format(**locals())
browseLocal(contents)

