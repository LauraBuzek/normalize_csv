#!/usr/bin/env python

import sys
import csv

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
			#result = execute_validation_fns(name, value)
			value = value.encode('utf-8')
			row[name] = value
			
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
		'Note': unicode_replacement #this won't work
	}

	fn = names_to_fns.get(header, "Invalid header")
	return fn(value)
		
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

def format_duration():
	return
#The columns `FooDuration` and `BarDuration` are in HH:MM:SS.MS
  #format (where MS is milliseconds); please convert them to a floating
  #point seconds format.

def update_total_duration():
	return
	#The column "TotalDuration" is filled with garbage data. For each
 # row, please replace the value of TotalDuration with the sum of
  #FooDuration and BarDuration.

def unicode_replacement():
	return
	#"a\x81b".decode("utf-8", "replace")
	#The column "Notes" is free form text input by end-users; please do
  #not perform any transformations on this column. If there are invalid
  #UTF-8 characters, please replace them with the Unicode Replacement
  #Character.



if __name__ == "__main__":
	main()
