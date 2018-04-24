#!/usr/bin/env python2.7

import sys

nospace = [line for line in sys.stdin if line.strip() != '']

print ''.join(nospace)
