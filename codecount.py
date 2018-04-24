#!/usr/bin/env python2.7
# 
import os
# calls CreateBookList for each subreddit
for subreddit in 1,2,3,4,5
    #returns list of books for each subreddit
    books = popen('./CreateBookList.py ' + '-s ' + subreddit )
    # makes html page for the values returned from CreateBookList
    links = popen('./GenerateHTML '  + books)
#!/usr/bin/env python2.7
import string
import sys
import csv
import os
import re
import requests
#import GoogleImg
import requests
PUNCT = '!"#$%&\'()*+,./:;<=>?@[\\]^_`{|}~'
NUM = 1
args = sys.argv[1:]
while len(args) and args[0].startswith('-') and len(args[0]) > 1:
    arg = args.pop(0)
    if arg == '-n':
          NUM = int(args.pop(0))
filename = ''
out = ''
if NUM == 1:
	filename = 'data1.txt'
	out = 'search1.txt'
elif NUM == 2:
	filename = 'data2.txt'
	out = 'search2.txt'
elif NUM == 3:
	filename = 'data3.txt'
	out = 'search3.txt'
elif NUM == 4:
	filename = 'data4.txt'
	out = 'search4.txt'
elif NUM == 5:
	filename = 'data5.txt'
	out = 'search5.txt'
elif NUM == 6:
	filename = 'data6.txt'
	out = 'search6.txt'
elif NUM == 7:
	filename = 'data7.txt'
	out = 'search7.txt'
elif NUM == 8:
	filename = 'data8.txt'
	out = 'search8.txt'
urls = []
with open(filename, 'r') as f:
	for line in f.readlines():
		line = line.split(':$:')
		line = [x.translate(None, PUNCT) for x in line]
		line = '+'.join(line)
		line = line.replace(" ", "+")
		line = line.translate(None, ' ').rstrip()
		line = line.replace('+++','+')
		line = line.replace('++','+')
		str = "echo {} | ./GoogleImg.py | grep http".format(line)
		urls.append(str)
with open(out, 'wb') as f:
	for url in urls:
		f.write(url+'\n')
#!/usr/bin/env python2.7
# CreateBookList.py
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
<title> Books Page </title>
<h1 style="color:red"> Trending in Books ... </h1>
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
    output = open("BooksSub.html","w")
    output.write(text)
    output.close()
def browseLocal(webpageText, filename='BooksSub.html'):
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
with open('url6.txt','r') as f:
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
<title> Custom Reddit Page </title>
<h1 style="color:red"> Trending ... </h1>
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
    output = open("CustomSub.html","w")
    output.write(text)
    output.close()
def browseLocal(webpageText, filename='CustomSub.html'):
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
with open('url8.txt','r') as f:
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
<title> Futurology Page </title>
<h1 style="color:red"> Trending in Futurology ... </h1>
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
    output = open("FuturologySub.html","w")
    output.write(text)
    output.close()
def browseLocal(webpageText, filename='FuturologySub.html'):
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
with open('url4.txt','r') as f:
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
<title> Politics Page </title>
<h1 style="color:red"> Trending in Politics ... </h1>
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
    output = open("PoliticsSub.html","w")
    output.write(text)
    output.close()
def browseLocal(webpageText, filename='PoliticsSub.html'):
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
with open('url2.txt','r') as f:
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
<title> Science Page </title>
<h1 style="color:red"> Trending in Science ... </h1>
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
    output = open("ScienceSub.html","w")
    output.write(text)
    output.close()
def browseLocal(webpageText, filename='ScienceSub.html'):
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
with open('url5.txt','r') as f:
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
<title> Sports Page </title>
<h1 style="color:red"> Trending in Sports ... </h1>
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
    output = open("SportsSub.html","w")
    output.write(text)
    output.close()
def browseLocal(webpageText, filename='SportsSub.html'):
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
with open('url7.txt','r') as f:
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
<title> Technology Page </title>
<h1 style="color:red"> Trending in Technology ... </h1>
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
    output = open("TechnologySub.html","w")
    output.write(text)
    output.close()
def browseLocal(webpageText, filename='TechnologySub.html'):
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
with open('url3.txt','r') as f:
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
#!/usr/bin/env python2.7
from PIL
for line in sys.stdin:
#	if count != 0:
#
#	if count == 0:
#		num = line
#		count = 1
#		pic = "L{}.txt".format(num)
r=png.Reader(file=urllib.urlopen(''))
#!/usr/bin/env python
from __future__ import print_function
# png.py - PNG encoder/decoder in pure Python
#
# Copyright (C) 2006 Johann C. Rocholl <johann@browsershots.org>
# Portions Copyright (C) 2009 David Jones <drj@pobox.com>
# And probably portions Copyright (C) 2006 Nicko van Someren <nicko@nicko.org>
#
# Original concept by Johann C. Rocholl.
#
# LICENCE (MIT)
#
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation files
# (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge,
# publish, distribute, sublicense, and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS
# BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN
# ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
"""
Pure Python PNG Reader/Writer
This Python module implements support for PNG images (see PNG
specification at http://www.w3.org/TR/2003/REC-PNG-20031110/ ). It reads
and writes PNG files with all allowable bit depths
(1/2/4/8/16/24/32/48/64 bits per pixel) and colour combinations:
greyscale (1/2/4/8/16 bit); RGB, RGBA, LA (greyscale with alpha) with
8/16 bits per channel; colour mapped images (1/2/4/8 bit).
Adam7 interlacing is supported for reading and
writing.  A number of optional chunks can be specified (when writing)
and understood (when reading): ``tRNS``, ``bKGD``, ``gAMA``.
For help, type ``import png; help(png)`` in your python interpreter.
A good place to start is the :class:`Reader` and :class:`Writer`
classes.
Requires Python 2.3.  Limited support is available for Python 2.2, but
not everything works.  Best with Python 2.4 and higher.  Installation is
trivial, but see the ``README.txt`` file (with the source distribution)
for details.
This file can also be used as a command-line utility to convert
`Netpbm <http://netpbm.sourceforge.net/>`_ PNM files to PNG, and the
reverse conversion from PNG to PNM. The interface is similar to that
of the ``pnmtopng`` program from Netpbm.  Type ``python png.py --help``
at the shell prompt for usage and a list of options.
A note on spelling and terminology
----------------------------------
Generally British English spelling is used in the documentation.  So
that's "greyscale" and "colour".  This not only matches the author's
native language, it's also used by the PNG specification.
The major colour models supported by PNG (and hence by PyPNG) are:
greyscale, RGB, greyscale--alpha, RGB--alpha.  These are sometimes
referred to using the abbreviations: L, RGB, LA, RGBA.  In this case
each letter abbreviates a single channel: *L* is for Luminance or Luma
or Lightness which is the channel used in greyscale images; *R*, *G*,
*B* stand for Red, Green, Blue, the components of a colour image; *A*
stands for Alpha, the opacity channel (used for transparency effects,
but higher values are more opaque, so it makes sense to call it 
opacity).
A note on formats
-----------------
When getting pixel data out of this module (reading) and presenting
data to this module (writing) there are a number of ways the data could
be represented as a Python value.  Generally this module uses one of
three formats called "flat row flat pixel", "boxed row flat pixel", and
"boxed row boxed pixel".  Basically the concern is whether each pixel
and each row comes in its own little tuple (box), or not.
Consider an image that is 3 pixels wide by 2 pixels high, and each pixel
has RGB components:
Boxed row flat pixel::
  list([R,G,B, R,G,B, R,G,B],
       [R,G,B, R,G,B, R,G,B])
Each row appears as its own list, but the pixels are flattened so
that three values for one pixel simply follow the three values for
the previous pixel.  This is the most common format used, because it
provides a good compromise between space and convenience.  PyPNG regards
itself as at liberty to replace any sequence type with any sufficiently
compatible other sequence type; in practice each row is an array (from
the array module), and the outer list is sometimes an iterator rather
than an explicit list (so that streaming is possible).
Flat row flat pixel::
  [R,G,B, R,G,B, R,G,B,
   R,G,B, R,G,B, R,G,B]
The entire image is one single giant sequence of colour values.
Generally an array will be used (to save space), not a list.
Boxed row boxed pixel::
  list([ (R,G,B), (R,G,B), (R,G,B) ],
       [ (R,G,B), (R,G,B), (R,G,B) ])
Each row appears in its own list, but each pixel also appears in its own
tuple.  A serious memory burn in Python.
In all cases the top row comes first, and for each row the pixels are
ordered from left-to-right.  Within a pixel the values appear in the
order, R-G-B-A (or L-A for greyscale--alpha).
There is a fourth format, mentioned because it is used internally,
is close to what lies inside a PNG file itself, and has some support
from the public API.  This format is called packed.  When packed,
each row is a sequence of bytes (integers from 0 to 255), just as
it is before PNG scanline filtering is applied.  When the bit depth
is 8 this is essentially the same as boxed row flat pixel; when the
bit depth is less than 8, several pixels are packed into each byte;
when the bit depth is 16 (the only value more than 8 that is supported
by the PNG image format) each pixel value is decomposed into 2 bytes
(and `packed` is a misnomer).  This format is used by the
:meth:`Writer.write_packed` method.  It isn't usually a convenient
format, but may be just right if the source data for the PNG image
comes from something that uses a similar format (for example, 1-bit
BMPs, or another PNG file).
And now, my famous members
--------------------------
"""
__version__ = "0.0.18"
import itertools
import math
import re
# http://www.python.org/doc/2.4.4/lib/module-operator.html
import operator
import struct
import sys
# http://www.python.org/doc/2.4.4/lib/module-warnings.html
import warnings
import zlib
from array import array
from functools import reduce
try:
    # `cpngfilters` is a Cython module: it must be compiled by
    # Cython for this import to work.
    # If this import does work, then it overrides pure-python
    # filtering functions defined later in this file (see `class
    # pngfilters`).
    import cpngfilters as pngfilters
except ImportError:
    pass
__all__ = ['Image', 'Reader', 'Writer', 'write_chunks', 'from_array']
# The PNG signature.
# http://www.w3.org/TR/PNG/#5PNG-file-signature
_signature = struct.pack('8B', 137, 80, 78, 71, 13, 10, 26, 10)
_adam7 = ((0, 0, 8, 8),
          (4, 0, 8, 8),
          (0, 4, 4, 8),
          (2, 0, 4, 4),
          (0, 2, 2, 4),
          (1, 0, 2, 2),
          (0, 1, 1, 2))
def group(s, n):
    # See http://www.python.org/doc/2.6/library/functions.html#zip
    return list(zip(*[iter(s)]*n))
def isarray(x):
    return isinstance(x, array)
def tostring(row):
    return row.tostring()
def interleave_planes(ipixels, apixels, ipsize, apsize):
    """
    Interleave (colour) planes, e.g. RGB + A = RGBA.
    Return an array of pixels consisting of the `ipsize` elements of
    data from each pixel in `ipixels` followed by the `apsize` elements
    of data from each pixel in `apixels`.  Conventionally `ipixels`
    and `apixels` are byte arrays so the sizes are bytes, but it
    actually works with any arrays of the same type.  The returned
    array is the same type as the input arrays which should be the
    same type as each other.
    """
    itotal = len(ipixels)
    atotal = len(apixels)
    newtotal = itotal + atotal
    newpsize = ipsize + apsize
    # Set up the output buffer
    # See http://www.python.org/doc/2.4.4/lib/module-array.html#l2h-1356
    out = array(ipixels.typecode)
    # It's annoying that there is no cheap way to set the array size :-(
    out.extend(ipixels)
    out.extend(apixels)
    # Interleave in the pixel data
    for i in range(ipsize):
        out[i:newtotal:newpsize] = ipixels[i:itotal:ipsize]
    for i in range(apsize):
        out[i+ipsize:newtotal:newpsize] = apixels[i:atotal:apsize]
    return out
def check_palette(palette):
    """Check a palette argument (to the :class:`Writer` class)
    for validity.  Returns the palette as a list if okay; raises an
    exception otherwise.
    """
    # None is the default and is allowed.
    if palette is None:
        return None
    p = list(palette)
    if not (0 < len(p) <= 256):
        raise ValueError("a palette must have between 1 and 256 entries")
    seen_triple = False
    for i,t in enumerate(p):
        if len(t) not in (3,4):
            raise ValueError(
              "palette entry %d: entries must be 3- or 4-tuples." % i)
        if len(t) == 3:
            seen_triple = True
        if seen_triple and len(t) == 4:
            raise ValueError(
              "palette entry %d: all 4-tuples must precede all 3-tuples" % i)
        for x in t:
            if int(x) != x or not(0 <= x <= 255):
                raise ValueError(
                  "palette entry %d: values must be integer: 0 <= x <= 255" % i)
    return p
def check_sizes(size, width, height):
    """Check that these arguments, in supplied, are consistent.
    Return a (width, height) pair.
    """
    if not size:
        return width, height
    if len(size) != 2:
        raise ValueError(
          "size argument should be a pair (width, height)")
    if width is not None and width != size[0]:
        raise ValueError(
          "size[0] (%r) and width (%r) should match when both are used."
            % (size[0], width))
    if height is not None and height != size[1]:
        raise ValueError(
          "size[1] (%r) and height (%r) should match when both are used."
            % (size[1], height))
    return size
def check_color(c, greyscale, which):
    """Checks that a colour argument for transparent or
    background options is the right form.  Returns the colour
    (which, if it's a bar integer, is "corrected" to a 1-tuple).
    """
    if c is None:
        return c
    if greyscale:
        try:
            len(c)
        except TypeError:
            c = (c,)
        if len(c) != 1:
            raise ValueError("%s for greyscale must be 1-tuple" %
                which)
        if not isinteger(c[0]):
            raise ValueError(
                "%s colour for greyscale must be integer" % which)
    else:
        if not (len(c) == 3 and
                isinteger(c[0]) and
                isinteger(c[1]) and
                isinteger(c[2])):
            raise ValueError(
                "%s colour must be a triple of integers" % which)
    return c
class Error(Exception):
    def __str__(self):
        return self.__class__.__name__ + ': ' + ' '.join(self.args)
class FormatError(Error):
    """Problem with input file format.  In other words, PNG file does
    not conform to the specification in some way and is invalid.
    """
class ChunkError(FormatError):
    pass
