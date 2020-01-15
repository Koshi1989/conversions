#!/usr/bin/env python3

import csv
import datetime

# 1. load input.csv into a variable `rows`

with open('input.csv') as f:
	reader = csv.DictReader(f)
	rows = list (reader)

# 2. open output.csv and create a `csv.writer`
with open('output.csv', 'w') as f:
	writer = csv.writer(f)

# 3. write csv header with columns: "date" and "close"
	writer.writerow(['date', 'close'])

# (use https://strftime.org/ to create the input/output date formats for the next two steps)
	INPUT_DATE_FORMAT = "%m/%d/%Y"
	OUTPUT_DATE_FORMAT = "%-d-%b-%y"

# for each row

	for row in rows:

    # 4. parse raw `enddate`: you can parse the `enddate` column using the datetime.datetime.strptime function
    # hint: datetime.datetime.strptime(myrawstring, "insert input format here")
		parsed_date = datetime.datetime.strptime(row['enddate'], INPUT_DATE_FORMAT)

# 5. convert the `enddate` datetime to the desired output date format by looking at dummy.csv
# hint: mydateobject.strftime("insert output format here")
		convert_date = parsed_date.strftime(OUTPUT_DATE_FORMAT)

    # 6. write the transformed date and "approve" value to the csv
		writer.writerow([convert_date, row["approve"]])
