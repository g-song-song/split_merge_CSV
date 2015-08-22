# -*- coding: UTF-8 -*-

import csv

def csvwrite(fname, row):
	with open(fname, 'a') as wfile:
		csvwriter = csv.writer(wfile)
		csvwriter.writerow(row)