class Writer:
    """
    PNG encoder in pure Python.
    """
    def __init__(self, width=None, height=None,
                 size=None,
                 greyscale=False,
                 alpha=False,
                 bitdepth=8,
                 palette=None,
                 transparent=None,
                 background=None,
                 gamma=None,
                 compression=None,
                 interlace=False,
                 bytes_per_sample=None, # deprecated
                 planes=None,
                 colormap=None,
                 maxval=None,
                 chunk_limit=2**20,
                 x_pixels_per_unit = None,
                 y_pixels_per_unit = None,
                 unit_is_meter = False):
        """
        Create a PNG encoder object.
        Arguments:
        width, height
          Image size in pixels, as two separate arguments.
        size
          Image size (w,h) in pixels, as single argument.
        greyscale
          Input data is greyscale, not RGB.
        alpha
          Input data has alpha channel (RGBA or LA).
        bitdepth
          Bit depth: from 1 to 16.
        palette
          Create a palette for a colour mapped image (colour type 3).
        transparent
          Specify a transparent colour (create a ``tRNS`` chunk).
        background
          Specify a default background colour (create a ``bKGD`` chunk).
        gamma
          Specify a gamma value (create a ``gAMA`` chunk).
        compression
          zlib compression level: 0 (none) to 9 (more compressed);
          default: -1 or None.
        interlace
          Create an interlaced image.
        chunk_limit
          Write multiple ``IDAT`` chunks to save memory.
        x_pixels_per_unit
          Number of pixels a unit along the x axis (write a
          `pHYs` chunk).
        y_pixels_per_unit
          Number of pixels a unit along the y axis (write a
          `pHYs` chunk). Along with `x_pixel_unit`, this gives
          the pixel size ratio.
        unit_is_meter
          `True` to indicate that the unit (for the `pHYs`
          chunk) is metre.
        The image size (in pixels) can be specified either by using the
        `width` and `height` arguments, or with the single `size`
        argument.  If `size` is used it should be a pair (*width*,
        *height*).
        `greyscale` and `alpha` are booleans that specify whether
        an image is greyscale (or colour), and whether it has an
        alpha channel (or not).
        `bitdepth` specifies the bit depth of the source pixel values.
        Each source pixel value must be an integer between 0 and
        ``2**bitdepth-1``.  For example, 8-bit images have values
        between 0 and 255.  PNG only stores images with bit depths of
        1,2,4,8, or 16.  When `bitdepth` is not one of these values,
        the next highest valid bit depth is selected, and an ``sBIT``
        (significant bits) chunk is generated that specifies the
        original precision of the source image.  In this case the
        supplied pixel values will be rescaled to fit the range of
        the selected bit depth.
        The details of which bit depth / colour model combinations the
        PNG file format supports directly, are somewhat arcane
        (refer to the PNG specification for full details).  Briefly:
        "small" bit depths (1,2,4) are only allowed with greyscale and
        colour mapped images; colour mapped images cannot have bit depth
        16.
        For colour mapped images (in other words, when the `palette`
        argument is specified) the `bitdepth` argument must match one of
        the valid PNG bit depths: 1, 2, 4, or 8.  (It is valid to have a
        PNG image with a palette and an ``sBIT`` chunk, but the meaning
        is slightly different; it would be awkward to press the
        `bitdepth` argument into service for this.)
        The `palette` option, when specified, causes a colour
        mapped image to be created: the PNG colour type is set to 3;
        `greyscale` must not be set; `alpha` must not be set;
        `transparent` must not be set; the bit depth must be 1,2,4,
        or 8.  When a colour mapped image is created, the pixel values
        are palette indexes and the `bitdepth` argument specifies the
        size of these indexes (not the size of the colour values in
        the palette).
        The palette argument value should be a sequence of 3- or
        4-tuples.  3-tuples specify RGB palette entries; 4-tuples
        specify RGBA palette entries.  If both 4-tuples and 3-tuples
        appear in the sequence then all the 4-tuples must come
        before all the 3-tuples.  A ``PLTE`` chunk is created; if there
        are 4-tuples then a ``tRNS`` chunk is created as well.  The
        ``PLTE`` chunk will contain all the RGB triples in the same
        sequence; the ``tRNS`` chunk will contain the alpha channel for
        all the 4-tuples, in the same sequence.  Palette entries
        are always 8-bit.
        If specified, the `transparent` and `background` parameters must
        be a tuple with three integer values for red, green, blue, or
        a simple integer (or singleton tuple) for a greyscale image.
        If specified, the `gamma` parameter must be a positive number
        (generally, a `float`).  A ``gAMA`` chunk will be created.
        Note that this will not change the values of the pixels as
        they appear in the PNG file, they are assumed to have already
        been converted appropriately for the gamma specified.
        The `compression` argument specifies the compression level to
        be used by the ``zlib`` module.  Values from 1 to 9 specify
        compression, with 9 being "more compressed" (usually smaller
        and slower, but it doesn't always work out that way).  0 means
        no compression.  -1 and ``None`` both mean that the default
        level of compession will be picked by the ``zlib`` module
        (which is generally acceptable).
        If `interlace` is true then an interlaced image is created
        (using PNG's so far only interace method, *Adam7*).  This does
        not affect how the pixels should be presented to the encoder,
        rather it changes how they are arranged into the PNG file.
        On slow connexions interlaced images can be partially decoded
        by the browser to give a rough view of the image that is
        successively refined as more image data appears.
        .. note ::
          Enabling the `interlace` option requires the entire image
          to be processed in working memory.
        `chunk_limit` is used to limit the amount of memory used whilst
        compressing the image.  In order to avoid using large amounts of
        memory, multiple ``IDAT`` chunks may be created.
        """
        # At the moment the `planes` argument is ignored;
        # its purpose is to act as a dummy so that
        # ``Writer(x, y, **info)`` works, where `info` is a dictionary
        # returned by Reader.read and friends.
        # Ditto for `colormap`.
        width, height = check_sizes(size, width, height)
        del size
        if width <= 0 or height <= 0:
            raise ValueError("width and height must be greater than zero")
        if not isinteger(width) or not isinteger(height):
            raise ValueError("width and height must be integers")
        # http://www.w3.org/TR/PNG/#7Integers-and-byte-order
        if width > 2**32-1 or height > 2**32-1:
            raise ValueError("width and height cannot exceed 2**32-1")
        if alpha and transparent is not None:
            raise ValueError(
                "transparent colour not allowed with alpha channel")
        if bytes_per_sample is not None:
            warnings.warn('please use bitdepth instead of bytes_per_sample',
                          DeprecationWarning)
            if bytes_per_sample not in (0.125, 0.25, 0.5, 1, 2):
                raise ValueError(
                    "bytes per sample must be .125, .25, .5, 1, or 2")
            bitdepth = int(8*bytes_per_sample)
        del bytes_per_sample
        if not isinteger(bitdepth) or bitdepth < 1 or 16 < bitdepth:
            raise ValueError("bitdepth (%r) must be a positive integer <= 16" %
              bitdepth)
        self.rescale = None
        palette = check_palette(palette)
        if palette:
            if bitdepth not in (1,2,4,8):
                raise ValueError("with palette, bitdepth must be 1, 2, 4, or 8")
            if transparent is not None:
                raise ValueError("transparent and palette not compatible")
            if alpha:
                raise ValueError("alpha and palette not compatible")
            if greyscale:
                raise ValueError("greyscale and palette not compatible")
        else:
            # No palette, check for sBIT chunk generation.
            if alpha or not greyscale:
                if bitdepth not in (8,16):
                    targetbitdepth = (8,16)[bitdepth > 8]
                    self.rescale = (bitdepth, targetbitdepth)
                    bitdepth = targetbitdepth
                    del targetbitdepth
            else:
                assert greyscale
                assert not alpha
                if bitdepth not in (1,2,4,8,16):
                    if bitdepth > 8:
                        targetbitdepth = 16
                    elif bitdepth == 3:
                        targetbitdepth = 4
                    else:
                        assert bitdepth in (5,6,7)
                        targetbitdepth = 8
                    self.rescale = (bitdepth, targetbitdepth)
                    bitdepth = targetbitdepth
                    del targetbitdepth
        if bitdepth < 8 and (alpha or not greyscale and not palette):
            raise ValueError(
              "bitdepth < 8 only permitted with greyscale or palette")
        if bitdepth > 8 and palette:
            raise ValueError(
                "bit depth must be 8 or less for images with palette")
        transparent = check_color(transparent, greyscale, 'transparent')
        background = check_color(background, greyscale, 'background')
        # It's important that the true boolean values (greyscale, alpha,
        # colormap, interlace) are converted to bool because Iverson's
        # convention is relied upon later on.
        self.width = width
        self.height = height
        self.transparent = transparent
        self.background = background
        self.gamma = gamma
        self.greyscale = bool(greyscale)
        self.alpha = bool(alpha)
        self.colormap = bool(palette)
        self.bitdepth = int(bitdepth)
        self.compression = compression
        self.chunk_limit = chunk_limit
        self.interlace = bool(interlace)
        self.palette = palette
        self.x_pixels_per_unit = x_pixels_per_unit
        self.y_pixels_per_unit = y_pixels_per_unit
        self.unit_is_meter = bool(unit_is_meter)
        self.color_type = 4*self.alpha + 2*(not greyscale) + 1*self.colormap
        assert self.color_type in (0,2,3,4,6)
        self.color_planes = (3,1)[self.greyscale or self.colormap]
        self.planes = self.color_planes + self.alpha
        # :todo: fix for bitdepth < 8
        self.psize = (self.bitdepth/8) * self.planes
    def make_palette(self):
        """Create the byte sequences for a ``PLTE`` and if necessary a
        ``tRNS`` chunk.  Returned as a pair (*p*, *t*).  *t* will be
        ``None`` if no ``tRNS`` chunk is necessary.
        """
        p = array('B')
        t = array('B')
        for x in self.palette:
            p.extend(x[0:3])
            if len(x) > 3:
                t.append(x[3])
        p = tostring(p)
        t = tostring(t)
        if t:
            return p,t
        return p,None
    def write(self, outfile, rows):
        """Write a PNG image to the output file.  `rows` should be
        an iterable that yields each row in boxed row flat pixel
        format.  The rows should be the rows of the original image,
        so there should be ``self.height`` rows of ``self.width *
        self.planes`` values.  If `interlace` is specified (when
        creating the instance), then an interlaced PNG file will
        be written.  Supply the rows in the normal image order;
        the interlacing is carried out internally.
        .. note ::
          Interlacing will require the entire image to be in working
          memory.
        """
        if self.interlace:
            fmt = 'BH'[self.bitdepth > 8]
            a = array(fmt, itertools.chain(*rows))
            return self.write_array(outfile, a)
        nrows = self.write_passes(outfile, rows)
        if nrows != self.height:
            raise ValueError(
              "rows supplied (%d) does not match height (%d)" %
              (nrows, self.height))
    def write_passes(self, outfile, rows, packed=False):
        """
        Write a PNG image to the output file.
        Most users are expected to find the :meth:`write` or
        :meth:`write_array` method more convenient.
        
        The rows should be given to this method in the order that
        they appear in the output file.  For straightlaced images,
        this is the usual top to bottom ordering, but for interlaced
        images the rows should have already been interlaced before
        passing them to this function.
        `rows` should be an iterable that yields each row.  When
        `packed` is ``False`` the rows should be in boxed row flat pixel
        format; when `packed` is ``True`` each row should be a packed
        sequence of bytes.
        """
        # http://www.w3.org/TR/PNG/#5PNG-file-signature
        outfile.write(_signature)
        # http://www.w3.org/TR/PNG/#11IHDR
        write_chunk(outfile, b'IHDR',
                    struct.pack("!2I5B", self.width, self.height,
                                self.bitdepth, self.color_type,
                                0, 0, self.interlace))
        # See :chunk:order
        # http://www.w3.org/TR/PNG/#11gAMA
        if self.gamma is not None:
            write_chunk(outfile, b'gAMA',
                        struct.pack("!L", int(round(self.gamma*1e5))))
        # See :chunk:order
        # http://www.w3.org/TR/PNG/#11sBIT
        if self.rescale:
            write_chunk(outfile, b'sBIT',
                struct.pack('%dB' % self.planes,
                            *[self.rescale[0]]*self.planes))
        
        # :chunk:order: Without a palette (PLTE chunk), ordering is
        # relatively relaxed.  With one, gAMA chunk must precede PLTE
        # chunk which must precede tRNS and bKGD.
        # See http://www.w3.org/TR/PNG/#5ChunkOrdering
        if self.palette:
            p,t = self.make_palette()
            write_chunk(outfile, b'PLTE', p)
            if t:
                # tRNS chunk is optional. Only needed if palette entries
                # have alpha.
                write_chunk(outfile, b'tRNS', t)
        # http://www.w3.org/TR/PNG/#11tRNS
        if self.transparent is not None:
            if self.greyscale:
                write_chunk(outfile, b'tRNS',
                            struct.pack("!1H", *self.transparent))
            else:
                write_chunk(outfile, b'tRNS',
                            struct.pack("!3H", *self.transparent))
        # http://www.w3.org/TR/PNG/#11bKGD
        if self.background is not None:
            if self.greyscale:
                write_chunk(outfile, b'bKGD',
                            struct.pack("!1H", *self.background))
            else:
                write_chunk(outfile, b'bKGD',
                            struct.pack("!3H", *self.background))
        # http://www.w3.org/TR/PNG/#11pHYs
        if self.x_pixels_per_unit is not None and self.y_pixels_per_unit is not None:
            tup = (self.x_pixels_per_unit, self.y_pixels_per_unit, int(self.unit_is_meter))
            write_chunk(outfile, b'pHYs', struct.pack("!LLB",*tup))
        # http://www.w3.org/TR/PNG/#11IDAT
        if self.compression is not None:
            compressor = zlib.compressobj(self.compression)
        else:
            compressor = zlib.compressobj()
        # Choose an extend function based on the bitdepth.  The extend
        # function packs/decomposes the pixel values into bytes and
        # stuffs them onto the data array.
        data = array('B')
        if self.bitdepth == 8 or packed:
            extend = data.extend
        elif self.bitdepth == 16:
            # Decompose into bytes
            def extend(sl):
                fmt = '!%dH' % len(sl)
                data.extend(array('B', struct.pack(fmt, *sl)))
        else:
            # Pack into bytes
            assert self.bitdepth < 8
            # samples per byte
            spb = int(8/self.bitdepth)
            def extend(sl):
                a = array('B', sl)
                # Adding padding bytes so we can group into a whole
                # number of spb-tuples.
                l = float(len(a))
                extra = math.ceil(l / float(spb))*spb - l
                a.extend([0]*int(extra))
                # Pack into bytes
                l = group(a, spb)
                l = [reduce(lambda x,y:
                                           (x << self.bitdepth) + y, e) for e in l]
                data.extend(l)
        if self.rescale:
            oldextend = extend
            factor = \
              float(2**self.rescale[1]-1) / float(2**self.rescale[0]-1)
            def extend(sl):
                oldextend([int(round(factor*x)) for x in sl])
        # Build the first row, testing mostly to see if we need to
        # changed the extend function to cope with NumPy integer types
        # (they cause our ordinary definition of extend to fail, so we
        # wrap it).  See
        # http://code.google.com/p/pypng/issues/detail?id=44
        enumrows = enumerate(rows)
        del rows
        # First row's filter type.
        data.append(0)
        # :todo: Certain exceptions in the call to ``.next()`` or the
        # following try would indicate no row data supplied.
        # Should catch.
        i,row = next(enumrows)
        try:
            # If this fails...
            extend(row)
        except:
            # ... try a version that converts the values to int first.
            # Not only does this work for the (slightly broken) NumPy
            # types, there are probably lots of other, unknown, "nearly"
            # int types it works for.
            def wrapmapint(f):
                return lambda sl: f([int(x) for x in sl])
            extend = wrapmapint(extend)
            del wrapmapint
            extend(row)
        for i,row in enumrows:
            # Add "None" filter type.  Currently, it's essential that
            # this filter type be used for every scanline as we do not
            # mark the first row of a reduced pass image; that means we
            # could accidentally compute the wrong filtered scanline if
            # we used "up", "average", or "paeth" on such a line.
            data.append(0)
            extend(row)
            if len(data) > self.chunk_limit:
                compressed = compressor.compress(tostring(data))
                if len(compressed):
                    write_chunk(outfile, b'IDAT', compressed)
                # Because of our very witty definition of ``extend``,
                # above, we must re-use the same ``data`` object.  Hence
                # we use ``del`` to empty this one, rather than create a
                # fresh one (which would be my natural FP instinct).
                del data[:]
        if len(data):
            compressed = compressor.compress(tostring(data))
        else:
            compressed = b''
        flushed = compressor.flush()
        if len(compressed) or len(flushed):
            write_chunk(outfile, b'IDAT', compressed + flushed)
        # http://www.w3.org/TR/PNG/#11IEND
        write_chunk(outfile, b'IEND')
        return i+1
    def write_array(self, outfile, pixels):
        """
        Write an array in flat row flat pixel format as a PNG file on
        the output file.  See also :meth:`write` method.
        """
        if self.interlace:
            self.write_passes(outfile, self.array_scanlines_interlace(pixels))
        else:
            self.write_passes(outfile, self.array_scanlines(pixels))
    def write_packed(self, outfile, rows):
        """
        Write PNG file to `outfile`.  The pixel data comes from `rows`
        which should be in boxed row packed format.  Each row should be
        a sequence of packed bytes.
        Technically, this method does work for interlaced images but it
        is best avoided.  For interlaced images, the rows should be
        presented in the order that they appear in the file.
        This method should not be used when the source image bit depth
        is not one naturally supported by PNG; the bit depth should be
        1, 2, 4, 8, or 16.
        """
        if self.rescale:
            raise Error("write_packed method not suitable for bit depth %d" %
              self.rescale[0])
        return self.write_passes(outfile, rows, packed=True)
    def convert_pnm(self, infile, outfile):
        """
        Convert a PNM file containing raw pixel data into a PNG file
        with the parameters set in the writer object.  Works for
        (binary) PGM, PPM, and PAM formats.
        """
        if self.interlace:
            pixels = array('B')
            pixels.fromfile(infile,
                            (self.bitdepth/8) * self.color_planes *
                            self.width * self.height)
            self.write_passes(outfile, self.array_scanlines_interlace(pixels))
        else:
            self.write_passes(outfile, self.file_scanlines(infile))
    def convert_ppm_and_pgm(self, ppmfile, pgmfile, outfile):
        """
        Convert a PPM and PGM file containing raw pixel data into a
        PNG outfile with the parameters set in the writer object.
        """
        pixels = array('B')
        pixels.fromfile(ppmfile,
                        (self.bitdepth/8) * self.color_planes *
                        self.width * self.height)
        apixels = array('B')
        apixels.fromfile(pgmfile,
                         (self.bitdepth/8) *
                         self.width * self.height)
        pixels = interleave_planes(pixels, apixels,
                                   (self.bitdepth/8) * self.color_planes,
                                   (self.bitdepth/8))
        if self.interlace:
            self.write_passes(outfile, self.array_scanlines_interlace(pixels))
        else:
            self.write_passes(outfile, self.array_scanlines(pixels))
    def file_scanlines(self, infile):
        """
        Generates boxed rows in flat pixel format, from the input file
        `infile`.  It assumes that the input file is in a "Netpbm-like"
        binary format, and is positioned at the beginning of the first
        pixel.  The number of pixels to read is taken from the image
        dimensions (`width`, `height`, `planes`) and the number of bytes
        per value is implied by the image `bitdepth`.
        """
        # Values per row
        vpr = self.width * self.planes
        row_bytes = vpr
        if self.bitdepth > 8:
            assert self.bitdepth == 16
            row_bytes *= 2
            fmt = '>%dH' % vpr
            def line():
                return array('H', struct.unpack(fmt, infile.read(row_bytes)))
        else:
            def line():
                scanline = array('B', infile.read(row_bytes))
                return scanline
        for y in range(self.height):
            yield line()
    def array_scanlines(self, pixels):
        """
        Generates boxed rows (flat pixels) from flat rows (flat pixels)
        in an array.
        """
        # Values per row
        vpr = self.width * self.planes
        stop = 0
        for y in range(self.height):
            start = stop
            stop = start + vpr
            yield pixels[start:stop]
    def array_scanlines_interlace(self, pixels):
        """
        Generator for interlaced scanlines from an array.  `pixels` is
        the full source image in flat row flat pixel format.  The
        generator yields each scanline of the reduced passes in turn, in
        boxed row flat pixel format.
        """
        # http://www.w3.org/TR/PNG/#8InterlaceMethods
        # Array type.
        fmt = 'BH'[self.bitdepth > 8]
        # Value per row
        vpr = self.width * self.planes
        for xstart, ystart, xstep, ystep in _adam7:
            if xstart >= self.width:
                continue
            # Pixels per row (of reduced image)
            ppr = int(math.ceil((self.width-xstart)/float(xstep)))
            # number of values in reduced image row.
            row_len = ppr*self.planes
            for y in range(ystart, self.height, ystep):
                if xstep == 1:
                    offset = y * vpr
                    yield pixels[offset:offset+vpr]
                else:
                    row = array(fmt)
                    # There's no easier way to set the length of an array
                    row.extend(pixels[0:row_len])
                    offset = y * vpr + xstart * self.planes
                    end_offset = (y+1) * vpr
                    skip = self.planes * xstep
                    for i in range(self.planes):
                        row[i::self.planes] = \
                            pixels[offset+i:end_offset:skip]
                    yield row
def write_chunk(outfile, tag, data=b''):
    """
    Write a PNG chunk to the output file, including length and
    checksum.
    """
    # http://www.w3.org/TR/PNG/#5Chunk-layout
    outfile.write(struct.pack("!I", len(data)))
    outfile.write(tag)
    outfile.write(data)
    checksum = zlib.crc32(tag)
    checksum = zlib.crc32(data, checksum)
    checksum &= 2**32-1
    outfile.write(struct.pack("!I", checksum))
def write_chunks(out, chunks):
    """Create a PNG file by writing out the chunks."""
    out.write(_signature)
    for chunk in chunks:
        write_chunk(out, *chunk)
def filter_scanline(type, line, fo, prev=None):
    """Apply a scanline filter to a scanline.  `type` specifies the
    filter type (0 to 4); `line` specifies the current (unfiltered)
    scanline as a sequence of bytes; `prev` specifies the previous
    (unfiltered) scanline as a sequence of bytes. `fo` specifies the
    filter offset; normally this is size of a pixel in bytes (the number
    of bytes per sample times the number of channels), but when this is
    < 1 (for bit depths < 8) then the filter offset is 1.
    """
    assert 0 <= type < 5
    # The output array.  Which, pathetically, we extend one-byte at a
    # time (fortunately this is linear).
    out = array('B', [type])
    def sub():
        ai = -fo
        for x in line:
            if ai >= 0:
                x = (x - line[ai]) & 0xff
            out.append(x)
            ai += 1
    def up():
        for i,x in enumerate(line):
            x = (x - prev[i]) & 0xff
            out.append(x)
    def average():
        ai = -fo
        for i,x in enumerate(line):
            if ai >= 0:
                x = (x - ((line[ai] + prev[i]) >> 1)) & 0xff
            else:
                x = (x - (prev[i] >> 1)) & 0xff
            out.append(x)
            ai += 1
    def paeth():
        # http://www.w3.org/TR/PNG/#9Filter-type-4-Paeth
        ai = -fo # also used for ci
        for i,x in enumerate(line):
            a = 0
            b = prev[i]
            c = 0
            if ai >= 0:
                a = line[ai]
                c = prev[ai]
            p = a + b - c
            pa = abs(p - a)
            pb = abs(p - b)
            pc = abs(p - c)
            if pa <= pb and pa <= pc:
                Pr = a
            elif pb <= pc:
                Pr = b
            else:
                Pr = c
            x = (x - Pr) & 0xff
            out.append(x)
            ai += 1
    if not prev:
        # We're on the first line.  Some of the filters can be reduced
        # to simpler cases which makes handling the line "off the top"
        # of the image simpler.  "up" becomes "none"; "paeth" becomes
        # "left" (non-trivial, but true). "average" needs to be handled
        # specially.
        if type == 2: # "up"
            type = 0
        elif type == 3:
            prev = [0]*len(line)
        elif type == 4: # "paeth"
            type = 1
    if type == 0:
        out.extend(line)
    elif type == 1:
        sub()
    elif type == 2:
        up()
    elif type == 3:
        average()
    else: # type == 4
        paeth()
    return out
# Regex for decoding mode string
RegexModeDecode = re.compile("(LA?|RGBA?);?([0-9]*)", flags=re.IGNORECASE)
def from_array(a, mode=None, info={}):
    """Create a PNG :class:`Image` object from a 2- or 3-dimensional
    array.  One application of this function is easy PIL-style saving:
    ``png.from_array(pixels, 'L').save('foo.png')``.
    Unless they are specified using the *info* parameter, the PNG's
    height and width are taken from the array size.  For a 3 dimensional
    array the first axis is the height; the second axis is the width;
    and the third axis is the channel number.  Thus an RGB image that is
    16 pixels high and 8 wide will use an array that is 16x8x3.  For 2
    dimensional arrays the first axis is the height, but the second axis
    is ``width*channels``, so an RGB image that is 16 pixels high and 8
    wide will use a 2-dimensional array that is 16x24 (each row will be
    8*3 = 24 sample values).
    *mode* is a string that specifies the image colour format in a
    PIL-style mode.  It can be:
    ``'L'``
      greyscale (1 channel)
    ``'LA'``
      greyscale with alpha (2 channel)
    ``'RGB'``
      colour image (3 channel)
    ``'RGBA'``
      colour image with alpha (4 channel)
    The mode string can also specify the bit depth (overriding how this
    function normally derives the bit depth, see below).  Appending
    ``';16'`` to the mode will cause the PNG to be 16 bits per channel;
    any decimal from 1 to 16 can be used to specify the bit depth.
    When a 2-dimensional array is used *mode* determines how many
    channels the image has, and so allows the width to be derived from
    the second array dimension.
    The array is expected to be a ``numpy`` array, but it can be any
    suitable Python sequence.  For example, a list of lists can be used:
    ``png.from_array([[0, 255, 0], [255, 0, 255]], 'L')``.  The exact
    rules are: ``len(a)`` gives the first dimension, height;
    ``len(a[0])`` gives the second dimension; ``len(a[0][0])`` gives the
    third dimension, unless an exception is raised in which case a
    2-dimensional array is assumed.  It's slightly more complicated than
    that because an iterator of rows can be used, and it all still
    works.  Using an iterator allows data to be streamed efficiently.
    The bit depth of the PNG is normally taken from the array element's
    datatype (but if *mode* specifies a bitdepth then that is used
    instead).  The array element's datatype is determined in a way which
    is supposed to work both for ``numpy`` arrays and for Python
    ``array.array`` objects.  A 1 byte datatype will give a bit depth of
    8, a 2 byte datatype will give a bit depth of 16.  If the datatype
    does not have an implicit size, for example it is a plain Python
    list of lists, as above, then a default of 8 is used.
    The *info* parameter is a dictionary that can be used to specify
    metadata (in the same style as the arguments to the
    :class:`png.Writer` class).  For this function the keys that are
    useful are:
    
    height
      overrides the height derived from the array dimensions and allows
      *a* to be an iterable.
    width
      overrides the width derived from the array dimensions.
    bitdepth
      overrides the bit depth derived from the element datatype (but
      must match *mode* if that also specifies a bit depth).
    Generally anything specified in the
    *info* dictionary will override any implicit choices that this
    function would otherwise make, but must match any explicit ones.
    For example, if the *info* dictionary has a ``greyscale`` key then
    this must be true when mode is ``'L'`` or ``'LA'`` and false when
    mode is ``'RGB'`` or ``'RGBA'``.
    """
    # We abuse the *info* parameter by modifying it.  Take a copy here.
    # (Also typechecks *info* to some extent).
    info = dict(info)
    # Syntax check mode string.
    match = RegexModeDecode.match(mode)
    if not match:
        raise Error("mode string should be 'RGB' or 'L;16' or similar.")
    mode, bitdepth = match.groups()
    alpha = 'A' in mode
    if bitdepth:
        bitdepth = int(bitdepth)
    # Colour format.
    if 'greyscale' in info:
        if bool(info['greyscale']) != ('L' in mode):
            raise Error("info['greyscale'] should match mode.")
    info['greyscale'] = 'L' in mode
    if 'alpha' in info:
        if bool(info['alpha']) != alpha:
            raise Error("info['alpha'] should match mode.")
    info['alpha'] = alpha
    # Get bitdepth from *mode* if possible.
    if bitdepth:
        if info.get("bitdepth") and bitdepth != info['bitdepth']:
            raise Error("bitdepth (%d) should match bitdepth of info (%d)." %
              (bitdepth, info['bitdepth']))
        info['bitdepth'] = bitdepth
    # Fill in and/or check entries in *info*.
    # Dimensions.
    if 'size' in info:
        assert len(info["size"]) == 2
        # Check width, height, size all match where used.
        for dimension,axis in [('width', 0), ('height', 1)]:
            if dimension in info:
                if info[dimension] != info['size'][axis]:
                    raise Error(
                      "info[%r] should match info['size'][%r]." %
                      (dimension, axis))
        info['width'],info['height'] = info['size']
    if 'height' not in info:
        try:
            info['height'] = len(a)
        except TypeError:
            raise Error("len(a) does not work, supply info['height'] instead.")
    planes = len(mode)
    if 'planes' in info:
        if info['planes'] != planes:
            raise Error("info['planes'] should match mode.")
    # In order to work out whether we the array is 2D or 3D we need its
    # first row, which requires that we take a copy of its iterator.
    # We may also need the first row to derive width and bitdepth.
    a,t = itertools.tee(a)
    row = next(t)
    del t
    try:
        row[0][0]
        threed = True
        testelement = row[0]
    except (IndexError, TypeError):
        threed = False
        testelement = row
    if 'width' not in info:
        if threed:
            width = len(row)
        else:
            width = len(row) // planes
        info['width'] = width
    if threed:
        # Flatten the threed rows
        a = (itertools.chain.from_iterable(x) for x in a)
    if 'bitdepth' not in info:
        try:
            dtype = testelement.dtype
            # goto the "else:" clause.  Sorry.
        except AttributeError:
            try:
                # Try a Python array.array.
                bitdepth = 8 * testelement.itemsize
            except AttributeError:
                # We can't determine it from the array element's
                # datatype, use a default of 8.
                bitdepth = 8
        else:
            # If we got here without exception, we now assume that
            # the array is a numpy array.
            if dtype.kind == 'b':
                bitdepth = 1
            else:
                bitdepth = 8 * dtype.itemsize
        info['bitdepth'] = bitdepth
    for thing in ["width", "height", "bitdepth", "greyscale", "alpha"]:
        assert thing in info
    return Image(a, info)
# So that refugee's from PIL feel more at home.  Not documented.
fromarray = from_array
class Image:
    """A PNG image.  You can create an :class:`Image` object from
    an array of pixels by calling :meth:`png.from_array`.  It can be
    saved to disk with the :meth:`save` method.
    """
    def __init__(self, rows, info):
        """
        .. note ::
        
          The constructor is not public.  Please do not call it.
        """
        
        self.rows = rows
        self.info = info
    def save(self, file):
        """Save the image to *file*.  If *file* looks like an open file
        descriptor then it is used, otherwise it is treated as a
        filename and a fresh file is opened.
        In general, you can only call this method once; after it has
        been called the first time and the PNG image has been saved, the
        source data will have been streamed, and cannot be streamed
        again.
        """
        w = Writer(**self.info)
        try:
            file.write
            def close(): pass
        except AttributeError:
            file = open(file, 'wb')
            def close(): file.close()
        try:
            w.write(file, self.rows)
        finally:
            close()
class _readable:
    """
    A simple file-like interface for strings and arrays.
    """
    def __init__(self, buf):
        self.buf = buf
        self.offset = 0
    def read(self, n):
        r = self.buf[self.offset:self.offset+n]
        if isarray(r):
            r = r.tostring()
        self.offset += n
        return r
try:
    str(b'dummy', 'ascii')
except TypeError:
    as_str = str
else:
    def as_str(x):
        return str(x, 'ascii')
