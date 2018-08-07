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
	csv_contents = csv.DictReader(f, quotechar='"', delimiter=',', quoting=csv.QUOTE_ALL)
	data = list(csv_contents)
	for row in data:
		for (name, value) in row.items():
			value = value.decode("utf-8", "replace")
			#will add try statement here
			result = execute_validation_fns(name, value)
			row[name] = result
			
		print row
			


def execute_validation_fns(header, value):
	names_to_fns = {
		'Timestamp': format_timestamp,
		'Address': format_address,
		'ZIP': format_zipcode,
		'FullName': format_name,
		'FooDuration': format_duration,
		'BarDuration': format_duration,
		'TotalDuration': update_total_duration,
		'Note': noop #this won't work, need a fn
	}
	fn = names_to_fns.get(header, noop)
	return fn(value)
		
def format_timestamp(ts):
	ts_as_date_et = datetime.strptime(ts, "%m/%d/%y %H:%M:%S %p")
	ts_as_date_pt = ts_as_date_et - timedelta(hours=3)

	return datetime.strftime(ts_as_date_pt, "%m/%d/%y %H:%M:%S %p")
  	
def format_zipcode(z):
	if (len(z) < 5):
		missing = 5 - len(z)
		z = "0"*missing + z
	return z
	#All ZIP codes should be formatted as 5 digits. If there are less
  #than 5 digits, assume 0 as the prefix.

def format_name(name):
	return
	#All name columns should be converted to uppercase. There will be
  #non-English names.

def format_address(addr):
	return
	#The Address column should be passed through as is, except for
  #Unicode validation. 

def format_duration(dur):
	return
#The columns `FooDuration` and `BarDuration` are in HH:MM:SS.MS
  #format (where MS is milliseconds); please convert them to a floating
  #point seconds format.

def update_total_duration(dur):
	return
	#The column "TotalDuration" is filled with garbage data. For each
 # row, please replace the value of TotalDuration with the sum of
  #FooDuration and BarDuration.

def noop(rep):
	return
	#"a\x81b".decode("utf-8", "replace")
	#The column "Notes" is free form text input by end-users; please do
  #not perform any transformations on this column. If there are invalid
  #UTF-8 characters, please replace them with the Unicode Replacement
  #Character.



if __name__ == "__main__":
	main()
