#!/bin/env python

import sys

def add(a,b):
	summ = a + b
	print (summ)
try:
	a = int(sys.argv[1])
	b = int(sys.argv[2])
except IndexError:
	print("Incorrect number of arguments!")
	sys.exit(0)


if len(sys.argv) != 3:
		
	print("Incorrect number of arguments!")
	sys.exit(0)

add(a,b)

