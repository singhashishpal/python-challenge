import os
import csv

# Set the path for the csv file
desired_path = 'Resources'

# Change the current working directory to the desired path
os.chdir(desired_path)

# Get the current working directory
path = os.getcwd()

# Set file_path variable storing the file.
file_path = os.path.join(path, 'budget_data.csv')

# print(file_path)
counter = 0

# Reading csvfile using importing csv module.
with open(file_path) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # print(csvreader)
    # print ("+++++++++++++++++++++++++++++++++++++")
    
    
    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")
    # print ("---------------------------------")
    
    # Read each row of data after the header
    for row in csvreader:
        counter += 1
        # print(row[0])
        # rows_dict = {index: column for index, column in enumerate(row)}
        # print (rows_dict)
    print (counter)
    
    
''' OLD FILE 

import os

# Module for reading CSV files
import csv

csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

# # Method 1: Plain Reading of CSV files
# with open(csvpath, 'r') as file_handler:
#     lines = file_handler.read()
#     print(lines)
#     print(type(lines))


# Method 2: Improved Reading using CSV module

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        print(row)

'''