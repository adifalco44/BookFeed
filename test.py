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

