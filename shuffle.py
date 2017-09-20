#!/usr/bin/env python2.7

import sys
from random import shuffle

x = []

for line in sys.stdin:
	x.append(line)

shuffle(x)

print ''.join(x)
