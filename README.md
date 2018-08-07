# Use this script to normalize your CSV
First, ensure you're running on MacOS and that you have Python 2.7 installed.

1.Clone the git repository

2.Run the program by calling:
`python normalize_csv.py <your_csv_path/your_csv_name.csv>`
 * Your csv will need to have the following column names:
 
   * 'Timestamp', 'Address', 'ZIP', 'FullName', 'FooDuration', 'BarDuration', 'TotalDuration', 'Notes'
  
3.Your results file will end up in the same directory as your csv under
the filename `<your_csv_path/your_csv_name>output.csv`

Rows will have been removed if they are found to include characters unrecognized by UTF-8 encoding. Sorry about that!
