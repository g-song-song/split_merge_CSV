#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import csv
import os

import csvwrite

def split(src, body, head = 0, tail = 0):
	with open(src, 'rU') as csvfile:
		fname = os.path.splitext(src)[0]
		reader = csv.reader(csvfile)

		for row in reader:
			if head > 0:
				csvwrite.csvwrite(fname + '_head.csv', row[0:head])

			nbody = int( (len(row) - head - tail) / float(body) + 0.5 )
			for n in range(nbody):
				c1 = body * n + head
				c2 = min(c1 + body, len(row) - tail)
				csvwrite.csvwrite(fname + '_' + str(n) + '.csv', row[c1:c2])

			if tail > 0:
				csvwrite.csvwrite(fname + '_tail.csv', row[-tail:])

if __name__ == "__main__":
	import sys

	argc = len(sys.argv)
	if not (3 <= argc <= 5):
		print("Usage")
		print("	[python3] ./split.py src body [head [tail]]")
		sys.exit()

	src = sys.argv[1]
	body = int(sys.argv[2])
	head = 0
	tail = 0
	if argc >= 4:
		head = int(sys.argv[3])
	if argc == 5:
		tail = int(sys.argv[4])

	if not os.path.isfile(src):
		print("CSV file",  src, "does not exist. Exit.")
		sys.exit()

	split(src, body, head, tail)

