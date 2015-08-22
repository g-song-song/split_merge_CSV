#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import csv
import os

import csvwrite

def merge(src1, src2, dest):
	with open(src1, 'rU') as f1, open(src2, 'rU') as f2:
		reader1 = csv.reader(f1)
		reader2 = csv.reader(f2)

		for row1 in reader1:
			row2 = next(reader2)
			row = row1 + row2
			csvwrite.csvwrite(dest, row)

if __name__ == "__main__":
	import sys

	argc = len(sys.argv)
	if not argc == 4:
		print("Usage")
		print("	[python3] ./merge.py src1 src2 dest")

	src1 = sys.argv[1]
	src2 = sys.argv[2]
	dest = sys.argv[3]
	dirname = os.path.dirname(os.path.abspath(dest))

	if not os.path.isfile(src1):
		print("CSV file", src1, "does not exist. Exit.")
		sys.exit()
	if not os.path.isfile(src2):
		print("CSV file", src2, "does not exist. Exit.")
		sys.exit()
	if not os.path.isdir(dirname):
		print("Directory", dirname, "does not exists. Exit.")
		sys.exit()
	if os.path.exists(dest):
		print("Destination file", dest, "already exists. Exit.")
		sys.exit()

	merge(src1, src2, dest)

