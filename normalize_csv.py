#!/usr/bin/env python

import sys
import csv

def main():
	filename = sys.argv[1]
	f = open(filename, 'r')
	csv_contents = csv.reader(f)
	data = list(csv_contents)
	for row in data:
		print ', '.join(row)

if __name__ == "__main__":
	main()
