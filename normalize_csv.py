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
		#Initialize duration as not updated, we only want to handle once
		updatedDuration = False
		for (name, value) in row.items():
			value = value.decode("utf-8", "replace")
			#TODO: will add try statement here
			
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
			if name.endswith("Duration") and not updatedDuration:
				#run the duration function
				result = update_duration(value)
				#Flag the duration as updated
				updatedDuration = True
			elif fn != None:
				result = fn(value)

			row[name] = result
			
		#TODO: will remove
		print row
			

		
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

def update_duration(dur):
	#TODO: implement
	return dur
	#The column "TotalDuration" is filled with garbage data. For each
 # row, please replace the value of TotalDuration with the sum of
  #FooDuration and BarDuration.


	#"a\x81b".decode("utf-8", "replace")
	#The column "Notes" is free form text input by end-users; please do
  #not perform any transformations on this column. If there are invalid
  #UTF-8 characters, please replace them with the Unicode Replacement
  #Character.



if __name__ == "__main__":
	main()
