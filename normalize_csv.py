#!/usr/bin/env python

import sys
import csv
from datetime import datetime, timedelta

#Please note there are commas in the Address
  #field; your CSV parsing will need to take that into account. Commas
  #will only be present inside a quoted string.
def main():
	filename = sys.argv[1]
	f = open(filename, 'r')
	fieldnames = ['Timestamp', 'Address', 'ZIP', 'FullName', 'FooDuration', 'BarDuration', 'TotalDuration', 'Notes']
	csv_contents = csv.DictReader(f, quotechar='"', delimiter=',', quoting=csv.QUOTE_ALL)
	data = list(csv_contents)

	output_filename = filename.split(".")
	output_filename = output_filename[0] + "output." + output_filename[1]
	out_f = open(output_filename, 'w')
	writer = csv.DictWriter(out_f, fieldnames=fieldnames)
	parse_contents(data, writer)


def parse_contents(data, writer):
	for row in data:
		#Initialize duration as not updated, we only want to handle once
		updatedDuration = False
		try:
			for (name, value) in row.items():
				value = value.decode("utf-8", "replace")


				#Check for simple functions to run
				fn = None
				if name == 'Timestamp':
					fn = format_timestamp
				elif name == 'ZIP':
					fn = format_zipcode
				elif name == 'FullName':
					fn = format_name

				#If duration, handle all at once, otherwise run fn
				result = value
				if name.endswith("Duration"):
					if updatedDuration:
						continue
					result = update_duration(
						row['FooDuration'],
						row['BarDuration'],
						row['TotalDuration']
					)
					row['FooDuration'] = result[0]
					row['BarDuration'] = result[1]
					row['TotalDuration'] = result[2]
					#Flag the duration as updated
					updatedDuration = True
				else:
					if fn != None:
						result = fn(value)
					row[name] = result

			writer.writerow(row)
		except UnicodeEncodeError:
			sys.stderr.write("Warning: Row dropped because of invalid characters," +
				"unparseable\n")

		
def format_timestamp(ts):
	ts_as_date_et = datetime.strptime(ts, "%m/%d/%y %H:%M:%S %p")
	ts_as_date_pt = ts_as_date_et - timedelta(hours=3)
	return datetime.strftime(ts_as_date_pt, "%m/%d/%y %H:%M:%S %p")

def format_zipcode(z):
	if (len(z) < 5):
		missing = 5 - len(z)
		z = "0"*missing + z
	return z

def format_name(name):
	return name.upper()

def update_duration(foo, bar, total):
	total = calc_total_duration(foo, bar)
	return [foo, bar, total]

def calc_total_duration(foo, bar):
	foo = time_to_array(foo)
	bar = time_to_array(bar)
	result = list()
	for i in range(len(foo)):
		result.append(int(foo[i]) + int(bar[i]))
	result_string =""
	for i in range(len(result)):
		result_string += str(result[i])
		if i < 2:
			result_string += ":"
		elif i == 2:
			result_string += "."

	return result_string

def time_to_array(str):
	rest, mill = str.split(".")
	rest = rest.split(":")
	rest.append(mill)
	return rest



if __name__ == "__main__":
	main()
