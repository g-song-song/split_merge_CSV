#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import csv
import os

import csvwrite

def merge(src, dest):
	f = []
	r = []
	for i in range(len(src)):
		f += [open(src[i], 'rU')]
		r += [csv.reader(f[i])]

	while (True):
		row = []
		reachEnd = False
		for r_ in r:
			try:
				row += next(r_)
			except:
				reachEnd = True
				break
		else:
			csvwrite.csvwrite(dest, row)

		if reachEnd == True:
			break

if __name__ == "__main__":
	import sys

	argc = len(sys.argv)
	if argc < 4:
		print("Usage")
		print("	[python3] ./merge.py src1 ... srcN dest")
		sys.exit()

	src = sys.argv[1:-1]
	dest = sys.argv[-1]
	dirname = os.path.dirname(os.path.abspath(dest))

	for s in src:
		if not os.path.isfile(s):
			print("CSV file", s, "does not exist. Exit.")
			sys.exit()
	if not os.path.isdir(dirname):
		print("Directory", dirname, "does not exists. Exit.")
		sys.exit()
	if os.path.exists(dest):
		print("Destination file", dest, "already exists. Exit.")
		sys.exit()

	merge(src, dest)

