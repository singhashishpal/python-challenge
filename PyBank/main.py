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

# initialising the counter for counting the total number of months
counter = 0
sum_of_pl = 0   # initializing the sum of profit and loss variable and declaring it as int.

# Reading csvfile using importing csv module.
with open(file_path) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
   
    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    
    # Read each row of data after the header
    for row in csvreader:
        profit_loss = (row[1])
        date_of_pl = (row[0])
        counter += 1
        sum_of_pl = (int(profit_loss) + sum_of_pl)
        next_value = (row[1])
        # diff_of_pl = (int(next_value) - (int(profit_loss)))
        # average_of_pl = (diff_of_pl/counter)

    print ("Financial Analysis")
    print ("----------------------------")
    print (f'Total Months: {counter}') # This will print the total number of months
    print (f'Total: ${sum_of_pl}') # This will print the sum of the total profit or loss
    # print (f'Average: ${average_of_pl}')
    print (date_of_pl)
    print (profit_loss)
    print (next_value)

