#!/usr/bin/env python

import sys
import csv

#Please note there are commas in the Address
  #field; your CSV parsing will need to take that into account. Commas
  #will only be present inside a quoted string.
def main():
	filename = sys.argv[1]
	f = open(filename, 'r')
	csv_contents = csv.reader(f, quotechar='"', delimiter=',', quoting=csv.QUOTE_ALL)
	data = list(csv_contents)
	for row in data:
		print row
		
def format_timestamp():
	return
	#The Timestamp column should be formatted in ISO-8601 format.
	#date.isoformat()
	#The Timestamp column should be assumed to be in US/Pacific time;
  	#please convert it to US/Eastern.
  	#date_str = "2009-05-05 22:28:15"
#datetime_obj = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
#datetime_obj_utc = datetime_obj.replace(tzinfo=timezone('UTC'))
#datetime_obj_utc.astimezone(timezone('US/Pacific'))
  	

def format_zipcode():
	return
	#All ZIP codes should be formatted as 5 digits. If there are less
  #than 5 digits, assume 0 as the prefix.

def format_name():
	return
	#All name columns should be converted to uppercase. There will be
  #non-English names.

def format_address():
	return
	#The Address column should be passed through as is, except for
  #Unicode validation. 




if __name__ == "__main__":
	main()
