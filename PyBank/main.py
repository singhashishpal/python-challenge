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

# initialising the variables
total_months = 0        # counter for counting the total number of months
sum_of_pl = 0           # initializing the sum of profit and loss variable and declaring it as int.
previous_pl = 0
greatest_pl_change = 0
smallest_pl_change = 0
pl_changes = []         # Profit/Loss list to store the P/L Changes.

# Reading csvfile using importing csv module.
with open(file_path) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
   
    # Read the header row first and store it into csv_header variable
    csv_header = next(csvreader)
    
    # Read each row of data after the header
    for row in csvreader:
        total_months += 1
        current_pl = int(row[1])
        sum_of_pl += current_pl

        if total_months > 1:
            pl_change = int(current_pl - previous_pl)
            pl_changes.append(pl_change)
            
            # Finding Greatest Profit/Loss Change 
            if pl_change > greatest_pl_change:
                greatest_pl_change = pl_change
                date_of_greatest_inc = row[0]   # This will store date of Greatest Increase in Profits
            
            if pl_change < smallest_pl_change:
                smallest_pl_change = pl_change
                date_of_greatest_dec = row[0]   # This will store date of Greatest Decrease in Profits

        previous_pl = current_pl


    # Calculate the average change in profit/loss
    average_change = sum(pl_changes) / len(pl_changes)

    # Printing the required outputs:
    print ("Financial Analysis")
    print ("----------------------------")
    print (f'Total Months: {total_months}')                                 # This will print the total number of months
    print (f'Total: ${sum_of_pl}')                                          # This will print the sum of the total profit or loss
    print (f'Average Change: ${average_change:.2f}')                        
    print (f'Greatest Increase in Profits: {date_of_greatest_inc} (${greatest_pl_change})')
    print (f'Greatest Decrease in Profits: {date_of_greatest_dec} (${smallest_pl_change})')


# Writing the output to the file
desired_output_path = '../Analysis'                     # setting up the desired path as one folder up from cwd and then analysis folder.
os.chdir(desired_output_path)
path = os.getcwd()
output_file_path = os.path.join(path, 'analysis.txt')


with open(output_file_path, "w") as txt_file:              # opening the file as txt_file and giving it the write access.
    
    # Write methods to print the Analysis Summary
    txt_file.write('Financial Analysis\n')
    txt_file.write('----------------------------\n')
    txt_file.write(f'Total Months: {total_months}\n')
    txt_file.write(f'Total: ${sum_of_pl}\n')
    txt_file.write(f'Average Change: ${average_change:.2f}\n')
    txt_file.write(f'Greatest Increase in Profits: {date_of_greatest_inc} (${greatest_pl_change})\n')
    txt_file.write(f'Greatest Decrease in Profits: {date_of_greatest_dec} (${smallest_pl_change})\n')