class Reader:
    """
    PNG decoder in pure Python.
    """
    def __init__(self, _guess=None, **kw):
        """
        Create a PNG decoder object.
        The constructor expects exactly one keyword argument. If you
        supply a positional argument instead, it will guess the input
        type. You can choose among the following keyword arguments:
        filename
          Name of input file (a PNG file).
        file
          A file-like object (object with a read() method).
        bytes
          ``array`` or ``string`` with PNG data.
        """
        if ((_guess is not None and len(kw) != 0) or
            (_guess is None and len(kw) != 1)):
            raise TypeError("Reader() takes exactly 1 argument")
        # Will be the first 8 bytes, later on.  See validate_signature.
        self.signature = None
        self.transparent = None
        # A pair of (len,type) if a chunk has been read but its data and
        # checksum have not (in other words the file position is just
        # past the 4 bytes that specify the chunk type).  See preamble
        # method for how this is used.
        self.atchunk = None
        if _guess is not None:
            if isarray(_guess):
                kw["bytes"] = _guess
            elif isinstance(_guess, str):
                kw["filename"] = _guess
            elif hasattr(_guess, 'read'):
                kw["file"] = _guess
        if "filename" in kw:
            self.file = open(kw["filename"], "rb")
        elif "file" in kw:
            self.file = kw["file"]
        elif "bytes" in kw:
            self.file = _readable(kw["bytes"])
        else:
            raise TypeError("expecting filename, file or bytes array")
    def chunk(self, seek=None, lenient=False):
        """
        Read the next PNG chunk from the input file; returns a
        (*type*, *data*) tuple.  *type* is the chunk's type as a
        byte string (all PNG chunk types are 4 bytes long).
        *data* is the chunk's data content, as a byte string.
        If the optional `seek` argument is
        specified then it will keep reading chunks until it either runs
        out of file or finds the type specified by the argument.  Note
        that in general the order of chunks in PNGs is unspecified, so
        using `seek` can cause you to miss chunks.
        If the optional `lenient` argument evaluates to `True`,
        checksum failures will raise warnings rather than exceptions.
        """
        self.validate_signature()
        while True:
            # http://www.w3.org/TR/PNG/#5Chunk-layout
            if not self.atchunk:
                self.atchunk = self.chunklentype()
            length, type = self.atchunk
            self.atchunk = None
            data = self.file.read(length)
            if len(data) != length:
                raise ChunkError('Chunk %s too short for required %i octets.'
                  % (type, length))
            checksum = self.file.read(4)
            if len(checksum) != 4:
                raise ChunkError('Chunk %s too short for checksum.' % type)
            if seek and type != seek:
                continue
            verify = zlib.crc32(type)
            verify = zlib.crc32(data, verify)
            # Whether the output from zlib.crc32 is signed or not varies
            # according to hideous implementation details, see
            # http://bugs.python.org/issue1202 .
            # We coerce it to be positive here (in a way which works on
            # Python 2.3 and older).
            verify &= 2**32 - 1
            verify = struct.pack('!I', verify)
            if checksum != verify:
                (a, ) = struct.unpack('!I', checksum)
                (b, ) = struct.unpack('!I', verify)
                message = "Checksum error in %s chunk: 0x%08X != 0x%08X." % (type, a, b)
                if lenient:
                    warnings.warn(message, RuntimeWarning)
                else:
                    raise ChunkError(message)
            return type, data
    def chunks(self):
        """Return an iterator that will yield each chunk as a
        (*chunktype*, *content*) pair.
        """
        while True:
            t,v = self.chunk()
            yield t,v
            if t == b'IEND':
                break
    def undo_filter(self, filter_type, scanline, previous):
        """Undo the filter for a scanline.  `scanline` is a sequence of
        bytes that does not include the initial filter type byte.
        `previous` is decoded previous scanline (for straightlaced
        images this is the previous pixel row, but for interlaced
        images, it is the previous scanline in the reduced image, which
        in general is not the previous pixel row in the final image).
        When there is no previous scanline (the first row of a
        straightlaced image, or the first row in one of the passes in an
        interlaced image), then this argument should be ``None``.
        The scanline will have the effects of filtering removed, and the
        result will be returned as a fresh sequence of bytes.
        """
        # :todo: Would it be better to update scanline in place?
        # Yes, with the Cython extension making the undo_filter fast,
        # updating scanline inplace makes the code 3 times faster
        # (reading 50 images of 800x800 went from 40s to 16s)
        result = scanline
        if filter_type == 0:
            return result
        if filter_type not in (1,2,3,4):
            raise FormatError('Invalid PNG Filter Type.'
              '  See http://www.w3.org/TR/2003/REC-PNG-20031110/#9Filters .')
        # Filter unit.  The stride from one pixel to the corresponding
        # byte from the previous pixel.  Normally this is the pixel
        # size in bytes, but when this is smaller than 1, the previous
        # byte is used instead.
        fu = max(1, self.psize)
        # For the first line of a pass, synthesize a dummy previous
        # line.  An alternative approach would be to observe that on the
        # first line 'up' is the same as 'null', 'paeth' is the same
        # as 'sub', with only 'average' requiring any special case.
        if not previous:
            previous = array('B', [0]*len(scanline))
        def sub():
            """Undo sub filter."""
            ai = 0
            # Loop starts at index fu.  Observe that the initial part
            # of the result is already filled in correctly with
            # scanline.
            for i in range(fu, len(result)):
                x = scanline[i]
                a = result[ai]
                result[i] = (x + a) & 0xff
                ai += 1
        def up():
            """Undo up filter."""
            for i in range(len(result)):
                x = scanline[i]
                b = previous[i]
                result[i] = (x + b) & 0xff
        def average():
            """Undo average filter."""
            ai = -fu
            for i in range(len(result)):
                x = scanline[i]
                if ai < 0:
                    a = 0
                else:
                    a = result[ai]
                b = previous[i]
                result[i] = (x + ((a + b) >> 1)) & 0xff
                ai += 1
        def paeth():
            """Undo Paeth filter."""
            # Also used for ci.
            ai = -fu
            for i in range(len(result)):
                x = scanline[i]
                if ai < 0:
                    a = c = 0
                else:
                    a = result[ai]
                    c = previous[ai]
                b = previous[i]
                p = a + b - c
                pa = abs(p - a)
                pb = abs(p - b)
                pc = abs(p - c)
                if pa <= pb and pa <= pc:
                    pr = a
                elif pb <= pc:
                    pr = b
                else:
                    pr = c
                result[i] = (x + pr) & 0xff
                ai += 1
        # Call appropriate filter algorithm.  Note that 0 has already
        # been dealt with.
        (None,
         pngfilters.undo_filter_sub,
         pngfilters.undo_filter_up,
         pngfilters.undo_filter_average,
         pngfilters.undo_filter_paeth)[filter_type](fu, scanline, previous, result)
        return result
    def deinterlace(self, raw):
        """
        Read raw pixel data, undo filters, deinterlace, and flatten.
        Return in flat row flat pixel format.
        """
        # Values per row (of the target image)
        vpr = self.width * self.planes
        # Make a result array, and make it big enough.  Interleaving
        # writes to the output array randomly (well, not quite), so the
        # entire output array must be in memory.
        fmt = 'BH'[self.bitdepth > 8]
        a = array(fmt, [0]*vpr*self.height)
        source_offset = 0
        for xstart, ystart, xstep, ystep in _adam7:
            if xstart >= self.width:
                continue
            # The previous (reconstructed) scanline.  None at the
            # beginning of a pass to indicate that there is no previous
            # line.
            recon = None
            # Pixels per row (reduced pass image)
            ppr = int(math.ceil((self.width-xstart)/float(xstep)))
            # Row size in bytes for this pass.
            row_size = int(math.ceil(self.psize * ppr))
            for y in range(ystart, self.height, ystep):
                filter_type = raw[source_offset]
                source_offset += 1
                scanline = raw[source_offset:source_offset+row_size]
                source_offset += row_size
                recon = self.undo_filter(filter_type, scanline, recon)
                # Convert so that there is one element per pixel value
                flat = self.serialtoflat(recon, ppr)
                if xstep == 1:
                    assert xstart == 0
                    offset = y * vpr
                    a[offset:offset+vpr] = flat
                else:
                    offset = y * vpr + xstart * self.planes
                    end_offset = (y+1) * vpr
                    skip = self.planes * xstep
                    for i in range(self.planes):
                        a[offset+i:end_offset:skip] = \
                            flat[i::self.planes]
        return a
    def iterboxed(self, rows):
        """Iterator that yields each scanline in boxed row flat pixel
        format.  `rows` should be an iterator that yields the bytes of
        each row in turn.
        """
        def asvalues(raw):
            """Convert a row of raw bytes into a flat row.  Result will
            be a freshly allocated object, not shared with
            argument.
            """
            if self.bitdepth == 8:
                return array('B', raw)
            if self.bitdepth == 16:
                raw = tostring(raw)
                return array('H', struct.unpack('!%dH' % (len(raw)//2), raw))
            assert self.bitdepth < 8
            width = self.width
            # Samples per byte
            spb = 8//self.bitdepth
            out = array('B')
            mask = 2**self.bitdepth - 1
            shifts = [self.bitdepth * i
                for i in reversed(list(range(spb)))]
            for o in raw:
                out.extend([mask&(o>>i) for i in shifts])
            return out[:width]
        return map(asvalues, rows)
    def serialtoflat(self, bytes, width=None):
        """Convert serial format (byte stream) pixel data to flat row
        flat pixel.
        """
        if self.bitdepth == 8:
            return bytes
        if self.bitdepth == 16:
            bytes = tostring(bytes)
            return array('H',
              struct.unpack('!%dH' % (len(bytes)//2), bytes))
        assert self.bitdepth < 8
        if width is None:
            width = self.width
        # Samples per byte
        spb = 8//self.bitdepth
        out = array('B')
        mask = 2**self.bitdepth - 1
        shifts = list(map(self.bitdepth.__mul__, reversed(list(range(spb)))))
        l = width
        for o in bytes:
            out.extend([(mask&(o>>s)) for s in shifts][:l])
            l -= spb
            if l <= 0:
                l = width
        return out
    def iterstraight(self, raw):
        """Iterator that undoes the effect of filtering, and yields
        each row in serialised format (as a sequence of bytes).
        Assumes input is straightlaced.  `raw` should be an iterable
        that yields the raw bytes in chunks of arbitrary size.
        """
        # length of row, in bytes
        rb = self.row_bytes
        a = array('B')
        # The previous (reconstructed) scanline.  None indicates first
        # line of image.
        recon = None
        for some in raw:
            a.extend(some)
            while len(a) >= rb + 1:
                filter_type = a[0]
                scanline = a[1:rb+1]
                del a[:rb+1]
                recon = self.undo_filter(filter_type, scanline, recon)
                yield recon
        if len(a) != 0:
            # :file:format We get here with a file format error:
            # when the available bytes (after decompressing) do not
            # pack into exact rows.
            raise FormatError(
              'Wrong size for decompressed IDAT chunk.')
        assert len(a) == 0
    def validate_signature(self):
        """If signature (header) has not been read then read and
        validate it; otherwise do nothing.
        """
        if self.signature:
            return
        self.signature = self.file.read(8)
        if self.signature != _signature:
            raise FormatError("PNG file has invalid signature.")
    def preamble(self, lenient=False):
        """
        Extract the image metadata by reading the initial part of
        the PNG file up to the start of the ``IDAT`` chunk.  All the
        chunks that precede the ``IDAT`` chunk are read and either
        processed for metadata or discarded.
        If the optional `lenient` argument evaluates to `True`, checksum
        failures will raise warnings rather than exceptions.
        """
        self.validate_signature()
        while True:
            if not self.atchunk:
                self.atchunk = self.chunklentype()
                if self.atchunk is None:
                    raise FormatError(
                      'This PNG file has no IDAT chunks.')
            if self.atchunk[1] == b'IDAT':
                return
            self.process_chunk(lenient=lenient)
    def chunklentype(self):
        """Reads just enough of the input to determine the next
        chunk's length and type, returned as a (*length*, *type*) pair
        where *type* is a string.  If there are no more chunks, ``None``
        is returned.
        """
        x = self.file.read(8)
        if not x:
            return None
        if len(x) != 8:
            raise FormatError(
              'End of file whilst reading chunk length and type.')
        length,type = struct.unpack('!I4s', x)
        if length > 2**31-1:
            raise FormatError('Chunk %s is too large: %d.' % (type,length))
        return length,type
    def process_chunk(self, lenient=False):
        """Process the next chunk and its data.  This only processes the
        following chunk types, all others are ignored: ``IHDR``,
        ``PLTE``, ``bKGD``, ``tRNS``, ``gAMA``, ``sBIT``, ``pHYs``.
        If the optional `lenient` argument evaluates to `True`,
        checksum failures will raise warnings rather than exceptions.
        """
        type, data = self.chunk(lenient=lenient)
        method = '_process_' + as_str(type)
        m = getattr(self, method, None)
        if m:
            m(data)
    def _process_IHDR(self, data):
        # http://www.w3.org/TR/PNG/#11IHDR
        if len(data) != 13:
            raise FormatError('IHDR chunk has incorrect length.')
        (self.width, self.height, self.bitdepth, self.color_type,
         self.compression, self.filter,
         self.interlace) = struct.unpack("!2I5B", data)
        check_bitdepth_colortype(self.bitdepth, self.color_type)
        if self.compression != 0:
            raise Error("unknown compression method %d" % self.compression)
        if self.filter != 0:
            raise FormatError("Unknown filter method %d,"
              " see http://www.w3.org/TR/2003/REC-PNG-20031110/#9Filters ."
              % self.filter)
        if self.interlace not in (0,1):
            raise FormatError("Unknown interlace method %d,"
              " see http://www.w3.org/TR/2003/REC-PNG-20031110/#8InterlaceMethods ."
              % self.interlace)
        # Derived values
        # http://www.w3.org/TR/PNG/#6Colour-values
        colormap =  bool(self.color_type & 1)
        greyscale = not (self.color_type & 2)
        alpha = bool(self.color_type & 4)
        color_planes = (3,1)[greyscale or colormap]
        planes = color_planes + alpha
        self.colormap = colormap
        self.greyscale = greyscale
        self.alpha = alpha
        self.color_planes = color_planes
        self.planes = planes
        self.psize = float(self.bitdepth)/float(8) * planes
        if int(self.psize) == self.psize:
            self.psize = int(self.psize)
        self.row_bytes = int(math.ceil(self.width * self.psize))
        # Stores PLTE chunk if present, and is used to check
        # chunk ordering constraints.
        self.plte = None
        # Stores tRNS chunk if present, and is used to check chunk
        # ordering constraints.
        self.trns = None
        # Stores sbit chunk if present.
        self.sbit = None
    def _process_PLTE(self, data):
        # http://www.w3.org/TR/PNG/#11PLTE
        if self.plte:
            warnings.warn("Multiple PLTE chunks present.")
        self.plte = data
        if len(data) % 3 != 0:
            raise FormatError(
              "PLTE chunk's length should be a multiple of 3.")
        if len(data) > (2**self.bitdepth)*3:
            raise FormatError("PLTE chunk is too long.")
        if len(data) == 0:
            raise FormatError("Empty PLTE is not allowed.")
    def _process_bKGD(self, data):
        try:
            if self.colormap:
                if not self.plte:
                    warnings.warn(
                      "PLTE chunk is required before bKGD chunk.")
                self.background = struct.unpack('B', data)
            else:
                self.background = struct.unpack("!%dH" % self.color_planes,
                  data)
        except struct.error:
            raise FormatError("bKGD chunk has incorrect length.")
    def _process_tRNS(self, data):
        # http://www.w3.org/TR/PNG/#11tRNS
        self.trns = data
        if self.colormap:
            if not self.plte:
                warnings.warn("PLTE chunk is required before tRNS chunk.")
            else:
                if len(data) > len(self.plte)/3:
                    # Was warning, but promoted to Error as it
                    # would otherwise cause pain later on.
                    raise FormatError("tRNS chunk is too long.")
        else:
            if self.alpha:
                raise FormatError(
                  "tRNS chunk is not valid with colour type %d." %
                  self.color_type)
            try:
                self.transparent = \
                    struct.unpack("!%dH" % self.color_planes, data)
            except struct.error:
                raise FormatError("tRNS chunk has incorrect length.")
    def _process_gAMA(self, data):
        try:
            self.gamma = struct.unpack("!L", data)[0] / 100000.0
        except struct.error:
            raise FormatError("gAMA chunk has incorrect length.")
    def _process_sBIT(self, data):
        self.sbit = data
        if (self.colormap and len(data) != 3 or
            not self.colormap and len(data) != self.planes):
            raise FormatError("sBIT chunk has incorrect length.")
    def _process_pHYs(self, data):
        # http://www.w3.org/TR/PNG/#11pHYs
        self.phys = data
        fmt = "!LLB"
        if len(data) != struct.calcsize(fmt):
            raise FormatError("pHYs chunk has incorrect length.")
        self.x_pixels_per_unit, self.y_pixels_per_unit, unit = struct.unpack(fmt,data)
        self.unit_is_meter = bool(unit)
    def read(self, lenient=False):
        """
        Read the PNG file and decode it.  Returns (`width`, `height`,
        `pixels`, `metadata`).
        May use excessive memory.
        `pixels` are returned in boxed row flat pixel format.
        If the optional `lenient` argument evaluates to True,
        checksum failures will raise warnings rather than exceptions.
        """
        def iteridat():
            """Iterator that yields all the ``IDAT`` chunks as strings."""
            while True:
                try:
                    type, data = self.chunk(lenient=lenient)
                except ValueError as e:
                    raise ChunkError(e.args[0])
                if type == b'IEND':
                    # http://www.w3.org/TR/PNG/#11IEND
                    break
                if type != b'IDAT':
                    continue
                # type == b'IDAT'
                # http://www.w3.org/TR/PNG/#11IDAT
                if self.colormap and not self.plte:
                    warnings.warn("PLTE chunk is required before IDAT chunk")
                yield data
        def iterdecomp(idat):
            """Iterator that yields decompressed strings.  `idat` should
            be an iterator that yields the ``IDAT`` chunk data.
            """
            # Currently, with no max_length parameter to decompress,
            # this routine will do one yield per IDAT chunk: Not very
            # incremental.
            d = zlib.decompressobj()
            # Each IDAT chunk is passed to the decompressor, then any
            # remaining state is decompressed out.
            for data in idat:
                # :todo: add a max_length argument here to limit output
                # size.
                yield array('B', d.decompress(data))
            yield array('B', d.flush())
        self.preamble(lenient=lenient)
        raw = iterdecomp(iteridat())
        if self.interlace:
            raw = array('B', itertools.chain(*raw))
            arraycode = 'BH'[self.bitdepth>8]
            # Like :meth:`group` but producing an array.array object for
            # each row.
            pixels = map(lambda *row: array(arraycode, row),
                       *[iter(self.deinterlace(raw))]*self.width*self.planes)
        else:
            pixels = self.iterboxed(self.iterstraight(raw))
        meta = dict()
        for attr in 'greyscale alpha planes bitdepth interlace'.split():
            meta[attr] = getattr(self, attr)
        meta['size'] = (self.width, self.height)
        for attr in 'gamma transparent background'.split():
            a = getattr(self, attr, None)
            if a is not None:
                meta[attr] = a
        if self.plte:
            meta['palette'] = self.palette()
        return self.width, self.height, pixels, meta
    def read_flat(self):
        """
        Read a PNG file and decode it into flat row flat pixel format.
        Returns (*width*, *height*, *pixels*, *metadata*).
        May use excessive memory.
        `pixels` are returned in flat row flat pixel format.
        See also the :meth:`read` method which returns pixels in the
        more stream-friendly boxed row flat pixel format.
        """
        x, y, pixel, meta = self.read()
        arraycode = 'BH'[meta['bitdepth']>8]
        pixel = array(arraycode, itertools.chain(*pixel))
        return x, y, pixel, meta
    def palette(self, alpha='natural'):
        """Returns a palette that is a sequence of 3-tuples or 4-tuples,
        synthesizing it from the ``PLTE`` and ``tRNS`` chunks.  These
        chunks should have already been processed (for example, by
        calling the :meth:`preamble` method).  All the tuples are the
        same size: 3-tuples if there is no ``tRNS`` chunk, 4-tuples when
        there is a ``tRNS`` chunk.  Assumes that the image is colour type
        3 and therefore a ``PLTE`` chunk is required.
        If the `alpha` argument is ``'force'`` then an alpha channel is
        always added, forcing the result to be a sequence of 4-tuples.
        """
        if not self.plte:
            raise FormatError(
                "Required PLTE chunk is missing in colour type 3 image.")
        plte = group(array('B', self.plte), 3)
        if self.trns or alpha == 'force':
            trns = array('B', self.trns or [])
            trns.extend([255]*(len(plte)-len(trns)))
            plte = list(map(operator.add, plte, group(trns, 1)))
        return plte
    def asDirect(self):
        """Returns the image data as a direct representation of an
        ``x * y * planes`` array.  This method is intended to remove the
        need for callers to deal with palettes and transparency
        themselves.  Images with a palette (colour type 3)
        are converted to RGB or RGBA; images with transparency (a
        ``tRNS`` chunk) are converted to LA or RGBA as appropriate.
        When returned in this format the pixel values represent the
        colour value directly without needing to refer to palettes or
        transparency information.
        Like the :meth:`read` method this method returns a 4-tuple:
        (*width*, *height*, *pixels*, *meta*)
        This method normally returns pixel values with the bit depth
        they have in the source image, but when the source PNG has an
        ``sBIT`` chunk it is inspected and can reduce the bit depth of
        the result pixels; pixel values will be reduced according to
        the bit depth specified in the ``sBIT`` chunk (PNG nerds should
        note a single result bit depth is used for all channels; the
        maximum of the ones specified in the ``sBIT`` chunk.  An RGB565
        image will be rescaled to 6-bit RGB666).
        The *meta* dictionary that is returned reflects the `direct`
        format and not the original source image.  For example, an RGB
        source image with a ``tRNS`` chunk to represent a transparent
        colour, will have ``planes=3`` and ``alpha=False`` for the
        source image, but the *meta* dictionary returned by this method
        will have ``planes=4`` and ``alpha=True`` because an alpha
        channel is synthesized and added.
        *pixels* is the pixel data in boxed row flat pixel format (just
        like the :meth:`read` method).
        All the other aspects of the image data are not changed.
        """
        self.preamble()
        # Simple case, no conversion necessary.
        if not self.colormap and not self.trns and not self.sbit:
            return self.read()
        x,y,pixels,meta = self.read()
        if self.colormap:
            meta['colormap'] = False
            meta['alpha'] = bool(self.trns)
            meta['bitdepth'] = 8
            meta['planes'] = 3 + bool(self.trns)
            plte = self.palette()
            def iterpal(pixels):
                for row in pixels:
                    row = [plte[x] for x in row]
                    yield array('B', itertools.chain(*row))
            pixels = iterpal(pixels)
        elif self.trns:
            # It would be nice if there was some reasonable way
            # of doing this without generating a whole load of
            # intermediate tuples.  But tuples does seem like the
            # easiest way, with no other way clearly much simpler or
            # much faster.  (Actually, the L to LA conversion could
            # perhaps go faster (all those 1-tuples!), but I still
            # wonder whether the code proliferation is worth it)
            it = self.transparent
            maxval = 2**meta['bitdepth']-1
            planes = meta['planes']
            meta['alpha'] = True
            meta['planes'] += 1
            typecode = 'BH'[meta['bitdepth']>8]
            def itertrns(pixels):
                for row in pixels:
                    # For each row we group it into pixels, then form a
                    # characterisation vector that says whether each
                    # pixel is opaque or not.  Then we convert
                    # True/False to 0/maxval (by multiplication),
                    # and add it as the extra channel.
                    row = group(row, planes)
                    opa = map(it.__ne__, row)
                    opa = map(maxval.__mul__, opa)
                    opa = list(zip(opa)) # convert to 1-tuples
                    yield array(typecode,
                      itertools.chain(*map(operator.add, row, opa)))
            pixels = itertrns(pixels)
        targetbitdepth = None
        if self.sbit:
            sbit = struct.unpack('%dB' % len(self.sbit), self.sbit)
            targetbitdepth = max(sbit)
            if targetbitdepth > meta['bitdepth']:
                raise Error('sBIT chunk %r exceeds bitdepth %d' %
                    (sbit,self.bitdepth))
            if min(sbit) <= 0:
                raise Error('sBIT chunk %r has a 0-entry' % sbit)
            if targetbitdepth == meta['bitdepth']:
                targetbitdepth = None
        if targetbitdepth:
            shift = meta['bitdepth'] - targetbitdepth
            meta['bitdepth'] = targetbitdepth
            def itershift(pixels):
                for row in pixels:
                    yield [p >> shift for p in row]
            pixels = itershift(pixels)
        return x,y,pixels,meta
    def asFloat(self, maxval=1.0):
        """Return image pixels as per :meth:`asDirect` method, but scale
        all pixel values to be floating point values between 0.0 and
        *maxval*.
        """
        x,y,pixels,info = self.asDirect()
        sourcemaxval = 2**info['bitdepth']-1
        del info['bitdepth']
        info['maxval'] = float(maxval)
        factor = float(maxval)/float(sourcemaxval)
        def iterfloat():
            for row in pixels:
                yield [factor * p for p in row]
        return x,y,iterfloat(),info
    def _as_rescale(self, get, targetbitdepth):
        """Helper used by :meth:`asRGB8` and :meth:`asRGBA8`."""
        width,height,pixels,meta = get()
        maxval = 2**meta['bitdepth'] - 1
        targetmaxval = 2**targetbitdepth - 1
        factor = float(targetmaxval) / float(maxval)
        meta['bitdepth'] = targetbitdepth
        def iterscale():
            for row in pixels:
                yield [int(round(x*factor)) for x in row]
        if maxval == targetmaxval:
            return width, height, pixels, meta
        else:
            return width, height, iterscale(), meta
    def asRGB8(self):
        """Return the image data as an RGB pixels with 8-bits per
        sample.  This is like the :meth:`asRGB` method except that
        this method additionally rescales the values so that they
        are all between 0 and 255 (8-bit).  In the case where the
        source image has a bit depth < 8 the transformation preserves
        all the information; where the source image has bit depth
        > 8, then rescaling to 8-bit values loses precision.  No
        dithering is performed.  Like :meth:`asRGB`, an alpha channel
        in the source image will raise an exception.
        This function returns a 4-tuple:
        (*width*, *height*, *pixels*, *metadata*).
        *width*, *height*, *metadata* are as per the
        :meth:`read` method.
        
        *pixels* is the pixel data in boxed row flat pixel format.
        """
        return self._as_rescale(self.asRGB, 8)
    def asRGBA8(self):
        """Return the image data as RGBA pixels with 8-bits per
        sample.  This method is similar to :meth:`asRGB8` and
        :meth:`asRGBA`:  The result pixels have an alpha channel, *and*
        values are rescaled to the range 0 to 255.  The alpha channel is
        synthesized if necessary (with a small speed penalty).
        """
        return self._as_rescale(self.asRGBA, 8)
    def asRGB(self):
        """Return image as RGB pixels.  RGB colour images are passed
        through unchanged; greyscales are expanded into RGB
        triplets (there is a small speed overhead for doing this).
        An alpha channel in the source image will raise an
        exception.
        The return values are as for the :meth:`read` method
        except that the *metadata* reflect the returned pixels, not the
        source image.  In particular, for this method
        ``metadata['greyscale']`` will be ``False``.
        """
        width,height,pixels,meta = self.asDirect()
        if meta['alpha']:
            raise Error("will not convert image with alpha channel to RGB")
        if not meta['greyscale']:
            return width,height,pixels,meta
        meta['greyscale'] = False
        typecode = 'BH'[meta['bitdepth'] > 8]
        def iterrgb():
            for row in pixels:
                a = array(typecode, [0]) * 3 * width
                for i in range(3):
                    a[i::3] = row
                yield a
        return width,height,iterrgb(),meta
    def asRGBA(self):
        """Return image as RGBA pixels.  Greyscales are expanded into
        RGB triplets; an alpha channel is synthesized if necessary.
        The return values are as for the :meth:`read` method
        except that the *metadata* reflect the returned pixels, not the
        source image.  In particular, for this method
        ``metadata['greyscale']`` will be ``False``, and
        ``metadata['alpha']`` will be ``True``.
        """
        width,height,pixels,meta = self.asDirect()
        if meta['alpha'] and not meta['greyscale']:
            return width,height,pixels,meta
        typecode = 'BH'[meta['bitdepth'] > 8]
        maxval = 2**meta['bitdepth'] - 1
        maxbuffer = struct.pack('=' + typecode, maxval) * 4 * width
        def newarray():
            return array(typecode, maxbuffer)
        if meta['alpha'] and meta['greyscale']:
            # LA to RGBA
            def convert():
                for row in pixels:
                    # Create a fresh target row, then copy L channel
                    # into first three target channels, and A channel
                    # into fourth channel.
                    a = newarray()
                    pngfilters.convert_la_to_rgba(row, a)
                    yield a
        elif meta['greyscale']:
            # L to RGBA
            def convert():
                for row in pixels:
                    a = newarray()
                    pngfilters.convert_l_to_rgba(row, a)
                    yield a
        else:
            assert not meta['alpha'] and not meta['greyscale']
            # RGB to RGBA
            def convert():
                for row in pixels:
                    a = newarray()
                    pngfilters.convert_rgb_to_rgba(row, a)
                    yield a
        meta['alpha'] = True
        meta['greyscale'] = False
        return width,height,convert(),meta
def check_bitdepth_colortype(bitdepth, colortype):
    """Check that `bitdepth` and `colortype` are both valid,
    and specified in a valid combination. Returns if valid,
    raise an Exception if not valid.
    """
    if bitdepth not in (1,2,4,8,16):
        raise FormatError("invalid bit depth %d" % bitdepth)
    if colortype not in (0,2,3,4,6):
        raise FormatError("invalid colour type %d" % colortype)
    # Check indexed (palettized) images have 8 or fewer bits
    # per pixel; check only indexed or greyscale images have
    # fewer than 8 bits per pixel.
    if colortype & 1 and bitdepth > 8:
        raise FormatError(
          "Indexed images (colour type %d) cannot"
          " have bitdepth > 8 (bit depth %d)."
          " See http://www.w3.org/TR/2003/REC-PNG-20031110/#table111 ."
          % (bitdepth, colortype))
    if bitdepth < 8 and colortype not in (0,3):
        raise FormatError("Illegal combination of bit depth (%d)"
          " and colour type (%d)."
          " See http://www.w3.org/TR/2003/REC-PNG-20031110/#table111 ."
          % (bitdepth, colortype))
def isinteger(x):
    try:
        return int(x) == x
    except (TypeError, ValueError):
        return False
# === Support for users without Cython ===
try:
    pngfilters
except NameError:
    class pngfilters(object):
        def undo_filter_sub(filter_unit, scanline, previous, result):
            """Undo sub filter."""
            ai = 0
            # Loops starts at index fu.  Observe that the initial part
            # of the result is already filled in correctly with
            # scanline.
            for i in range(filter_unit, len(result)):
                x = scanline[i]
                a = result[ai]
                result[i] = (x + a) & 0xff
                ai += 1
        undo_filter_sub = staticmethod(undo_filter_sub)
        def undo_filter_up(filter_unit, scanline, previous, result):
            """Undo up filter."""
            for i in range(len(result)):
                x = scanline[i]
                b = previous[i]
                result[i] = (x + b) & 0xff
        undo_filter_up = staticmethod(undo_filter_up)
        def undo_filter_average(filter_unit, scanline, previous, result):
            """Undo up filter."""
            ai = -filter_unit
            for i in range(len(result)):
                x = scanline[i]
                if ai < 0:
                    a = 0
                else:
                    a = result[ai]
                b = previous[i]
                result[i] = (x + ((a + b) >> 1)) & 0xff
                ai += 1
        undo_filter_average = staticmethod(undo_filter_average)
        def undo_filter_paeth(filter_unit, scanline, previous, result):
            """Undo Paeth filter."""
            # Also used for ci.
            ai = -filter_unit
            for i in range(len(result)):
                x = scanline[i]
                if ai < 0:
                    a = c = 0
                else:
                    a = result[ai]
                    c = previous[ai]
                b = previous[i]
                p = a + b - c
                pa = abs(p - a)
                pb = abs(p - b)
                pc = abs(p - c)
                if pa <= pb and pa <= pc:
                    pr = a
                elif pb <= pc:
                    pr = b
                else:
                    pr = c
                result[i] = (x + pr) & 0xff
                ai += 1
        undo_filter_paeth = staticmethod(undo_filter_paeth)
        def convert_la_to_rgba(row, result):
            for i in range(3):
                result[i::4] = row[0::2]
            result[3::4] = row[1::2]
        convert_la_to_rgba = staticmethod(convert_la_to_rgba)
        def convert_l_to_rgba(row, result):
            """Convert a grayscale image to RGBA. This method assumes
            the alpha channel in result is already correctly
            initialized.
            """
            for i in range(3):
                result[i::4] = row
        convert_l_to_rgba = staticmethod(convert_l_to_rgba)
        def convert_rgb_to_rgba(row, result):
            """Convert an RGB image to RGBA. This method assumes the
            alpha channel in result is already correctly initialized.
            """
            for i in range(3):
                result[i::4] = row[i::3]
        convert_rgb_to_rgba = staticmethod(convert_rgb_to_rgba)
# === Command Line Support ===
def read_pam_header(infile):
    """
    Read (the rest of a) PAM header.  `infile` should be positioned
    immediately after the initial 'P7' line (at the beginning of the
    second line).  Returns are as for `read_pnm_header`.
    """
    
    # Unlike PBM, PGM, and PPM, we can read the header a line at a time.
    header = dict()
    while True:
        l = infile.readline().strip()
        if l == b'ENDHDR':
            break
        if not l:
            raise EOFError('PAM ended prematurely')
        if l[0] == b'#':
            continue
        l = l.split(None, 1)
        if l[0] not in header:
            header[l[0]] = l[1]
        else:
            header[l[0]] += b' ' + l[1]
    required = [b'WIDTH', b'HEIGHT', b'DEPTH', b'MAXVAL']
    WIDTH,HEIGHT,DEPTH,MAXVAL = required
    present = [x for x in required if x in header]
    if len(present) != len(required):
        raise Error('PAM file must specify WIDTH, HEIGHT, DEPTH, and MAXVAL')
    width = int(header[WIDTH])
    height = int(header[HEIGHT])
    depth = int(header[DEPTH])
    maxval = int(header[MAXVAL])
    if (width <= 0 or
        height <= 0 or
        depth <= 0 or
        maxval <= 0):
        raise Error(
          'WIDTH, HEIGHT, DEPTH, MAXVAL must all be positive integers')
    return 'P7', width, height, depth, maxval
def read_pnm_header(infile, supported=(b'P5', b'P6')):
    """
    Read a PNM header, returning (format,width,height,depth,maxval).
    `width` and `height` are in pixels.  `depth` is the number of
    channels in the image; for PBM and PGM it is synthesized as 1, for
    PPM as 3; for PAM images it is read from the header.  `maxval` is
    synthesized (as 1) for PBM images.
    """
    # Generally, see http://netpbm.sourceforge.net/doc/ppm.html
    # and http://netpbm.sourceforge.net/doc/pam.html
    # Technically 'P7' must be followed by a newline, so by using
    # rstrip() we are being liberal in what we accept.  I think this
    # is acceptable.
    type = infile.read(3).rstrip()
    if type not in supported:
        raise NotImplementedError('file format %s not supported' % type)
    if type == b'P7':
        # PAM header parsing is completely different.
        return read_pam_header(infile)
    # Expected number of tokens in header (3 for P4, 4 for P6)
    expected = 4
    pbm = (b'P1', b'P4')
    if type in pbm:
        expected = 3
    header = [type]
    # We have to read the rest of the header byte by byte because the
    # final whitespace character (immediately following the MAXVAL in
    # the case of P6) may not be a newline.  Of course all PNM files in
    # the wild use a newline at this point, so it's tempting to use
    # readline; but it would be wrong.
    def getc():
        c = infile.read(1)
        if not c:
            raise Error('premature EOF reading PNM header')
        return c
    c = getc()
    while True:
        # Skip whitespace that precedes a token.
        while c.isspace():
            c = getc()
        # Skip comments.
        while c == '#':
            while c not in b'\n\r':
                c = getc()
        if not c.isdigit():
            raise Error('unexpected character %s found in header' % c)
        # According to the specification it is legal to have comments
        # that appear in the middle of a token.
        # This is bonkers; I've never seen it; and it's a bit awkward to
        # code good lexers in Python (no goto).  So we break on such
        # cases.
        token = b''
        while c.isdigit():
            token += c
            c = getc()
        # Slight hack.  All "tokens" are decimal integers, so convert
        # them here.
        header.append(int(token))
        if len(header) == expected:
            break
    # Skip comments (again)
    while c == '#':
        while c not in '\n\r':
            c = getc()
    if not c.isspace():
        raise Error('expected header to end with whitespace, not %s' % c)
    if type in pbm:
        # synthesize a MAXVAL
        header.append(1)
    depth = (1,3)[type == b'P6']
    return header[0], header[1], header[2], depth, header[3]
def write_pnm(file, width, height, pixels, meta):
    """Write a Netpbm PNM/PAM file.
    """
    bitdepth = meta['bitdepth']
    maxval = 2**bitdepth - 1
    # Rudely, the number of image planes can be used to determine
    # whether we are L (PGM), LA (PAM), RGB (PPM), or RGBA (PAM).
    planes = meta['planes']
    # Can be an assert as long as we assume that pixels and meta came
    # from a PNG file.
    assert planes in (1,2,3,4)
    if planes in (1,3):
        if 1 == planes:
            # PGM
            # Could generate PBM if maxval is 1, but we don't (for one
            # thing, we'd have to convert the data, not just blat it
            # out).
            fmt = 'P5'
        else:
            # PPM
            fmt = 'P6'
        header = '%s %d %d %d\n' % (fmt, width, height, maxval)
    if planes in (2,4):
        # PAM
        # See http://netpbm.sourceforge.net/doc/pam.html
        if 2 == planes:
            tupltype = 'GRAYSCALE_ALPHA'
        else:
            tupltype = 'RGB_ALPHA'
        header = ('P7\nWIDTH %d\nHEIGHT %d\nDEPTH %d\nMAXVAL %d\n'
                  'TUPLTYPE %s\nENDHDR\n' %
                  (width, height, planes, maxval, tupltype))
    file.write(header.encode('ascii'))
    # Values per row
    vpr = planes * width
    # struct format
    fmt = '>%d' % vpr
    if maxval > 0xff:
        fmt = fmt + 'H'
    else:
        fmt = fmt + 'B'
    for row in pixels:
        file.write(struct.pack(fmt, *row))
    file.flush()
def color_triple(color):
    """
    Convert a command line colour value to a RGB triple of integers.
    FIXME: Somewhere we need support for greyscale backgrounds etc.
    """
    if color.startswith('#') and len(color) == 4:
        return (int(color[1], 16),
                int(color[2], 16),
                int(color[3], 16))
    if color.startswith('#') and len(color) == 7:
        return (int(color[1:3], 16),
                int(color[3:5], 16),
                int(color[5:7], 16))
    elif color.startswith('#') and len(color) == 13:
        return (int(color[1:5], 16),
                int(color[5:9], 16),
                int(color[9:13], 16))
def _add_common_options(parser):
    """Call *parser.add_option* for each of the options that are
    common between this PNG--PNM conversion tool and the gen
    tool.
    """
    parser.add_option("-i", "--interlace",
                      default=False, action="store_true",
                      help="create an interlaced PNG file (Adam7)")
    parser.add_option("-t", "--transparent",
                      action="store", type="string", metavar="#RRGGBB",
                      help="mark the specified colour as transparent")
    parser.add_option("-b", "--background",
                      action="store", type="string", metavar="#RRGGBB",
                      help="save the specified background colour")
    parser.add_option("-g", "--gamma",
                      action="store", type="float", metavar="value",
                      help="save the specified gamma value")
    parser.add_option("-c", "--compression",
                      action="store", type="int", metavar="level",
                      help="zlib compression level (0-9)")
    return parser
def _main(argv):
    """
    Run the PNG encoder with options from the command line.
    """
    # Parse command line arguments
    from optparse import OptionParser
    version = '%prog ' + __version__
    parser = OptionParser(version=version)
    parser.set_usage("%prog [options] [imagefile]")
    parser.add_option('-r', '--read-png', default=False,
                      action='store_true',
                      help='Read PNG, write PNM')
    parser.add_option("-a", "--alpha",
                      action="store", type="string", metavar="pgmfile",
                      help="alpha channel transparency (RGBA)")
    _add_common_options(parser)
    (options, args) = parser.parse_args(args=argv[1:])
    # Convert options
    if options.transparent is not None:
        options.transparent = color_triple(options.transparent)
    if options.background is not None:
        options.background = color_triple(options.background)
    # Prepare input and output files
    if len(args) == 0:
        infilename = '-'
        infile = sys.stdin
    elif len(args) == 1:
        infilename = args[0]
        infile = open(infilename, 'rb')
    else:
        parser.error("more than one input file")
    outfile = sys.stdout
    if sys.platform == "win32":
        import msvcrt, os
        msvcrt.setmode(sys.stdout.fileno(), os.O_BINARY)
    if options.read_png:
        # Encode PNG to PPM
        png = Reader(file=infile)
        width,height,pixels,meta = png.asDirect()
        write_pnm(outfile, width, height, pixels, meta) 
    else:
        # Encode PNM to PNG
        format, width, height, depth, maxval = \
          read_pnm_header(infile, (b'P5',b'P6',b'P7'))
        # When it comes to the variety of input formats, we do something
        # rather rude.  Observe that L, LA, RGB, RGBA are the 4 colour
        # types supported by PNG and that they correspond to 1, 2, 3, 4
        # channels respectively.  So we use the number of channels in
        # the source image to determine which one we have.  We do not
        # care about TUPLTYPE.
        greyscale = depth <= 2
        pamalpha = depth in (2,4)
        supported = [2**x-1 for x in range(1,17)]
        try:
            mi = supported.index(maxval)
        except ValueError:
            raise NotImplementedError(
              'your maxval (%s) not in supported list %s' %
              (maxval, str(supported)))
        bitdepth = mi+1
        writer = Writer(width, height,
                        greyscale=greyscale,
                        bitdepth=bitdepth,
                        interlace=options.interlace,
                        transparent=options.transparent,
                        background=options.background,
                        alpha=bool(pamalpha or options.alpha),
                        gamma=options.gamma,
                        compression=options.compression)
        if options.alpha:
            pgmfile = open(options.alpha, 'rb')
            format, awidth, aheight, adepth, amaxval = \
              read_pnm_header(pgmfile, 'P5')
            if amaxval != '255':
                raise NotImplementedError(
                  'maxval %s not supported for alpha channel' % amaxval)
            if (awidth, aheight) != (width, height):
                raise ValueError("alpha channel image size mismatch"
                                 " (%s has %sx%s but %s has %sx%s)"
                                 % (infilename, width, height,
                                    options.alpha, awidth, aheight))
            writer.convert_ppm_and_pgm(infile, pgmfile, outfile)
        else:
            writer.convert_pnm(infile, outfile)
if __name__ == '__main__':
    try:
        _main(sys.argv)
    except Error as e:
        print(e, file=sys.stderr)
#!/usr/bin/env python2.7
import sys
import os
import subprocess
import GoogleImg
urls = []
with open('search1.txt','r') as f:
	for line in f.readlines():
		url = os.popen(line).read()
		urls.append(url)
with open('url1.txt','wb') as f:
	for url in urls:
		f.write(url+'\n')
#!/usr/bin/env python2.7
import sys
import os
import GoogleImg
urls = []
with open('search2.txt','r') as f:
	for line in f.readlines():
		url = os.popen(line).read()
		urls.append(url)
with open('url2.txt','wb') as f:
	for url in urls:
		f.write(url+'\n')
#!/usr/bin/env python2.7
import sys
import os
import GoogleImg
urls = []
with open('search3.txt','r') as f:
	for line in f.readlines():
		url = os.popen(line).read()
		urls.append(url)
with open('url3.txt','wb') as f:
	for url in urls:
		f.write(url+'\n')
#!/usr/bin/env python2.7
import sys
import os
import GoogleImg
urls = []
with open('search4.txt','r') as f:
	for line in f.readlines():
		url = os.popen(line).read()
		urls.append(url)
with open('url4.txt','wb') as f:
	for url in urls:
		f.write(url+'\n')
#!/usr/bin/env python2.7
import sys
import os
import GoogleImg
urls = []
with open('search5.txt','r') as f:
	for line in f.readlines():
		url = os.popen(line).read()
		urls.append(url)
with open('url5.txt','wb') as f:
	for url in urls:
		f.write(url+'\n')
#!/usr/bin/env python2.7
import sys
import os
import GoogleImg
urls = []
with open('search6.txt','r') as f:
	for line in f.readlines():
		url = os.popen(line).read()
		urls.append(url)
with open('url6.txt','wb') as f:
	for url in urls:
		f.write(url+'\n')
#!/usr/bin/env python2.7
import sys
import os
import GoogleImg
urls = []
with open('search7.txt','r') as f:
	for line in f.readlines():
		url = os.popen(line).read()
		urls.append(url)
with open('url7.txt','wb') as f:
	for url in urls:
		f.write(url+'\n')
#!/usr/bin/env python2.7
import sys
import os
import GoogleImg
urls = []
with open('search8.txt','r') as f:
	for line in f.readlines():
		url = os.popen(line).read()
		urls.append(url)
with open('url8.txt','wb') as f:
	for url in urls:
		f.write(url+'\n')
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
#os.system("rm url* search*.txt *.html")
if (WORLD_NEWS):
	#Compiles sports page
#	os.system("./topreddit1.py -n 0 | tee reddits.txt | ./keywords.py | tee keys.txt | ./strip.py | ./search.py | ./shuffle.py | head -n 5 > data1.txt 2> /dev/null") 
#	os.system("./callGoogleImg.py -n 1")
#	os.system("./readData1.py")
	os.system("cat data1.txt | ./createWorldnewsPage.py")
if (POLITICS):
	#Compiles science page
#	os.system("./topreddit1.py -n 1 | tee reddits.txt | ./keywords.py | tee keys.txt | ./strip.py | ./search.py | ./shuffle.py | head -n 5 > data2.txt 2> /dev/null")
#    os.system("./callGoogleImg.py -n 2")
#    os.system("./readData2.py")
	os.system("cat data2.txt | ./createPoliticsPage.py")
if (TECHNOLOGY):
	#Compiles politics page
#	os.system("./topreddit1.py -n 2 | tee reddits.txt | ./keywords.py | tee keys.txt | ./strip.py | ./search.py | ./shuffle.py  2> /dev/null | head -n 5 > data3.txt 2> /dev/null")
 #   os.system("./callGoogleImg.py -n 3")
#    os.system("./readData3.py")
	os.system("cat data3.txt | ./createTechnologyPage.py")
if (FUTUROLOGY):
	#Compiles futurology page
#	os.system("./topreddit1.py -n 3 | tee reddits.txt | ./keywords.py | tee keys.txt | ./strip.py | ./search.py| ./shuffle.py  2> /dev/null | head -n 5  > data4.txt 2> /dev/null")
#    os.system("./callGoogleImg.py -n 4")
#    os.system("./readData4.py")
	os.system("cat data4.txt | ./createFuturologyPage.py")
if (SCIENCE):
	#Compiles tech page
#	os.system("./topreddit1.py -n 4 | tee reddits.txt | ./keywords.py | tee keys.txt | ./strip.py | ./search.py | ./shuffle.py  2> /dev/null | head -n 5 > data5.txt 2> /dev/null")
#    os.system("./callGoogleImg.py -n 5")
#    os.system("./readData5.py")
	os.system("cat data5.txt | ./createSciencePage.py")
if (BOOKS):
	#Compiles news page
#	os.system("./topreddit1.py -n 5 | tee reddits.txt | ./keywords.py | tee keys.txt | ./strip.py |./search.py | ./shuffle.py  2> /dev/null | head -n 5 > data6.txt 2> /dev/null")
#    os.system("./callGoogleImg.py -n 6")
#    os.system("./readData6.py")
	os.system("cat data6.txt | ./createBooksPage.py")
if (SPORTS):
	#Compiles books page
#	os.system("./topreddit1.py -n 6 | tee reddits.txt | ./keywords.py | tee keys.txt | ./strip.py | ./search.py | shuffle.py  2> /dev/null | head -n 5 > data7.txt 2> /dev/null")
#    os.system("./callGoogleImg.py -n 7")
#    os.system("./readData7.py")
	os.system("cat data7.txt | ./createSportsPage.py")
if (MEMES):
     #Compiles books page
#	os.system("./topreddit1.py -n 7 -s {} | tee reddits.txt | ./keywords.py | tee keys.txt | ./strip.py | ./search.py | ./shuffle.py  2> /dev/null | head -n 5 > data8.txt 2> /dev/null".format(csub))
#    os.system("./callGoogleImg.py -n 8")
 #   os.system("./readData8.py")
	os.system("cat data8.txt | ./createCustomPage.py")
os.system("./test_output.py 2> /dev/null")
#!/usr/bin/env python2.7
# search.py
import sys
import os
import requests
import subprocess
import urllib2
import string
import re
from lxml import etree
URL = 'https://5q2kx9wux7.execute-api.us-east-1.amazonaws.com/dev/search?query='
keyword = []
for line in sys.stdin:
	words = line.split(':')
	for word in words:
		keyword.append(word.rstrip())
headers = {'x-api-key': 'WyOS4BNZ3K4h8WwbqGwfO57Y1MqXmwgI8RGWalEs'}
for word in keyword:
	print word
	word = word.replace(" ", "_")
	if os.path.isfile('./caches/'+word+'.txt'):
		pass
	else:
		with open('./caches/'+word+'.txt','w') as x:
			word = word.replace("_", " ")
			url = URL + word
			f = requests.get(url, headers=headers)
			x.write(f.content)
	word = word.replace(" ", "_")
	f = open('./caches/'+word+'.txt', 'r')
	data = f.read().replace('\n', '')
	sorts = re.findall('<sort>[\s\S]*?</sort>', data, re.DOTALL)
	sorts = "\n".join(sorts)
	titles = []
	authors = []
	for x in sorts.split('\n'):
		if re.match('.*<author>.*', x) and re.match('.*<title>.*', x):
			try:
				temp1 = re.findall('<title>[^<|&]*<', x, re.DOTALL)[0]
			except:
				temp1 = 'N\/A'
			try:
				temp2 = re.findall('<author>[^<|&]*<', x, re.DOTALL)[0]
			except:
				temp2 = 'N\/A'
			if temp1 != 'N\/A' and temp2 != 'N\/A':
				titles.append(temp1)
				authors.append(temp2)
	#titles = re.findall('<title>[^<|&]*<', sorts, re.DOTALL)
	#titles = list(set(titles))
	#authors = re.findall('<author>[^<|&]*<', sorts, re.DOTALL)
	#authors = list(set(authors))
	titles = [line.translate(None, '<>$/').replace('title', '') for line in titles]
	titles = [re.sub(' +$', '', line) for line in titles]
	authors = [line.translate(None, '<>$/1234567890-.').replace('author', '') for line in authors]
	authors = [re.sub(', +$', '', line) for line in authors]
	counter = 0
	while counter < len(titles) and counter < len(authors):
		print titles[counter] + ' :$: ' + authors[counter]
		counter += 1
#!/usr/bin/env python2.7
import sys
from random import shuffle
x = []
for line in sys.stdin:
	x.append(line)
shuffle(x)
print ''.join(x)
#!/usr/bin/env python2.7
import sys
nospace = [line for line in sys.stdin if line.strip() != '']
print ''.join(nospace)
#!/usr/bin/env python2.7
import string
pageTemplate= '''<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html style="background-color:lightblue">
<head>
<meta content="text/html; charset=ISO-8859-1"http-equiv="content-type">
<title>Book Feed </title>
<h1 style="color:black">Welcome to your source for information!</h1>
</head>
<body style="background-color:lightblue">
<h2 style="color:blue" href="https://www.google.com> Trending in Politics ... </h2>
<p style="color:green"> Find out what's trending YOUR world! </p>
<a href="PoliticsSub.html"> /r/politics</a><br>
<a href="WorldnewsSub.html"> /r/worldnews</a><br>
<a href="TechnologySub.html"> /r/technology</a><br>
<a href="FuturologySub.html"> /r/Futurology</a><br>
<a href="SportsSub.html"> /r/sports</a><br>
<a href="Books.html"> /r/Books</a>
<form action="http://www.google.com">	
	<p>Subreddit Choice:
	<input type="text" name="username" size="15" maxlength="30" />
	</p>
</form> 
</body>
</html>
'''
   
def main():
    #VARIABLES TO BE USED IN FUNCTIONS
    drink = raw_input("Enter a drink if you want to pick your drink (we can match a drink to suite your meal): ")
    contents = pageTemplate.format(**locals())
    browseLocal(contents)
 
def strToFile(text, filename):
    output = open(filename,"w")
    output.write(text)
    output.close()
def browseLocal(webpageText, filename='tempBrowseLocal.html'):
    import webbrowser, os.path
    strToFile(webpageText, filename)
    webbrowser.open("file:///" + os.path.abspath(filename))                                   
main()
#!/usr/bin/env python2.7
import string
pageTemplate= '''<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html style="background-color:lightblue">
<head>
<meta content="text/html; charset=ISO-8859-1"http-equiv="content-type">
<title>
</title>
<h1 style="color:black">Welcome to your source for information!</h1>
</head>
<body style="background-color:lightblue">
<div>
<img src="BOOKFEED.PNG" width="518" height="113" align="center"/>
</div>
<h2 style="color:blue" href="https://www.google.com> Trending in Politics ... </h2>
<p style="color:green"> Find out what's trending YOUR world! </p>
<a href="CustomSub.html"> /r/politics</a><br>
<a href="CustomSub.html"> /r/worldnews</a><br>
<a href="TechnologySub.html"> /r/technology</a><br>
<a href="FuturologySub.html"> /r/Futurology</a><br>
<a href="ScienceSub.html"> /r/science</a><br>
<a href="SportsSub.html"> /r/sports</a><br>
<a href="BooksSub.html"> /r/Books</a><br>
<a href="https://www.reddit.com"> Articles Provided By ... </a><br>
<br>
<br>
<p> JerseyBoys++ </p> 
</form> 
</body>
</html>
'''
   
def main():
    #VARIABLES TO BE USED IN FUNCTIONS
    contents = pageTemplate.format(**locals())
    browseLocal(contents)
 
def strToFile(text, filename):
    output = open(filename,"w")
    output.write(text)
    output.close()
def browseLocal(webpageText, filename='tempBrowseLocal.html'):
    import webbrowser, os.path
    strToFile(webpageText, filename)
    webbrowser.open("file:///" + os.path.abspath(filename))                                   
main()
#!/usr/bin/env python2.7
import sys
A1 = ' '
T1 = ' '
for line in sys.stdin:
    if (1 > 0):
        line = line.split(':$:')
        T1 = line[0]
        A1 = line[1]
        A1 = A1.translate(None, ' ,').rstrip()
        T1 = T1.translate(None, ' ,').rstrip()
        full = A1 +  '+' + T1
        string = 'cat {} | ./GoogleImg.py | head -n 2 | tail -n 1 '.format(full)
        JP1 = os.popen(string)
        response = requests.get(JP1)
        with open('boJP1.png', 'wb') as pic:
             pic.write(reponse.content)
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
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
  <link crossorigin="anonymous" href="https://assets-cdn.github.com/assets/frameworks-80206cf5276e283a2a42e750a19cfc777c5bc184c6509b5db88bac96930c339f.css" media="all" rel="stylesheet" />
  <link crossorigin="anonymous" href="https://assets-cdn.github.com/assets/github-e37787f054128b693988d66147a56af54ed8c479fa4abd1a183d787453cc90a6.css" media="all" rel="stylesheet" />
  
  
  <link crossorigin="anonymous" href="https://assets-cdn.github.com/assets/site-f4fa6ace91e5f0fabb47e8405e5ecf6a9815949cd3958338f6578e626cd443d7.css" media="all" rel="stylesheet" />
  
  <meta name="viewport" content="width=device-width">
  
  <title>xml2json/xml2json.py at master · hay/xml2json · GitHub</title>
  <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub">
  <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub">
  <meta property="fb:app_id" content="1401488693436528">
    
    <meta content="https://avatars1.githubusercontent.com/u/129681?v=3&amp;s=400" property="og:image" /><meta content="GitHub" property="og:site_name" /><meta content="object" property="og:type" /><meta content="hay/xml2json" property="og:title" /><meta content="https://github.com/hay/xml2json" property="og:url" /><meta content="xml2json - Python script converts XML to JSON or the other way around" property="og:description" />
  <link rel="assets" href="https://assets-cdn.github.com/">
  
  <meta name="pjax-timeout" content="1000">
  
  <meta name="request-id" content="CB54:BD3A:2C84257:482A5C4:58E00D89" data-pjax-transient>
  
  <meta name="selected-link" value="repo_source" data-pjax-transient>
  <meta name="google-site-verification" content="KT5gs8h0wvaagLKAVWq8bbeNwnZZK1r1XQysX3xurLU">
<meta name="google-site-verification" content="ZzhVyEFwb7w3e0-uOTltm8Jsck2F5StVihD0exw2fsA">
    <meta name="google-analytics" content="UA-3769691-2">
<meta content="collector.githubapp.com" name="octolytics-host" /><meta content="github" name="octolytics-app-id" /><meta content="https://collector.githubapp.com/github-external/browser_event" name="octolytics-event-url" /><meta content="CB54:BD3A:2C84257:482A5C4:58E00D89" name="octolytics-dimension-request_id" />
<meta content="/&lt;user-name&gt;/&lt;repo-name&gt;/blob/show" data-pjax-transient="true" name="analytics-location" />
  <meta class="js-ga-set" name="dimension1" content="Logged Out">
  
      <meta name="hostname" content="github.com">
  <meta name="user-login" content="">
      <meta name="expected-hostname" content="github.com">
    <meta name="js-proxy-site-detection-payload" content="MDg1MGQ3NTYzZDg0MDJjMzU1MGJlNjdjMjA3MDY3ZDI3MDAzY2I2M2NlNGM3NDg3YTJhNzY1ZjcxODgwZDVlZHx7InJlbW90ZV9hZGRyZXNzIjoiMTI5Ljc0LjE1Mi43MyIsInJlcXVlc3RfaWQiOiJDQjU0OkJEM0E6MkM4NDI1Nzo0ODJBNUM0OjU4RTAwRDg5IiwidGltZXN0YW1wIjoxNDkxMDc4NTM4LCJob3N0IjoiZ2l0aHViLmNvbSJ9">
  <meta name="html-safe-nonce" content="f1c536a9aa51bc5c7d21cc1bab1aeb915e41c605">
  <meta http-equiv="x-pjax-version" content="7fd8eb26117c353adeedb9d8318a2b0e">
  
    
  <meta name="description" content="xml2json - Python script converts XML to JSON or the other way around">
  <meta name="go-import" content="github.com/hay/xml2json git https://github.com/hay/xml2json.git">
  <meta content="129681" name="octolytics-dimension-user_id" /><meta content="hay" name="octolytics-dimension-user_login" /><meta content="946900" name="octolytics-dimension-repository_id" /><meta content="hay/xml2json" name="octolytics-dimension-repository_nwo" /><meta content="true" name="octolytics-dimension-repository_public" /><meta content="false" name="octolytics-dimension-repository_is_fork" /><meta content="946900" name="octolytics-dimension-repository_network_root_id" /><meta content="hay/xml2json" name="octolytics-dimension-repository_network_root_nwo" />
        <link href="https://github.com/hay/xml2json/commits/master.atom" rel="alternate" title="Recent Commits to xml2json:master" type="application/atom+xml">
    <link rel="canonical" href="https://github.com/hay/xml2json/blob/master/xml2json.py" data-pjax-transient>
  <meta name="browser-stats-url" content="https://api.github.com/_private/browser/stats">
  <meta name="browser-errors-url" content="https://api.github.com/_private/browser/errors">
  <link rel="mask-icon" href="https://assets-cdn.github.com/pinned-octocat.svg" color="#000000">
  <link rel="icon" type="image/x-icon" href="https://assets-cdn.github.com/favicon.ico">
<meta name="theme-color" content="#1e2327">
  </head>
  <body class="logged-out env-production page-blob">
    
  <div class="position-relative js-header-wrapper ">
    <a href="#start-of-content" tabindex="1" class="accessibility-aid js-skip-to-content">Skip to content</a>
    <div id="js-pjax-loader-bar" class="pjax-loader-bar"><div class="progress"></div></div>
    
    
    
          <header class="site-header js-details-container Details" role="banner">
  <div class="container-responsive">
    <a class="header-logo-invertocat" href="https://github.com/" aria-label="Homepage" data-ga-click="(Logged out) Header, go to homepage, icon:logo-wordmark">
      <svg aria-hidden="true" class="octicon octicon-mark-github" height="32" version="1.1" viewBox="0 0 16 16" width="32"><path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z"/></svg>
    </a>
    <button class="btn-link float-right site-header-toggle js-details-target" type="button" aria-label="Toggle navigation">
      <svg aria-hidden="true" class="octicon octicon-three-bars" height="24" version="1.1" viewBox="0 0 12 16" width="18"><path fill-rule="evenodd" d="M11.41 9H.59C0 9 0 8.59 0 8c0-.59 0-1 .59-1H11.4c.59 0 .59.41.59 1 0 .59 0 1-.59 1h.01zm0-4H.59C0 5 0 4.59 0 4c0-.59 0-1 .59-1H11.4c.59 0 .59.41.59 1 0 .59 0 1-.59 1h.01zM.59 11H11.4c.59 0 .59.41.59 1 0 .59 0 1-.59 1H.59C0 13 0 12.59 0 12c0-.59 0-1 .59-1z"/></svg>
    </button>
    <div class="site-header-menu">
      <nav class="site-header-nav">
        <a href="/features" class="js-selected-navigation-item nav-item" data-ga-click="Header, click, Nav menu - item:features" data-selected-links="/features /features">
          Features
</a>        <a href="/business" class="js-selected-navigation-item nav-item" data-ga-click="Header, click, Nav menu - item:business" data-selected-links="/business /business/security /business/customers /business">
          Business
</a>        <a href="/explore" class="js-selected-navigation-item nav-item" data-ga-click="Header, click, Nav menu - item:explore" data-selected-links="/explore /trending /trending/developers /integrations /integrations/feature/code /integrations/feature/collaborate /integrations/feature/ship /showcases /explore">
          Explore
</a>        <a href="/pricing" class="js-selected-navigation-item nav-item" data-ga-click="Header, click, Nav menu - item:pricing" data-selected-links="/pricing /pricing">
          Pricing
</a>      </nav>
      <div class="site-header-actions">
          <div class="header-search scoped-search site-scoped-search js-site-search" role="search">
  <!-- '"` --><!-- </textarea></xmp> --></option></form><form accept-charset="UTF-8" action="/hay/xml2json/search" class="js-site-search-form" data-scoped-search-url="/hay/xml2json/search" data-unscoped-search-url="/search" method="get"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /></div>
    <label class="form-control header-search-wrapper js-chromeless-input-container">
        <a href="/hay/xml2json/blob/master/xml2json.py" class="header-search-scope no-underline">This repository</a>
      <input type="text"
        class="form-control header-search-input js-site-search-focus js-site-search-field is-clearable"
        data-hotkey="s"
        name="q"
        value=""
        placeholder="Search"
        aria-label="Search this repository"
        data-unscoped-placeholder="Search GitHub"
        data-scoped-placeholder="Search"
        autocapitalize="off">
        <input type="hidden" class="js-site-search-type-field" name="type" >
    </label>
</form></div>
          <a class="text-bold site-header-link" href="/login?return_to=%2Fhay%2Fxml2json%2Fblob%2Fmaster%2Fxml2json.py" data-ga-click="(Logged out) Header, clicked Sign in, text:sign-in">Sign in</a>
            <span class="text-gray">or</span>
            <a class="text-bold site-header-link" href="/join?source=header-repo" data-ga-click="(Logged out) Header, clicked Sign up, text:sign-up">Sign up</a>
      </div>
    </div>
  </div>
</header>
  </div>
  <div id="start-of-content" class="accessibility-aid"></div>
    <div id="js-flash-container">
</div>
  <div role="main">
        <div itemscope itemtype="http://schema.org/SoftwareSourceCode">
    <div id="js-repo-pjax-container" data-pjax-container>
        
  <div class="pagehead repohead instapaper_ignore readability-menu experiment-repo-nav">
    <div class="container repohead-details-container">
      <ul class="pagehead-actions">
  <li>
      <a href="/login?return_to=%2Fhay%2Fxml2json"
    class="btn btn-sm btn-with-count tooltipped tooltipped-n"
    aria-label="You must be signed in to watch a repository" rel="nofollow">
    <svg aria-hidden="true" class="octicon octicon-eye" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M8.06 2C3 2 0 8 0 8s3 6 8.06 6C13 14 16 8 16 8s-3-6-7.94-6zM8 12c-2.2 0-4-1.78-4-4 0-2.2 1.8-4 4-4 2.22 0 4 1.8 4 4 0 2.22-1.78 4-4 4zm2-4c0 1.11-.89 2-2 2-1.11 0-2-.89-2-2 0-1.11.89-2 2-2 1.11 0 2 .89 2 2z"/></svg>
    Watch
  </a>
  <a class="social-count" href="/hay/xml2json/watchers"
     aria-label="21 users are watching this repository">
    21
  </a>
  </li>
  <li>
      <a href="/login?return_to=%2Fhay%2Fxml2json"
    class="btn btn-sm btn-with-count tooltipped tooltipped-n"
    aria-label="You must be signed in to star a repository" rel="nofollow">
    <svg aria-hidden="true" class="octicon octicon-star" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path fill-rule="evenodd" d="M14 6l-4.9-.64L7 1 4.9 5.36 0 6l3.6 3.26L2.67 14 7 11.67 11.33 14l-.93-4.74z"/></svg>
    Star
  </a>
    <a class="social-count js-social-count" href="/hay/xml2json/stargazers"
      aria-label="315 users starred this repository">
      315
    </a>
  </li>
  <li>
      <a href="/login?return_to=%2Fhay%2Fxml2json"
        class="btn btn-sm btn-with-count tooltipped tooltipped-n"
        aria-label="You must be signed in to fork a repository" rel="nofollow">
        <svg aria-hidden="true" class="octicon octicon-repo-forked" height="16" version="1.1" viewBox="0 0 10 16" width="10"><path fill-rule="evenodd" d="M8 1a1.993 1.993 0 0 0-1 3.72V6L5 8 3 6V4.72A1.993 1.993 0 0 0 2 1a1.993 1.993 0 0 0-1 3.72V6.5l3 3v1.78A1.993 1.993 0 0 0 5 15a1.993 1.993 0 0 0 1-3.72V9.5l3-3V4.72A1.993 1.993 0 0 0 8 1zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zm3 10c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zm3-10c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"/></svg>
        Fork
      </a>
    <a href="/hay/xml2json/network" class="social-count"
       aria-label="153 users forked this repository">
      153
    </a>
  </li>
</ul>
      <h1 class="public ">
  <svg aria-hidden="true" class="octicon octicon-repo" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M4 9H3V8h1v1zm0-3H3v1h1V6zm0-2H3v1h1V4zm0-2H3v1h1V2zm8-1v12c0 .55-.45 1-1 1H6v2l-1.5-1.5L3 16v-2H1c-.55 0-1-.45-1-1V1c0-.55.45-1 1-1h10c.55 0 1 .45 1 1zm-1 10H1v2h2v-1h3v1h5v-2zm0-10H2v9h9V1z"/></svg>
  <span class="author" itemprop="author"><a href="/hay" class="url fn" rel="author">hay</a></span><!--
--><span class="path-divider">/</span><!--
--><strong itemprop="name"><a href="/hay/xml2json" data-pjax="#js-repo-pjax-container">xml2json</a></strong>
</h1>
    </div>
    <div class="container">
      
<nav class="reponav js-repo-nav js-sidenav-container-pjax"
     itemscope
     itemtype="http://schema.org/BreadcrumbList"
     role="navigation"
     data-pjax="#js-repo-pjax-container">
  <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
    <a href="/hay/xml2json" class="js-selected-navigation-item selected reponav-item" data-hotkey="g c" data-selected-links="repo_source repo_downloads repo_commits repo_releases repo_tags repo_branches /hay/xml2json" itemprop="url">
      <svg aria-hidden="true" class="octicon octicon-code" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path fill-rule="evenodd" d="M9.5 3L8 4.5 11.5 8 8 11.5 9.5 13 14 8 9.5 3zm-5 0L0 8l4.5 5L6 11.5 2.5 8 6 4.5 4.5 3z"/></svg>
      <span itemprop="name">Code</span>
      <meta itemprop="position" content="1">
</a>  </span>
    <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
      <a href="/hay/xml2json/issues" class="js-selected-navigation-item reponav-item" data-hotkey="g i" data-selected-links="repo_issues repo_labels repo_milestones /hay/xml2json/issues" itemprop="url">
        <svg aria-hidden="true" class="octicon octicon-issue-opened" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"/></svg>
        <span itemprop="name">Issues</span>
        <span class="counter">5</span>
        <meta itemprop="position" content="2">
</a>    </span>
  <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
    <a href="/hay/xml2json/pulls" class="js-selected-navigation-item reponav-item" data-hotkey="g p" data-selected-links="repo_pulls /hay/xml2json/pulls" itemprop="url">
      <svg aria-hidden="true" class="octicon octicon-git-pull-request" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"/></svg>
      <span itemprop="name">Pull requests</span>
      <span class="counter">10</span>
      <meta itemprop="position" content="3">
</a>  </span>
    <a href="/hay/xml2json/projects" class="js-selected-navigation-item reponav-item" data-selected-links="repo_projects new_repo_project repo_project /hay/xml2json/projects">
      <svg aria-hidden="true" class="octicon octicon-project" height="16" version="1.1" viewBox="0 0 15 16" width="15"><path fill-rule="evenodd" d="M10 12h3V2h-3v10zm-4-2h3V2H6v8zm-4 4h3V2H2v12zm-1 1h13V1H1v14zM14 0H1a1 1 0 0 0-1 1v14a1 1 0 0 0 1 1h13a1 1 0 0 0 1-1V1a1 1 0 0 0-1-1z"/></svg>
      Projects
      <span class="counter">0</span>
</a>
  <a href="/hay/xml2json/pulse" class="js-selected-navigation-item reponav-item" data-selected-links="pulse /hay/xml2json/pulse">
    <svg aria-hidden="true" class="octicon octicon-pulse" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path fill-rule="evenodd" d="M11.5 8L8.8 5.4 6.6 8.5 5.5 1.6 2.38 8H0v2h3.6l.9-1.8.9 5.4L9 8.5l1.6 1.5H14V8z"/></svg>
    Pulse
</a>
  <a href="/hay/xml2json/graphs" class="js-selected-navigation-item reponav-item" data-selected-links="repo_graphs repo_contributors /hay/xml2json/graphs">
    <svg aria-hidden="true" class="octicon octicon-graph" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M16 14v1H0V0h1v14h15zM5 13H3V8h2v5zm4 0H7V3h2v10zm4 0h-2V6h2v7z"/></svg>
    Graphs
</a>
</nav>
    </div>
  </div>
<div class="container new-discussion-timeline experiment-repo-nav">
  <div class="repository-content">
    
<a href="/hay/xml2json/blob/22ffcdf75b967fedd62bde065efdfcd02b216e80/xml2json.py" class="d-none js-permalink-shortcut" data-hotkey="y">Permalink</a>
<!-- blob contrib key: blob_contributors:v21:73fb9434c61db68b0be4afeb5c533e7c -->
<div class="file-navigation js-zeroclipboard-container">
  
<div class="select-menu branch-select-menu js-menu-container js-select-menu float-left">
  <button class=" btn btn-sm select-menu-button js-menu-target css-truncate" data-hotkey="w"
    
    type="button" aria-label="Switch branches or tags" tabindex="0" aria-haspopup="true">
      <i>Branch:</i>
      <span class="js-select-button css-truncate-target">master</span>
  </button>
  <div class="select-menu-modal-holder js-menu-content js-navigation-container" data-pjax aria-hidden="true">
    <div class="select-menu-modal">
      <div class="select-menu-header">
        <svg aria-label="Close" class="octicon octicon-x js-menu-close" height="16" role="img" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48z"/></svg>
        <span class="select-menu-title">Switch branches/tags</span>
      </div>
      <div class="select-menu-filters">
        <div class="select-menu-text-filter">
          <input type="text" aria-label="Filter branches/tags" id="context-commitish-filter-field" class="form-control js-filterable-field js-navigation-enable" placeholder="Filter branches/tags">
        </div>
        <div class="select-menu-tabs">
          <ul>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="branches" data-filter-placeholder="Filter branches/tags" class="js-select-menu-tab" role="tab">Branches</a>
            </li>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="tags" data-filter-placeholder="Find a tag…" class="js-select-menu-tab" role="tab">Tags</a>
            </li>
          </ul>
        </div>
      </div>
      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="branches" role="menu">
        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">
            <a class="select-menu-item js-navigation-item js-navigation-open selected"
               href="/hay/xml2json/blob/master/xml2json.py"
               data-name="master"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                master
              </span>
            </a>
        </div>
          <div class="select-menu-no-results">Nothing to show</div>
      </div>
      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="tags">
        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">
        </div>
        <div class="select-menu-no-results">Nothing to show</div>
      </div>
    </div>
  </div>
</div>
  <div class="BtnGroup float-right">
    <a href="/hay/xml2json/find/master"
          class="js-pjax-capture-input btn btn-sm BtnGroup-item"
          data-pjax
          data-hotkey="t">
      Find file
    </a>
    <button aria-label="Copy file path to clipboard" class="js-zeroclipboard btn btn-sm BtnGroup-item tooltipped tooltipped-s" data-copied-hint="Copied!" type="button">Copy path</button>
  </div>
  <div class="breadcrumb js-zeroclipboard-target">
    <span class="repo-root js-repo-root"><span class="js-path-segment"><a href="/hay/xml2json"><span>xml2json</span></a></span></span><span class="separator">/</span><strong class="final-path">xml2json.py</strong>
  </div>
</div>
  <div class="commit-tease">
      <span class="float-right">
        <a class="commit-tease-sha" href="/hay/xml2json/commit/925de7db43eba2d2291af9573b8f996e9b7748a9" data-pjax>
          925de7d
        </a>
        <relative-time datetime="2017-02-07T12:49:05Z">Feb 7, 2017</relative-time>
      </span>
      <div>
        <img alt="@grunde73" class="avatar" height="20" src="https://avatars2.githubusercontent.com/u/15782558?v=3&amp;s=40" width="20" />
        <a href="/grunde73" class="user-mention" rel="contributor">grunde73</a>
          <a href="/hay/xml2json/commit/925de7db43eba2d2291af9573b8f996e9b7748a9" class="message" data-pjax="true" title="JSON order same as XML
Output JASON is now in the same order as the input XML file.">JSON order same as XML</a>
      </div>
    <div class="commit-tease-contributors">
      <button type="button" class="btn-link muted-link contributors-toggle" data-facebox="#blob_contributors_box">
        <strong>10</strong>
         contributors
      </button>
          <a class="avatar-link tooltipped tooltipped-s" aria-label="hay" href="/hay/xml2json/commits/master/xml2json.py?author=hay"><img alt="@hay" class="avatar" height="20" src="https://avatars2.githubusercontent.com/u/129681?v=3&amp;s=40" width="20" /> </a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="cemmanouilidis" href="/hay/xml2json/commits/master/xml2json.py?author=cemmanouilidis"><img alt="@cemmanouilidis" class="avatar" height="20" src="https://avatars0.githubusercontent.com/u/657476?v=3&amp;s=40" width="20" /> </a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="larrycai" href="/hay/xml2json/commits/master/xml2json.py?author=larrycai"><img alt="@larrycai" class="avatar" height="20" src="https://avatars2.githubusercontent.com/u/106192?v=3&amp;s=40" width="20" /> </a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="jdanbrown" href="/hay/xml2json/commits/master/xml2json.py?author=jdanbrown"><img alt="@jdanbrown" class="avatar" height="20" src="https://avatars2.githubusercontent.com/u/627486?v=3&amp;s=40" width="20" /> </a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="noelpark" href="/hay/xml2json/commits/master/xml2json.py?author=noelpark"><img alt="@noelpark" class="avatar" height="20" src="https://avatars2.githubusercontent.com/u/965475?v=3&amp;s=40" width="20" /> </a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="sl45sms" href="/hay/xml2json/commits/master/xml2json.py?author=sl45sms"><img alt="@sl45sms" class="avatar" height="20" src="https://avatars3.githubusercontent.com/u/63211?v=3&amp;s=40" width="20" /> </a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="scottchiefbaker" href="/hay/xml2json/commits/master/xml2json.py?author=scottchiefbaker"><img alt="@scottchiefbaker" class="avatar" height="20" src="https://avatars3.githubusercontent.com/u/3429760?v=3&amp;s=40" width="20" /> </a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="grunde73" href="/hay/xml2json/commits/master/xml2json.py?author=grunde73"><img alt="@grunde73" class="avatar" height="20" src="https://avatars2.githubusercontent.com/u/15782558?v=3&amp;s=40" width="20" /> </a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="gmh04" href="/hay/xml2json/commits/master/xml2json.py?author=gmh04"><img alt="@gmh04" class="avatar" height="20" src="https://avatars3.githubusercontent.com/u/611548?v=3&amp;s=40" width="20" /> </a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="webmalex" href="/hay/xml2json/commits/master/xml2json.py?author=webmalex"><img alt="@webmalex" class="avatar" height="20" src="https://avatars3.githubusercontent.com/u/365578?v=3&amp;s=40" width="20" /> </a>
    </div>
    <div id="blob_contributors_box" style="display:none">
      <h2 class="facebox-header" data-facebox-id="facebox-header">Users who have contributed to this file</h2>
      <ul class="facebox-user-list" data-facebox-id="facebox-description">
          <li class="facebox-user-list-item">
            <img alt="@hay" height="24" src="https://avatars0.githubusercontent.com/u/129681?v=3&amp;s=48" width="24" />
            <a href="/hay">hay</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="@cemmanouilidis" height="24" src="https://avatars2.githubusercontent.com/u/657476?v=3&amp;s=48" width="24" />
            <a href="/cemmanouilidis">cemmanouilidis</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="@larrycai" height="24" src="https://avatars0.githubusercontent.com/u/106192?v=3&amp;s=48" width="24" />
            <a href="/larrycai">larrycai</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="@jdanbrown" height="24" src="https://avatars0.githubusercontent.com/u/627486?v=3&amp;s=48" width="24" />
            <a href="/jdanbrown">jdanbrown</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="@noelpark" height="24" src="https://avatars0.githubusercontent.com/u/965475?v=3&amp;s=48" width="24" />
            <a href="/noelpark">noelpark</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="@sl45sms" height="24" src="https://avatars1.githubusercontent.com/u/63211?v=3&amp;s=48" width="24" />
            <a href="/sl45sms">sl45sms</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="@scottchiefbaker" height="24" src="https://avatars1.githubusercontent.com/u/3429760?v=3&amp;s=48" width="24" />
            <a href="/scottchiefbaker">scottchiefbaker</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="@grunde73" height="24" src="https://avatars0.githubusercontent.com/u/15782558?v=3&amp;s=48" width="24" />
            <a href="/grunde73">grunde73</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="@gmh04" height="24" src="https://avatars1.githubusercontent.com/u/611548?v=3&amp;s=48" width="24" />
            <a href="/gmh04">gmh04</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="@webmalex" height="24" src="https://avatars1.githubusercontent.com/u/365578?v=3&amp;s=48" width="24" />
            <a href="/webmalex">webmalex</a>
          </li>
      </ul>
    </div>
  </div>
<div class="file">
  <div class="file-header">
  <div class="file-actions">
    <div class="BtnGroup">
      <a href="/hay/xml2json/raw/master/xml2json.py" class="btn btn-sm BtnGroup-item" id="raw-url">Raw</a>
        <a href="/hay/xml2json/blame/master/xml2json.py" class="btn btn-sm js-update-url-with-hash BtnGroup-item" data-hotkey="b">Blame</a>
      <a href="/hay/xml2json/commits/master/xml2json.py" class="btn btn-sm BtnGroup-item" rel="nofollow">History</a>
    </div>
        <button type="button" class="btn-octicon disabled tooltipped tooltipped-nw"
          aria-label="You must be signed in to make or propose changes">
          <svg aria-hidden="true" class="octicon octicon-pencil" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path fill-rule="evenodd" d="M0 12v3h3l8-8-3-3-8 8zm3 2H1v-2h1v1h1v1zm10.3-9.3L12 6 9 3l1.3-1.3a.996.996 0 0 1 1.41 0l1.59 1.59c.39.39.39 1.02 0 1.41z"/></svg>
        </button>
        <button type="button" class="btn-octicon btn-octicon-danger disabled tooltipped tooltipped-nw"
          aria-label="You must be signed in to make or propose changes">
          <svg aria-hidden="true" class="octicon octicon-trashcan" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M11 2H9c0-.55-.45-1-1-1H5c-.55 0-1 .45-1 1H2c-.55 0-1 .45-1 1v1c0 .55.45 1 1 1v9c0 .55.45 1 1 1h7c.55 0 1-.45 1-1V5c.55 0 1-.45 1-1V3c0-.55-.45-1-1-1zm-1 12H3V5h1v8h1V5h1v8h1V5h1v8h1V5h1v9zm1-10H2V3h9v1z"/></svg>
        </button>
  </div>
  <div class="file-info">
      <span class="file-mode" title="File mode">executable file</span>
      <span class="file-info-divider"></span>
      252 lines (198 sloc)
      <span class="file-info-divider"></span>
    7.29 KB
  </div>
</div>
  
  <div itemprop="text" class="blob-wrapper data type-python">
      <table class="highlight tab-size js-file-line-container" data-tab-size="8">
      <tr>
        <td id="L1" class="blob-num js-line-number" data-line-number="1"></td>
        <td id="LC1" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>!/usr/bin/env python</span></td>
      </tr>
      <tr>
        <td id="L2" class="blob-num js-line-number" data-line-number="2"></td>
        <td id="LC2" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L3" class="blob-num js-line-number" data-line-number="3"></td>
        <td id="LC3" class="blob-code blob-code-inner js-file-line"><span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span>xml2json.py  Convert XML to JSON</span></td>
      </tr>
      <tr>
        <td id="L4" class="blob-num js-line-number" data-line-number="4"></td>
        <td id="LC4" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L5" class="blob-num js-line-number" data-line-number="5"></td>
        <td id="LC5" class="blob-code blob-code-inner js-file-line"><span class="pl-s">Relies on ElementTree for the XML parsing.  This is based on</span></td>
      </tr>
      <tr>
        <td id="L6" class="blob-num js-line-number" data-line-number="6"></td>
        <td id="LC6" class="blob-code blob-code-inner js-file-line"><span class="pl-s">pesterfish.py but uses a different XML-&gt;JSON mapping.</span></td>
      </tr>
      <tr>
        <td id="L7" class="blob-num js-line-number" data-line-number="7"></td>
        <td id="LC7" class="blob-code blob-code-inner js-file-line"><span class="pl-s">The XML-&gt;JSON mapping is described at</span></td>
      </tr>
      <tr>
        <td id="L8" class="blob-num js-line-number" data-line-number="8"></td>
        <td id="LC8" class="blob-code blob-code-inner js-file-line"><span class="pl-s">http://www.xml.com/pub/a/2006/05/31/converting-between-xml-and-json.html</span></td>
      </tr>
      <tr>
        <td id="L9" class="blob-num js-line-number" data-line-number="9"></td>
        <td id="LC9" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L10" class="blob-num js-line-number" data-line-number="10"></td>
        <td id="LC10" class="blob-code blob-code-inner js-file-line"><span class="pl-s">Rewritten to a command line utility by Hay Kranen &lt; github.com/hay &gt; with</span></td>
      </tr>
      <tr>
        <td id="L11" class="blob-num js-line-number" data-line-number="11"></td>
        <td id="LC11" class="blob-code blob-code-inner js-file-line"><span class="pl-s">contributions from George Hamilton (gmh04) and Dan Brown (jdanbrown)</span></td>
      </tr>
      <tr>
        <td id="L12" class="blob-num js-line-number" data-line-number="12"></td>
        <td id="LC12" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L13" class="blob-num js-line-number" data-line-number="13"></td>
        <td id="LC13" class="blob-code blob-code-inner js-file-line"><span class="pl-s">XML                              JSON</span></td>
      </tr>
      <tr>
        <td id="L14" class="blob-num js-line-number" data-line-number="14"></td>
        <td id="LC14" class="blob-code blob-code-inner js-file-line"><span class="pl-s">&lt;e/&gt;                             &quot;e&quot;: null</span></td>
      </tr>
      <tr>
        <td id="L15" class="blob-num js-line-number" data-line-number="15"></td>
        <td id="LC15" class="blob-code blob-code-inner js-file-line"><span class="pl-s">&lt;e&gt;text&lt;/e&gt;                      &quot;e&quot;: &quot;text&quot;</span></td>
      </tr>
      <tr>
        <td id="L16" class="blob-num js-line-number" data-line-number="16"></td>
        <td id="LC16" class="blob-code blob-code-inner js-file-line"><span class="pl-s">&lt;e name=&quot;value&quot; /&gt;               &quot;e&quot;: { &quot;@name&quot;: &quot;value&quot; }</span></td>
      </tr>
      <tr>
        <td id="L17" class="blob-num js-line-number" data-line-number="17"></td>
        <td id="LC17" class="blob-code blob-code-inner js-file-line"><span class="pl-s">&lt;e name=&quot;value&quot;&gt;text&lt;/e&gt;         &quot;e&quot;: { &quot;@name&quot;: &quot;value&quot;, &quot;#text&quot;: &quot;text&quot; }</span></td>
      </tr>
      <tr>
        <td id="L18" class="blob-num js-line-number" data-line-number="18"></td>
        <td id="LC18" class="blob-code blob-code-inner js-file-line"><span class="pl-s">&lt;e&gt; &lt;a&gt;text&lt;/a &gt;&lt;b&gt;text&lt;/b&gt; &lt;/e&gt; &quot;e&quot;: { &quot;a&quot;: &quot;text&quot;, &quot;b&quot;: &quot;text&quot; }</span></td>
      </tr>
      <tr>
        <td id="L19" class="blob-num js-line-number" data-line-number="19"></td>
        <td id="LC19" class="blob-code blob-code-inner js-file-line"><span class="pl-s">&lt;e&gt; &lt;a&gt;text&lt;/a&gt; &lt;a&gt;text&lt;/a&gt; &lt;/e&gt; &quot;e&quot;: { &quot;a&quot;: [&quot;text&quot;, &quot;text&quot;] }</span></td>
      </tr>
      <tr>
        <td id="L20" class="blob-num js-line-number" data-line-number="20"></td>
        <td id="LC20" class="blob-code blob-code-inner js-file-line"><span class="pl-s">&lt;e&gt; text &lt;a&gt;text&lt;/a&gt; &lt;/e&gt;        &quot;e&quot;: { &quot;#text&quot;: &quot;text&quot;, &quot;a&quot;: &quot;text&quot; }</span></td>
      </tr>
      <tr>
        <td id="L21" class="blob-num js-line-number" data-line-number="21"></td>
        <td id="LC21" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L22" class="blob-num js-line-number" data-line-number="22"></td>
        <td id="LC22" class="blob-code blob-code-inner js-file-line"><span class="pl-s">This is very similar to the mapping used for Yahoo Web Services</span></td>
      </tr>
      <tr>
        <td id="L23" class="blob-num js-line-number" data-line-number="23"></td>
        <td id="LC23" class="blob-code blob-code-inner js-file-line"><span class="pl-s">(http://developer.yahoo.com/common/json.html#xml).</span></td>
      </tr>
      <tr>
        <td id="L24" class="blob-num js-line-number" data-line-number="24"></td>
        <td id="LC24" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L25" class="blob-num js-line-number" data-line-number="25"></td>
        <td id="LC25" class="blob-code blob-code-inner js-file-line"><span class="pl-s">This is a mess in that it is so unpredictable -- it requires lots of testing</span></td>
      </tr>
      <tr>
        <td id="L26" class="blob-num js-line-number" data-line-number="26"></td>
        <td id="LC26" class="blob-code blob-code-inner js-file-line"><span class="pl-s">(e.g. to see if values are lists or strings or dictionaries).  For use</span></td>
      </tr>
      <tr>
        <td id="L27" class="blob-num js-line-number" data-line-number="27"></td>
        <td id="LC27" class="blob-code blob-code-inner js-file-line"><span class="pl-s">in Python this could be vastly cleaner.  Think about whether the internal</span></td>
      </tr>
      <tr>
        <td id="L28" class="blob-num js-line-number" data-line-number="28"></td>
        <td id="LC28" class="blob-code blob-code-inner js-file-line"><span class="pl-s">form can be more self-consistent while maintaining good external</span></td>
      </tr>
      <tr>
        <td id="L29" class="blob-num js-line-number" data-line-number="29"></td>
        <td id="LC29" class="blob-code blob-code-inner js-file-line"><span class="pl-s">characteristics for the JSON.</span></td>
      </tr>
      <tr>
        <td id="L30" class="blob-num js-line-number" data-line-number="30"></td>
        <td id="LC30" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L31" class="blob-num js-line-number" data-line-number="31"></td>
        <td id="LC31" class="blob-code blob-code-inner js-file-line"><span class="pl-s">Look at the Yahoo version closely to see how it works.  Maybe can adopt</span></td>
      </tr>
      <tr>
        <td id="L32" class="blob-num js-line-number" data-line-number="32"></td>
        <td id="LC32" class="blob-code blob-code-inner js-file-line"><span class="pl-s">that completely if it makes more sense...</span></td>
      </tr>
      <tr>
        <td id="L33" class="blob-num js-line-number" data-line-number="33"></td>
        <td id="LC33" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L34" class="blob-num js-line-number" data-line-number="34"></td>
        <td id="LC34" class="blob-code blob-code-inner js-file-line"><span class="pl-s">R. White, 2006 November 6</span></td>
      </tr>
      <tr>
        <td id="L35" class="blob-num js-line-number" data-line-number="35"></td>
        <td id="LC35" class="blob-code blob-code-inner js-file-line"><span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L36" class="blob-num js-line-number" data-line-number="36"></td>
        <td id="LC36" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L37" class="blob-num js-line-number" data-line-number="37"></td>
        <td id="LC37" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> json</td>
      </tr>
      <tr>
        <td id="L38" class="blob-num js-line-number" data-line-number="38"></td>
        <td id="LC38" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> optparse</td>
      </tr>
      <tr>
        <td id="L39" class="blob-num js-line-number" data-line-number="39"></td>
        <td id="LC39" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> sys</td>
      </tr>
      <tr>
        <td id="L40" class="blob-num js-line-number" data-line-number="40"></td>
        <td id="LC40" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> os</td>
      </tr>
      <tr>
        <td id="L41" class="blob-num js-line-number" data-line-number="41"></td>
        <td id="LC41" class="blob-code blob-code-inner js-file-line"><span class="pl-k">from</span> collections <span class="pl-k">import</span> OrderedDict</td>
      </tr>
      <tr>
        <td id="L42" class="blob-num js-line-number" data-line-number="42"></td>
        <td id="LC42" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L43" class="blob-num js-line-number" data-line-number="43"></td>
        <td id="LC43" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> xml.etree.cElementTree <span class="pl-k">as</span> <span class="pl-c1">ET</span></td>
      </tr>
      <tr>
        <td id="L44" class="blob-num js-line-number" data-line-number="44"></td>
        <td id="LC44" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L45" class="blob-num js-line-number" data-line-number="45"></td>
        <td id="LC45" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L46" class="blob-num js-line-number" data-line-number="46"></td>
        <td id="LC46" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">strip_tag</span>(<span class="pl-smi">tag</span>):</td>
      </tr>
      <tr>
        <td id="L47" class="blob-num js-line-number" data-line-number="47"></td>
        <td id="LC47" class="blob-code blob-code-inner js-file-line">    strip_ns_tag <span class="pl-k">=</span> tag</td>
      </tr>
      <tr>
        <td id="L48" class="blob-num js-line-number" data-line-number="48"></td>
        <td id="LC48" class="blob-code blob-code-inner js-file-line">    split_array <span class="pl-k">=</span> tag.split(<span class="pl-s"><span class="pl-pds">&#39;</span>}<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L49" class="blob-num js-line-number" data-line-number="49"></td>
        <td id="LC49" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> <span class="pl-c1">len</span>(split_array) <span class="pl-k">&gt;</span> <span class="pl-c1">1</span>:</td>
      </tr>
      <tr>
        <td id="L50" class="blob-num js-line-number" data-line-number="50"></td>
        <td id="LC50" class="blob-code blob-code-inner js-file-line">        strip_ns_tag <span class="pl-k">=</span> split_array[<span class="pl-c1">1</span>]</td>
      </tr>
      <tr>
        <td id="L51" class="blob-num js-line-number" data-line-number="51"></td>
        <td id="LC51" class="blob-code blob-code-inner js-file-line">        tag <span class="pl-k">=</span> strip_ns_tag</td>
      </tr>
      <tr>
        <td id="L52" class="blob-num js-line-number" data-line-number="52"></td>
        <td id="LC52" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">return</span> tag</td>
      </tr>
      <tr>
        <td id="L53" class="blob-num js-line-number" data-line-number="53"></td>
        <td id="LC53" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L54" class="blob-num js-line-number" data-line-number="54"></td>
        <td id="LC54" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L55" class="blob-num js-line-number" data-line-number="55"></td>
        <td id="LC55" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">elem_to_internal</span>(<span class="pl-smi">elem</span>, <span class="pl-smi">strip_ns</span><span class="pl-k">=</span><span class="pl-c1">1</span>, <span class="pl-smi">strip</span><span class="pl-k">=</span><span class="pl-c1">1</span>):</td>
      </tr>
      <tr>
        <td id="L56" class="blob-num js-line-number" data-line-number="56"></td>
        <td id="LC56" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span>Convert an Element into an internal dictionary (not JSON!).<span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L57" class="blob-num js-line-number" data-line-number="57"></td>
        <td id="LC57" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L58" class="blob-num js-line-number" data-line-number="58"></td>
        <td id="LC58" class="blob-code blob-code-inner js-file-line">    d <span class="pl-k">=</span> OrderedDict()</td>
      </tr>
      <tr>
        <td id="L59" class="blob-num js-line-number" data-line-number="59"></td>
        <td id="LC59" class="blob-code blob-code-inner js-file-line">    elem_tag <span class="pl-k">=</span> elem.tag</td>
      </tr>
      <tr>
        <td id="L60" class="blob-num js-line-number" data-line-number="60"></td>
        <td id="LC60" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> strip_ns:</td>
      </tr>
      <tr>
        <td id="L61" class="blob-num js-line-number" data-line-number="61"></td>
        <td id="LC61" class="blob-code blob-code-inner js-file-line">        elem_tag <span class="pl-k">=</span> strip_tag(elem.tag)</td>
      </tr>
      <tr>
        <td id="L62" class="blob-num js-line-number" data-line-number="62"></td>
        <td id="LC62" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L63" class="blob-num js-line-number" data-line-number="63"></td>
        <td id="LC63" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">for</span> key, value <span class="pl-k">in</span> <span class="pl-c1">list</span>(elem.attrib.items()):</td>
      </tr>
      <tr>
        <td id="L64" class="blob-num js-line-number" data-line-number="64"></td>
        <td id="LC64" class="blob-code blob-code-inner js-file-line">            d[<span class="pl-s"><span class="pl-pds">&#39;</span>@<span class="pl-pds">&#39;</span></span> <span class="pl-k">+</span> key] <span class="pl-k">=</span> value</td>
      </tr>
      <tr>
        <td id="L65" class="blob-num js-line-number" data-line-number="65"></td>
        <td id="LC65" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L66" class="blob-num js-line-number" data-line-number="66"></td>
        <td id="LC66" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"><span class="pl-c">#</span> loop over subelements to merge them</span></td>
      </tr>
      <tr>
        <td id="L67" class="blob-num js-line-number" data-line-number="67"></td>
        <td id="LC67" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">for</span> subelem <span class="pl-k">in</span> elem:</td>
      </tr>
      <tr>
        <td id="L68" class="blob-num js-line-number" data-line-number="68"></td>
        <td id="LC68" class="blob-code blob-code-inner js-file-line">        v <span class="pl-k">=</span> elem_to_internal(subelem, <span class="pl-v">strip_ns</span><span class="pl-k">=</span>strip_ns, <span class="pl-v">strip</span><span class="pl-k">=</span>strip)</td>
      </tr>
      <tr>
        <td id="L69" class="blob-num js-line-number" data-line-number="69"></td>
        <td id="LC69" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L70" class="blob-num js-line-number" data-line-number="70"></td>
        <td id="LC70" class="blob-code blob-code-inner js-file-line">        tag <span class="pl-k">=</span> subelem.tag</td>
      </tr>
      <tr>
        <td id="L71" class="blob-num js-line-number" data-line-number="71"></td>
        <td id="LC71" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> strip_ns:</td>
      </tr>
      <tr>
        <td id="L72" class="blob-num js-line-number" data-line-number="72"></td>
        <td id="LC72" class="blob-code blob-code-inner js-file-line">            tag <span class="pl-k">=</span> strip_tag(subelem.tag)</td>
      </tr>
      <tr>
        <td id="L73" class="blob-num js-line-number" data-line-number="73"></td>
        <td id="LC73" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L74" class="blob-num js-line-number" data-line-number="74"></td>
        <td id="LC74" class="blob-code blob-code-inner js-file-line">        value <span class="pl-k">=</span> v[tag]</td>
      </tr>
      <tr>
        <td id="L75" class="blob-num js-line-number" data-line-number="75"></td>
        <td id="LC75" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L76" class="blob-num js-line-number" data-line-number="76"></td>
        <td id="LC76" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L77" class="blob-num js-line-number" data-line-number="77"></td>
        <td id="LC77" class="blob-code blob-code-inner js-file-line">            <span class="pl-c"><span class="pl-c">#</span> add to existing list for this tag</span></td>
      </tr>
      <tr>
        <td id="L78" class="blob-num js-line-number" data-line-number="78"></td>
        <td id="LC78" class="blob-code blob-code-inner js-file-line">            d[tag].append(value)</td>
      </tr>
      <tr>
        <td id="L79" class="blob-num js-line-number" data-line-number="79"></td>
        <td id="LC79" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">except</span> <span class="pl-c1">AttributeError</span>:</td>
      </tr>
      <tr>
        <td id="L80" class="blob-num js-line-number" data-line-number="80"></td>
        <td id="LC80" class="blob-code blob-code-inner js-file-line">            <span class="pl-c"><span class="pl-c">#</span> turn existing entry into a list</span></td>
      </tr>
      <tr>
        <td id="L81" class="blob-num js-line-number" data-line-number="81"></td>
        <td id="LC81" class="blob-code blob-code-inner js-file-line">            d[tag] <span class="pl-k">=</span> [d[tag], value]</td>
      </tr>
      <tr>
        <td id="L82" class="blob-num js-line-number" data-line-number="82"></td>
        <td id="LC82" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">except</span> <span class="pl-c1">KeyError</span>:</td>
      </tr>
      <tr>
        <td id="L83" class="blob-num js-line-number" data-line-number="83"></td>
        <td id="LC83" class="blob-code blob-code-inner js-file-line">            <span class="pl-c"><span class="pl-c">#</span> add a new non-list entry</span></td>
      </tr>
      <tr>
        <td id="L84" class="blob-num js-line-number" data-line-number="84"></td>
        <td id="LC84" class="blob-code blob-code-inner js-file-line">            d[tag] <span class="pl-k">=</span> value</td>
      </tr>
      <tr>
        <td id="L85" class="blob-num js-line-number" data-line-number="85"></td>
        <td id="LC85" class="blob-code blob-code-inner js-file-line">    text <span class="pl-k">=</span> elem.text</td>
      </tr>
      <tr>
        <td id="L86" class="blob-num js-line-number" data-line-number="86"></td>
        <td id="LC86" class="blob-code blob-code-inner js-file-line">    tail <span class="pl-k">=</span> elem.tail</td>
      </tr>
      <tr>
        <td id="L87" class="blob-num js-line-number" data-line-number="87"></td>
        <td id="LC87" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> strip:</td>
      </tr>
      <tr>
        <td id="L88" class="blob-num js-line-number" data-line-number="88"></td>
        <td id="LC88" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> ignore leading and trailing whitespace</span></td>
      </tr>
      <tr>
        <td id="L89" class="blob-num js-line-number" data-line-number="89"></td>
        <td id="LC89" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> text:</td>
      </tr>
      <tr>
        <td id="L90" class="blob-num js-line-number" data-line-number="90"></td>
        <td id="LC90" class="blob-code blob-code-inner js-file-line">            text <span class="pl-k">=</span> text.strip()</td>
      </tr>
      <tr>
        <td id="L91" class="blob-num js-line-number" data-line-number="91"></td>
        <td id="LC91" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> tail:</td>
      </tr>
      <tr>
        <td id="L92" class="blob-num js-line-number" data-line-number="92"></td>
        <td id="LC92" class="blob-code blob-code-inner js-file-line">            tail <span class="pl-k">=</span> tail.strip()</td>
      </tr>
      <tr>
        <td id="L93" class="blob-num js-line-number" data-line-number="93"></td>
        <td id="LC93" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L94" class="blob-num js-line-number" data-line-number="94"></td>
        <td id="LC94" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> tail:</td>
      </tr>
      <tr>
        <td id="L95" class="blob-num js-line-number" data-line-number="95"></td>
        <td id="LC95" class="blob-code blob-code-inner js-file-line">        d[<span class="pl-s"><span class="pl-pds">&#39;</span>#tail<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> tail</td>
      </tr>
      <tr>
        <td id="L96" class="blob-num js-line-number" data-line-number="96"></td>
        <td id="LC96" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L97" class="blob-num js-line-number" data-line-number="97"></td>
        <td id="LC97" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> d:</td>
      </tr>
      <tr>
        <td id="L98" class="blob-num js-line-number" data-line-number="98"></td>
        <td id="LC98" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> use #text element if other attributes exist</span></td>
      </tr>
      <tr>
        <td id="L99" class="blob-num js-line-number" data-line-number="99"></td>
        <td id="LC99" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> text:</td>
      </tr>
      <tr>
        <td id="L100" class="blob-num js-line-number" data-line-number="100"></td>
        <td id="LC100" class="blob-code blob-code-inner js-file-line">            d[<span class="pl-s"><span class="pl-pds">&quot;</span>#text<span class="pl-pds">&quot;</span></span>] <span class="pl-k">=</span> text</td>
      </tr>
      <tr>
        <td id="L101" class="blob-num js-line-number" data-line-number="101"></td>
        <td id="LC101" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L102" class="blob-num js-line-number" data-line-number="102"></td>
        <td id="LC102" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> text is the value if no attributes</span></td>
      </tr>
      <tr>
        <td id="L103" class="blob-num js-line-number" data-line-number="103"></td>
        <td id="LC103" class="blob-code blob-code-inner js-file-line">        d <span class="pl-k">=</span> text <span class="pl-k">or</span> <span class="pl-c1">None</span></td>
      </tr>
      <tr>
        <td id="L104" class="blob-num js-line-number" data-line-number="104"></td>
        <td id="LC104" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">return</span> {elem_tag: d}</td>
      </tr>
      <tr>
        <td id="L105" class="blob-num js-line-number" data-line-number="105"></td>
        <td id="LC105" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L106" class="blob-num js-line-number" data-line-number="106"></td>
        <td id="LC106" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L107" class="blob-num js-line-number" data-line-number="107"></td>
        <td id="LC107" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">internal_to_elem</span>(<span class="pl-smi">pfsh</span>, <span class="pl-smi">factory</span><span class="pl-k">=</span><span class="pl-c1">ET</span>.Element):</td>
      </tr>
      <tr>
        <td id="L108" class="blob-num js-line-number" data-line-number="108"></td>
        <td id="LC108" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L109" class="blob-num js-line-number" data-line-number="109"></td>
        <td id="LC109" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span>Convert an internal dictionary (not JSON!) into an Element.</span></td>
      </tr>
      <tr>
        <td id="L110" class="blob-num js-line-number" data-line-number="110"></td>
        <td id="LC110" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L111" class="blob-num js-line-number" data-line-number="111"></td>
        <td id="LC111" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    Whatever Element implementation we could import will be</span></td>
      </tr>
      <tr>
        <td id="L112" class="blob-num js-line-number" data-line-number="112"></td>
        <td id="LC112" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    used by default; if you want to use something else, pass the</span></td>
      </tr>
      <tr>
        <td id="L113" class="blob-num js-line-number" data-line-number="113"></td>
        <td id="LC113" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    Element class as the factory parameter.</span></td>
      </tr>
      <tr>
        <td id="L114" class="blob-num js-line-number" data-line-number="114"></td>
        <td id="LC114" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    <span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L115" class="blob-num js-line-number" data-line-number="115"></td>
        <td id="LC115" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L116" class="blob-num js-line-number" data-line-number="116"></td>
        <td id="LC116" class="blob-code blob-code-inner js-file-line">    attribs <span class="pl-k">=</span> OrderedDict()</td>
      </tr>
      <tr>
        <td id="L117" class="blob-num js-line-number" data-line-number="117"></td>
        <td id="LC117" class="blob-code blob-code-inner js-file-line">    text <span class="pl-k">=</span> <span class="pl-c1">None</span></td>
      </tr>
      <tr>
        <td id="L118" class="blob-num js-line-number" data-line-number="118"></td>
        <td id="LC118" class="blob-code blob-code-inner js-file-line">    tail <span class="pl-k">=</span> <span class="pl-c1">None</span></td>
      </tr>
      <tr>
        <td id="L119" class="blob-num js-line-number" data-line-number="119"></td>
        <td id="LC119" class="blob-code blob-code-inner js-file-line">    sublist <span class="pl-k">=</span> []</td>
      </tr>
      <tr>
        <td id="L120" class="blob-num js-line-number" data-line-number="120"></td>
        <td id="LC120" class="blob-code blob-code-inner js-file-line">    tag <span class="pl-k">=</span> <span class="pl-c1">list</span>(pfsh.keys())</td>
      </tr>
      <tr>
        <td id="L121" class="blob-num js-line-number" data-line-number="121"></td>
        <td id="LC121" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> <span class="pl-c1">len</span>(tag) <span class="pl-k">!=</span> <span class="pl-c1">1</span>:</td>
      </tr>
      <tr>
        <td id="L122" class="blob-num js-line-number" data-line-number="122"></td>
        <td id="LC122" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">raise</span> <span class="pl-c1">ValueError</span>(<span class="pl-s"><span class="pl-pds">&quot;</span>Illegal structure with multiple tags: <span class="pl-c1">%s</span><span class="pl-pds">&quot;</span></span> <span class="pl-k">%</span> tag)</td>
      </tr>
      <tr>
        <td id="L123" class="blob-num js-line-number" data-line-number="123"></td>
        <td id="LC123" class="blob-code blob-code-inner js-file-line">    tag <span class="pl-k">=</span> tag[<span class="pl-c1">0</span>]</td>
      </tr>
      <tr>
        <td id="L124" class="blob-num js-line-number" data-line-number="124"></td>
        <td id="LC124" class="blob-code blob-code-inner js-file-line">    value <span class="pl-k">=</span> pfsh[tag]</td>
      </tr>
      <tr>
        <td id="L125" class="blob-num js-line-number" data-line-number="125"></td>
        <td id="LC125" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> <span class="pl-c1">isinstance</span>(value, <span class="pl-c1">dict</span>):</td>
      </tr>
      <tr>
        <td id="L126" class="blob-num js-line-number" data-line-number="126"></td>
        <td id="LC126" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">for</span> k, v <span class="pl-k">in</span> <span class="pl-c1">list</span>(value.items()):</td>
      </tr>
      <tr>
        <td id="L127" class="blob-num js-line-number" data-line-number="127"></td>
        <td id="LC127" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> k[:<span class="pl-c1">1</span>] <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&quot;</span>@<span class="pl-pds">&quot;</span></span>:</td>
      </tr>
      <tr>
        <td id="L128" class="blob-num js-line-number" data-line-number="128"></td>
        <td id="LC128" class="blob-code blob-code-inner js-file-line">                attribs[k[<span class="pl-c1">1</span>:]] <span class="pl-k">=</span> v</td>
      </tr>
      <tr>
        <td id="L129" class="blob-num js-line-number" data-line-number="129"></td>
        <td id="LC129" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">elif</span> k <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&quot;</span>#text<span class="pl-pds">&quot;</span></span>:</td>
      </tr>
      <tr>
        <td id="L130" class="blob-num js-line-number" data-line-number="130"></td>
        <td id="LC130" class="blob-code blob-code-inner js-file-line">                text <span class="pl-k">=</span> v</td>
      </tr>
      <tr>
        <td id="L131" class="blob-num js-line-number" data-line-number="131"></td>
        <td id="LC131" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">elif</span> k <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&quot;</span>#tail<span class="pl-pds">&quot;</span></span>:</td>
      </tr>
      <tr>
        <td id="L132" class="blob-num js-line-number" data-line-number="132"></td>
        <td id="LC132" class="blob-code blob-code-inner js-file-line">                tail <span class="pl-k">=</span> v</td>
      </tr>
      <tr>
        <td id="L133" class="blob-num js-line-number" data-line-number="133"></td>
        <td id="LC133" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">elif</span> <span class="pl-c1">isinstance</span>(v, <span class="pl-c1">list</span>):</td>
      </tr>
      <tr>
        <td id="L134" class="blob-num js-line-number" data-line-number="134"></td>
        <td id="LC134" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">for</span> v2 <span class="pl-k">in</span> v:</td>
      </tr>
      <tr>
        <td id="L135" class="blob-num js-line-number" data-line-number="135"></td>
        <td id="LC135" class="blob-code blob-code-inner js-file-line">                    sublist.append(internal_to_elem({k: v2}, <span class="pl-v">factory</span><span class="pl-k">=</span>factory))</td>
      </tr>
      <tr>
        <td id="L136" class="blob-num js-line-number" data-line-number="136"></td>
        <td id="LC136" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L137" class="blob-num js-line-number" data-line-number="137"></td>
        <td id="LC137" class="blob-code blob-code-inner js-file-line">                sublist.append(internal_to_elem({k: v}, <span class="pl-v">factory</span><span class="pl-k">=</span>factory))</td>
      </tr>
      <tr>
        <td id="L138" class="blob-num js-line-number" data-line-number="138"></td>
        <td id="LC138" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L139" class="blob-num js-line-number" data-line-number="139"></td>
        <td id="LC139" class="blob-code blob-code-inner js-file-line">        text <span class="pl-k">=</span> value</td>
      </tr>
      <tr>
        <td id="L140" class="blob-num js-line-number" data-line-number="140"></td>
        <td id="LC140" class="blob-code blob-code-inner js-file-line">    e <span class="pl-k">=</span> factory(tag, attribs)</td>
      </tr>
      <tr>
        <td id="L141" class="blob-num js-line-number" data-line-number="141"></td>
        <td id="LC141" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">for</span> sub <span class="pl-k">in</span> sublist:</td>
      </tr>
      <tr>
        <td id="L142" class="blob-num js-line-number" data-line-number="142"></td>
        <td id="LC142" class="blob-code blob-code-inner js-file-line">        e.append(sub)</td>
      </tr>
      <tr>
        <td id="L143" class="blob-num js-line-number" data-line-number="143"></td>
        <td id="LC143" class="blob-code blob-code-inner js-file-line">    e.text <span class="pl-k">=</span> text</td>
      </tr>
      <tr>
        <td id="L144" class="blob-num js-line-number" data-line-number="144"></td>
        <td id="LC144" class="blob-code blob-code-inner js-file-line">    e.tail <span class="pl-k">=</span> tail</td>
      </tr>
      <tr>
        <td id="L145" class="blob-num js-line-number" data-line-number="145"></td>
        <td id="LC145" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">return</span> e</td>
      </tr>
      <tr>
        <td id="L146" class="blob-num js-line-number" data-line-number="146"></td>
        <td id="LC146" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L147" class="blob-num js-line-number" data-line-number="147"></td>
        <td id="LC147" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L148" class="blob-num js-line-number" data-line-number="148"></td>
        <td id="LC148" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">elem2json</span>(<span class="pl-smi">elem</span>, <span class="pl-smi">options</span>, <span class="pl-smi">strip_ns</span><span class="pl-k">=</span><span class="pl-c1">1</span>, <span class="pl-smi">strip</span><span class="pl-k">=</span><span class="pl-c1">1</span>):</td>
      </tr>
      <tr>
        <td id="L149" class="blob-num js-line-number" data-line-number="149"></td>
        <td id="LC149" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L150" class="blob-num js-line-number" data-line-number="150"></td>
        <td id="LC150" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span>Convert an ElementTree or Element into a JSON string.<span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L151" class="blob-num js-line-number" data-line-number="151"></td>
        <td id="LC151" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L152" class="blob-num js-line-number" data-line-number="152"></td>
        <td id="LC152" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> <span class="pl-c1">hasattr</span>(elem, <span class="pl-s"><span class="pl-pds">&#39;</span>getroot<span class="pl-pds">&#39;</span></span>):</td>
      </tr>
      <tr>
        <td id="L153" class="blob-num js-line-number" data-line-number="153"></td>
        <td id="LC153" class="blob-code blob-code-inner js-file-line">        elem <span class="pl-k">=</span> elem.getroot()</td>
      </tr>
      <tr>
        <td id="L154" class="blob-num js-line-number" data-line-number="154"></td>
        <td id="LC154" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L155" class="blob-num js-line-number" data-line-number="155"></td>
        <td id="LC155" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> options.pretty:</td>
      </tr>
      <tr>
        <td id="L156" class="blob-num js-line-number" data-line-number="156"></td>
        <td id="LC156" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">return</span> json.dumps(elem_to_internal(elem, <span class="pl-v">strip_ns</span><span class="pl-k">=</span>strip_ns, <span class="pl-v">strip</span><span class="pl-k">=</span>strip), <span class="pl-v">indent</span><span class="pl-k">=</span><span class="pl-c1">4</span>, <span class="pl-v">separators</span><span class="pl-k">=</span>(<span class="pl-s"><span class="pl-pds">&#39;</span>,<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>: <span class="pl-pds">&#39;</span></span>))</td>
      </tr>
      <tr>
        <td id="L157" class="blob-num js-line-number" data-line-number="157"></td>
        <td id="LC157" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L158" class="blob-num js-line-number" data-line-number="158"></td>
        <td id="LC158" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">return</span> json.dumps(elem_to_internal(elem, <span class="pl-v">strip_ns</span><span class="pl-k">=</span>strip_ns, <span class="pl-v">strip</span><span class="pl-k">=</span>strip))</td>
      </tr>
      <tr>
        <td id="L159" class="blob-num js-line-number" data-line-number="159"></td>
        <td id="LC159" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L160" class="blob-num js-line-number" data-line-number="160"></td>
        <td id="LC160" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L161" class="blob-num js-line-number" data-line-number="161"></td>
        <td id="LC161" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">json2elem</span>(<span class="pl-smi">json_data</span>, <span class="pl-smi">factory</span><span class="pl-k">=</span><span class="pl-c1">ET</span>.Element):</td>
      </tr>
      <tr>
        <td id="L162" class="blob-num js-line-number" data-line-number="162"></td>
        <td id="LC162" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L163" class="blob-num js-line-number" data-line-number="163"></td>
        <td id="LC163" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span>Convert a JSON string into an Element.</span></td>
      </tr>
      <tr>
        <td id="L164" class="blob-num js-line-number" data-line-number="164"></td>
        <td id="LC164" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L165" class="blob-num js-line-number" data-line-number="165"></td>
        <td id="LC165" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    Whatever Element implementation we could import will be used by</span></td>
      </tr>
      <tr>
        <td id="L166" class="blob-num js-line-number" data-line-number="166"></td>
        <td id="LC166" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    default; if you want to use something else, pass the Element class</span></td>
      </tr>
      <tr>
        <td id="L167" class="blob-num js-line-number" data-line-number="167"></td>
        <td id="LC167" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    as the factory parameter.</span></td>
      </tr>
      <tr>
        <td id="L168" class="blob-num js-line-number" data-line-number="168"></td>
        <td id="LC168" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    <span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L169" class="blob-num js-line-number" data-line-number="169"></td>
        <td id="LC169" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L170" class="blob-num js-line-number" data-line-number="170"></td>
        <td id="LC170" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">return</span> internal_to_elem(json.loads(json_data), factory)</td>
      </tr>
      <tr>
        <td id="L171" class="blob-num js-line-number" data-line-number="171"></td>
        <td id="LC171" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L172" class="blob-num js-line-number" data-line-number="172"></td>
        <td id="LC172" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L173" class="blob-num js-line-number" data-line-number="173"></td>
        <td id="LC173" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">xml2json</span>(<span class="pl-smi">xmlstring</span>, <span class="pl-smi">options</span>, <span class="pl-smi">strip_ns</span><span class="pl-k">=</span><span class="pl-c1">1</span>, <span class="pl-smi">strip</span><span class="pl-k">=</span><span class="pl-c1">1</span>):</td>
      </tr>
      <tr>
        <td id="L174" class="blob-num js-line-number" data-line-number="174"></td>
        <td id="LC174" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L175" class="blob-num js-line-number" data-line-number="175"></td>
        <td id="LC175" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span>Convert an XML string into a JSON string.<span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L176" class="blob-num js-line-number" data-line-number="176"></td>
        <td id="LC176" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L177" class="blob-num js-line-number" data-line-number="177"></td>
        <td id="LC177" class="blob-code blob-code-inner js-file-line">    elem <span class="pl-k">=</span> <span class="pl-c1">ET</span>.fromstring(xmlstring)</td>
      </tr>
      <tr>
        <td id="L178" class="blob-num js-line-number" data-line-number="178"></td>
        <td id="LC178" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">return</span> elem2json(elem, options, <span class="pl-v">strip_ns</span><span class="pl-k">=</span>strip_ns, <span class="pl-v">strip</span><span class="pl-k">=</span>strip)</td>
      </tr>
      <tr>
        <td id="L179" class="blob-num js-line-number" data-line-number="179"></td>
        <td id="LC179" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L180" class="blob-num js-line-number" data-line-number="180"></td>
        <td id="LC180" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L181" class="blob-num js-line-number" data-line-number="181"></td>
        <td id="LC181" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">json2xml</span>(<span class="pl-smi">json_data</span>, <span class="pl-smi">factory</span><span class="pl-k">=</span><span class="pl-c1">ET</span>.Element):</td>
      </tr>
      <tr>
        <td id="L182" class="blob-num js-line-number" data-line-number="182"></td>
        <td id="LC182" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L183" class="blob-num js-line-number" data-line-number="183"></td>
        <td id="LC183" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span>Convert a JSON string into an XML string.</span></td>
      </tr>
      <tr>
        <td id="L184" class="blob-num js-line-number" data-line-number="184"></td>
        <td id="LC184" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L185" class="blob-num js-line-number" data-line-number="185"></td>
        <td id="LC185" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    Whatever Element implementation we could import will be used by</span></td>
      </tr>
      <tr>
        <td id="L186" class="blob-num js-line-number" data-line-number="186"></td>
        <td id="LC186" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    default; if you want to use something else, pass the Element class</span></td>
      </tr>
      <tr>
        <td id="L187" class="blob-num js-line-number" data-line-number="187"></td>
        <td id="LC187" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    as the factory parameter.</span></td>
      </tr>
      <tr>
        <td id="L188" class="blob-num js-line-number" data-line-number="188"></td>
        <td id="LC188" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    <span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L189" class="blob-num js-line-number" data-line-number="189"></td>
        <td id="LC189" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> <span class="pl-k">not</span> <span class="pl-c1">isinstance</span>(json_data, <span class="pl-c1">dict</span>):</td>
      </tr>
      <tr>
        <td id="L190" class="blob-num js-line-number" data-line-number="190"></td>
        <td id="LC190" class="blob-code blob-code-inner js-file-line">        json_data <span class="pl-k">=</span> json.loads(json_data)</td>
      </tr>
      <tr>
        <td id="L191" class="blob-num js-line-number" data-line-number="191"></td>
        <td id="LC191" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L192" class="blob-num js-line-number" data-line-number="192"></td>
        <td id="LC192" class="blob-code blob-code-inner js-file-line">    elem <span class="pl-k">=</span> internal_to_elem(json_data, factory)</td>
      </tr>
      <tr>
        <td id="L193" class="blob-num js-line-number" data-line-number="193"></td>
        <td id="LC193" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">return</span> <span class="pl-c1">ET</span>.tostring(elem)</td>
      </tr>
      <tr>
        <td id="L194" class="blob-num js-line-number" data-line-number="194"></td>
        <td id="LC194" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L195" class="blob-num js-line-number" data-line-number="195"></td>
        <td id="LC195" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L196" class="blob-num js-line-number" data-line-number="196"></td>
        <td id="LC196" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">main</span>():</td>
      </tr>
      <tr>
        <td id="L197" class="blob-num js-line-number" data-line-number="197"></td>
        <td id="LC197" class="blob-code blob-code-inner js-file-line">    p <span class="pl-k">=</span> optparse.OptionParser(</td>
      </tr>
      <tr>
        <td id="L198" class="blob-num js-line-number" data-line-number="198"></td>
        <td id="LC198" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">description</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>Converts XML to JSON or the other way around.  Reads from standard input by default, or from file if given.<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L199" class="blob-num js-line-number" data-line-number="199"></td>
        <td id="LC199" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">prog</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>xml2json<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L200" class="blob-num js-line-number" data-line-number="200"></td>
        <td id="LC200" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">usage</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>%prog -t xml2json -o file.json [file]<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L201" class="blob-num js-line-number" data-line-number="201"></td>
        <td id="LC201" class="blob-code blob-code-inner js-file-line">    )</td>
      </tr>
      <tr>
        <td id="L202" class="blob-num js-line-number" data-line-number="202"></td>
        <td id="LC202" class="blob-code blob-code-inner js-file-line">    p.add_option(<span class="pl-s"><span class="pl-pds">&#39;</span>--type<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>-t<span class="pl-pds">&#39;</span></span>, <span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>&#39;xml2json&#39; or &#39;json2xml&#39;<span class="pl-pds">&quot;</span></span>, <span class="pl-v">default</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>xml2json<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L203" class="blob-num js-line-number" data-line-number="203"></td>
        <td id="LC203" class="blob-code blob-code-inner js-file-line">    p.add_option(<span class="pl-s"><span class="pl-pds">&#39;</span>--out<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>-o<span class="pl-pds">&#39;</span></span>, <span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Write to OUT instead of stdout<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L204" class="blob-num js-line-number" data-line-number="204"></td>
        <td id="LC204" class="blob-code blob-code-inner js-file-line">    p.add_option(</td>
      </tr>
      <tr>
        <td id="L205" class="blob-num js-line-number" data-line-number="205"></td>
        <td id="LC205" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&#39;</span>--strip_text<span class="pl-pds">&#39;</span></span>, <span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>store_true<span class="pl-pds">&quot;</span></span>,</td>
      </tr>
      <tr>
        <td id="L206" class="blob-num js-line-number" data-line-number="206"></td>
        <td id="LC206" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">dest</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>strip_text<span class="pl-pds">&quot;</span></span>, <span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Strip text for xml2json<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L207" class="blob-num js-line-number" data-line-number="207"></td>
        <td id="LC207" class="blob-code blob-code-inner js-file-line">    p.add_option(</td>
      </tr>
      <tr>
        <td id="L208" class="blob-num js-line-number" data-line-number="208"></td>
        <td id="LC208" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&#39;</span>--pretty<span class="pl-pds">&#39;</span></span>, <span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>store_true<span class="pl-pds">&quot;</span></span>,</td>
      </tr>
      <tr>
        <td id="L209" class="blob-num js-line-number" data-line-number="209"></td>
        <td id="LC209" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">dest</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>pretty<span class="pl-pds">&quot;</span></span>, <span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Format JSON output so it is easier to read<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L210" class="blob-num js-line-number" data-line-number="210"></td>
        <td id="LC210" class="blob-code blob-code-inner js-file-line">    p.add_option(</td>
      </tr>
      <tr>
        <td id="L211" class="blob-num js-line-number" data-line-number="211"></td>
        <td id="LC211" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&#39;</span>--strip_namespace<span class="pl-pds">&#39;</span></span>, <span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>store_true<span class="pl-pds">&quot;</span></span>,</td>
      </tr>
      <tr>
        <td id="L212" class="blob-num js-line-number" data-line-number="212"></td>
        <td id="LC212" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">dest</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>strip_ns<span class="pl-pds">&quot;</span></span>, <span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Strip namespace for xml2json<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L213" class="blob-num js-line-number" data-line-number="213"></td>
        <td id="LC213" class="blob-code blob-code-inner js-file-line">    p.add_option(</td>
      </tr>
      <tr>
        <td id="L214" class="blob-num js-line-number" data-line-number="214"></td>
        <td id="LC214" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&#39;</span>--strip_newlines<span class="pl-pds">&#39;</span></span>, <span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>store_true<span class="pl-pds">&quot;</span></span>,</td>
      </tr>
      <tr>
        <td id="L215" class="blob-num js-line-number" data-line-number="215"></td>
        <td id="LC215" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">dest</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>strip_nl<span class="pl-pds">&quot;</span></span>, <span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Strip newlines for xml2json<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L216" class="blob-num js-line-number" data-line-number="216"></td>
        <td id="LC216" class="blob-code blob-code-inner js-file-line">    options, arguments <span class="pl-k">=</span> p.parse_args()</td>
      </tr>
      <tr>
        <td id="L217" class="blob-num js-line-number" data-line-number="217"></td>
        <td id="LC217" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L218" class="blob-num js-line-number" data-line-number="218"></td>
        <td id="LC218" class="blob-code blob-code-inner js-file-line">    inputstream <span class="pl-k">=</span> sys.stdin</td>
      </tr>
      <tr>
        <td id="L219" class="blob-num js-line-number" data-line-number="219"></td>
        <td id="LC219" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> <span class="pl-c1">len</span>(arguments) <span class="pl-k">==</span> <span class="pl-c1">1</span>:</td>
      </tr>
      <tr>
        <td id="L220" class="blob-num js-line-number" data-line-number="220"></td>
        <td id="LC220" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L221" class="blob-num js-line-number" data-line-number="221"></td>
        <td id="LC221" class="blob-code blob-code-inner js-file-line">            inputstream <span class="pl-k">=</span> <span class="pl-c1">open</span>(arguments[<span class="pl-c1">0</span>])</td>
      </tr>
      <tr>
        <td id="L222" class="blob-num js-line-number" data-line-number="222"></td>
        <td id="LC222" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">except</span>:</td>
      </tr>
      <tr>
        <td id="L223" class="blob-num js-line-number" data-line-number="223"></td>
        <td id="LC223" class="blob-code blob-code-inner js-file-line">            sys.stderr.write(<span class="pl-s"><span class="pl-pds">&quot;</span>Problem reading &#39;<span class="pl-c1">{0}</span>&#39;<span class="pl-cce">\n</span><span class="pl-pds">&quot;</span></span>.format(arguments[<span class="pl-c1">0</span>]))</td>
      </tr>
      <tr>
        <td id="L224" class="blob-num js-line-number" data-line-number="224"></td>
        <td id="LC224" class="blob-code blob-code-inner js-file-line">            p.print_help()</td>
      </tr>
      <tr>
        <td id="L225" class="blob-num js-line-number" data-line-number="225"></td>
        <td id="LC225" class="blob-code blob-code-inner js-file-line">            sys.exit(<span class="pl-k">-</span><span class="pl-c1">1</span>)</td>
      </tr>
      <tr>
        <td id="L226" class="blob-num js-line-number" data-line-number="226"></td>
        <td id="LC226" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L227" class="blob-num js-line-number" data-line-number="227"></td>
        <td id="LC227" class="blob-code blob-code-inner js-file-line">    <span class="pl-c1">input</span> <span class="pl-k">=</span> inputstream.read()</td>
      </tr>
      <tr>
        <td id="L228" class="blob-num js-line-number" data-line-number="228"></td>
        <td id="LC228" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L229" class="blob-num js-line-number" data-line-number="229"></td>
        <td id="LC229" class="blob-code blob-code-inner js-file-line">    strip <span class="pl-k">=</span> <span class="pl-c1">0</span></td>
      </tr>
      <tr>
        <td id="L230" class="blob-num js-line-number" data-line-number="230"></td>
        <td id="LC230" class="blob-code blob-code-inner js-file-line">    strip_ns <span class="pl-k">=</span> <span class="pl-c1">0</span></td>
      </tr>
      <tr>
        <td id="L231" class="blob-num js-line-number" data-line-number="231"></td>
        <td id="LC231" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> options.strip_text:</td>
      </tr>
      <tr>
        <td id="L232" class="blob-num js-line-number" data-line-number="232"></td>
        <td id="LC232" class="blob-code blob-code-inner js-file-line">        strip <span class="pl-k">=</span> <span class="pl-c1">1</span></td>
      </tr>
      <tr>
        <td id="L233" class="blob-num js-line-number" data-line-number="233"></td>
        <td id="LC233" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> options.strip_ns:</td>
      </tr>
      <tr>
        <td id="L234" class="blob-num js-line-number" data-line-number="234"></td>
        <td id="LC234" class="blob-code blob-code-inner js-file-line">        strip_ns <span class="pl-k">=</span> <span class="pl-c1">1</span></td>
      </tr>
      <tr>
        <td id="L235" class="blob-num js-line-number" data-line-number="235"></td>
        <td id="LC235" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> options.strip_nl:</td>
      </tr>
      <tr>
        <td id="L236" class="blob-num js-line-number" data-line-number="236"></td>
        <td id="LC236" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">input</span> <span class="pl-k">=</span> <span class="pl-c1">input</span>.replace(<span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-cce">\n</span><span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-pds">&#39;</span></span>).replace(<span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-cce">\r</span><span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L237" class="blob-num js-line-number" data-line-number="237"></td>
        <td id="LC237" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> (options.type <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&quot;</span>xml2json<span class="pl-pds">&quot;</span></span>):</td>
      </tr>
      <tr>
        <td id="L238" class="blob-num js-line-number" data-line-number="238"></td>
        <td id="LC238" class="blob-code blob-code-inner js-file-line">        out <span class="pl-k">=</span> xml2json(<span class="pl-c1">input</span>, options, strip_ns, strip)</td>
      </tr>
      <tr>
        <td id="L239" class="blob-num js-line-number" data-line-number="239"></td>
        <td id="LC239" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L240" class="blob-num js-line-number" data-line-number="240"></td>
        <td id="LC240" class="blob-code blob-code-inner js-file-line">        out <span class="pl-k">=</span> json2xml(<span class="pl-c1">input</span>)</td>
      </tr>
      <tr>
        <td id="L241" class="blob-num js-line-number" data-line-number="241"></td>
        <td id="LC241" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L242" class="blob-num js-line-number" data-line-number="242"></td>
        <td id="LC242" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> (options.out):</td>
      </tr>
      <tr>
        <td id="L243" class="blob-num js-line-number" data-line-number="243"></td>
        <td id="LC243" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">file</span> <span class="pl-k">=</span> <span class="pl-c1">open</span>(options.out, <span class="pl-s"><span class="pl-pds">&#39;</span>w<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L244" class="blob-num js-line-number" data-line-number="244"></td>
        <td id="LC244" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">file</span>.write(out)</td>
      </tr>
      <tr>
        <td id="L245" class="blob-num js-line-number" data-line-number="245"></td>
        <td id="LC245" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">file</span>.close()</td>
      </tr>
      <tr>
        <td id="L246" class="blob-num js-line-number" data-line-number="246"></td>
        <td id="LC246" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L247" class="blob-num js-line-number" data-line-number="247"></td>
        <td id="LC247" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">print</span>(out)</td>
      </tr>
      <tr>
        <td id="L248" class="blob-num js-line-number" data-line-number="248"></td>
        <td id="LC248" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L249" class="blob-num js-line-number" data-line-number="249"></td>
        <td id="LC249" class="blob-code blob-code-inner js-file-line"><span class="pl-k">if</span> <span class="pl-c1">__name__</span> <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&quot;</span>__main__<span class="pl-pds">&quot;</span></span>:</td>
      </tr>
      <tr>
        <td id="L250" class="blob-num js-line-number" data-line-number="250"></td>
        <td id="LC250" class="blob-code blob-code-inner js-file-line">    main()</td>
      </tr>
      <tr>
        <td id="L251" class="blob-num js-line-number" data-line-number="251"></td>
        <td id="LC251" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
</table>
  </div>
</div>
<button type="button" data-facebox="#jump-to-line" data-facebox-class="linejump" data-hotkey="l" class="d-none">Jump to Line</button>
<div id="jump-to-line" style="display:none">
  <!-- '"` --><!-- </textarea></xmp> --></option></form><form accept-charset="UTF-8" action="" class="js-jump-to-line-form" method="get"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /></div>
    <input class="form-control linejump-input js-jump-to-line-field" type="text" placeholder="Jump to line&hellip;" aria-label="Jump to line" autofocus>
    <button type="submit" class="btn">Go</button>
</form></div>
  </div>
  <div class="modal-backdrop js-touch-events"></div>
</div>
    </div>
  </div>
  </div>
      <div class="container site-footer-container">
  <div class="site-footer" role="contentinfo">
    <ul class="site-footer-links float-right">
        <li><a href="https://github.com/contact" data-ga-click="Footer, go to contact, text:contact">Contact GitHub</a></li>
      <li><a href="https://developer.github.com" data-ga-click="Footer, go to api, text:api">API</a></li>
      <li><a href="https://training.github.com" data-ga-click="Footer, go to training, text:training">Training</a></li>
      <li><a href="https://shop.github.com" data-ga-click="Footer, go to shop, text:shop">Shop</a></li>
        <li><a href="https://github.com/blog" data-ga-click="Footer, go to blog, text:blog">Blog</a></li>
        <li><a href="https://github.com/about" data-ga-click="Footer, go to about, text:about">About</a></li>
    </ul>
    <a href="https://github.com" aria-label="Homepage" class="site-footer-mark" title="GitHub">
      <svg aria-hidden="true" class="octicon octicon-mark-github" height="24" version="1.1" viewBox="0 0 16 16" width="24"><path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z"/></svg>
</a>
    <ul class="site-footer-links">
      <li>&copy; 2017 <span title="0.06174s from github-fe-134ed95.cp1-iad.github.net">GitHub</span>, Inc.</li>
        <li><a href="https://github.com/site/terms" data-ga-click="Footer, go to terms, text:terms">Terms</a></li>
        <li><a href="https://github.com/site/privacy" data-ga-click="Footer, go to privacy, text:privacy">Privacy</a></li>
        <li><a href="https://github.com/security" data-ga-click="Footer, go to security, text:security">Security</a></li>
        <li><a href="https://status.github.com/" data-ga-click="Footer, go to status, text:status">Status</a></li>
        <li><a href="https://help.github.com" data-ga-click="Footer, go to help, text:help">Help</a></li>
    </ul>
  </div>
</div>
  
  <div id="ajax-error-message" class="ajax-error-message flash flash-error">
    <svg aria-hidden="true" class="octicon octicon-alert" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M8.865 1.52c-.18-.31-.51-.5-.87-.5s-.69.19-.87.5L.275 13.5c-.18.31-.18.69 0 1 .19.31.52.5.87.5h13.7c.36 0 .69-.19.86-.5.17-.31.18-.69.01-1L8.865 1.52zM8.995 13h-2v-2h2v2zm0-3h-2V6h2v4z"/></svg>
    <button type="button" class="flash-close js-flash-close js-ajax-error-dismiss" aria-label="Dismiss error">
      <svg aria-hidden="true" class="octicon octicon-x" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48z"/></svg>
    </button>
    You can't perform that action at this time.
  </div>
    <script crossorigin="anonymous" src="https://assets-cdn.github.com/assets/compat-8a4318ffea09a0cdb8214b76cf2926b9f6a0ced318a317bed419db19214c690d.js"></script>
    <script crossorigin="anonymous" src="https://assets-cdn.github.com/assets/frameworks-6d109e75ad8471ba415082726c00c35fb929ceab975082492835f11eca8c07d9.js"></script>
    <script async="async" crossorigin="anonymous" src="https://assets-cdn.github.com/assets/github-cd1f7c97279e009c44357eb19c6bccc6b634a442001c0c5e1a368177c209bf6a.js"></script>
    
    
    
    
  <div class="js-stale-session-flash stale-session-flash flash flash-warn flash-banner d-none">
    <svg aria-hidden="true" class="octicon octicon-alert" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M8.865 1.52c-.18-.31-.51-.5-.87-.5s-.69.19-.87.5L.275 13.5c-.18.31-.18.69 0 1 .19.31.52.5.87.5h13.7c.36 0 .69-.19.86-.5.17-.31.18-.69.01-1L8.865 1.52zM8.995 13h-2v-2h2v2zm0-3h-2V6h2v4z"/></svg>
    <span class="signed-in-tab-flash">You signed in with another tab or window. <a href="">Reload</a> to refresh your session.</span>
    <span class="signed-out-tab-flash">You signed out in another tab or window. <a href="">Reload</a> to refresh your session.</span>
  </div>
  <div class="facebox" id="facebox" style="display:none;">
  <div class="facebox-popup">
    <div class="facebox-content" role="dialog" aria-labelledby="facebox-header" aria-describedby="facebox-description">
    </div>
    <button type="button" class="facebox-close js-facebox-close" aria-label="Close modal">
      <svg aria-hidden="true" class="octicon octicon-x" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48z"/></svg>
    </button>
  </div>
</div>
  </body>
</html>
#!/bin/sh
# chevronRemove.sh
# see name for details
DELIM="<" # default delimter
stripSpace="true"
# parse arguments
while [ $# -gt 0 ]; do
	case $1 in
		-h)	cat << "EOF"
Usage: chevronRemove.sh
  -d DELIM    Use this as the comment delimiter.
EOF
			exit 1	;;
		-d)	DELIM="$2" # store desired delimiter
	esac
	shift
done
sed -E 's|<[^>]*>||g' # remove chevrons
exit 0;
