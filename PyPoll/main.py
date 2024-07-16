import os
import csv
from operator import itemgetter                             # gain more knowledge on importing modules such as this

# Set the path for the csv file
desired_path = 'Resources'

# Change the current working directory to the desired path
os.chdir(desired_path)

# Get the current working directory
path = os.getcwd()

# Set file_path variable storing the file.
file_path = os.path.join(path, 'election_data.csv')

# Initiating variables
ballots = 0
charles_votes = 0
diana_votes = 0
raymon_votes = 0

# Defining Candidate dictionary 
candidate_votes = {
  "Charles Casper Stockham": charles_votes,
  "Diana DeGette": diana_votes,
  "Raymon Anthony Doane": raymon_votes
}

# Reading csvfile using importing csv module.
with open(file_path) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
   
    # Read the header row first and store it into csv_header variable
    csv_header = next(csvreader)
    
    # Read each row of data after the header
    for row in csvreader:
        ballots += 1

        if row[2] == "Charles Casper Stockham":
            charles_votes +=1                       # Counter for Charles Votes

        elif row[2] == "Diana DeGette":
            diana_votes +=1                         # Counter for Diana Votes
            
    
        elif row[2] == "Raymon Anthony Doane":
            raymon_votes +=1                        # Counter for Raymon Votes


        winner = max(candidate_votes, key=itemgetter(1))        # got this from StackOverflow -- https://stackoverflow.com/questions/268272/getting-key-with-maximum-value-in-dictionary

# Print Statements
    print (f'Election Results')
    print ('-------------------------')
    print (f'Total Votes: {ballots}')
    print ('-------------------------')
    print (f'Charles Casper Stockham: {charles_votes/ballots:.3%} ({charles_votes})')
    print (f'Diana DeGette: {diana_votes/ballots:.3%} ({diana_votes})')
    print (f'Raymon Anthony Doane: {raymon_votes/ballots:.3%} ({raymon_votes})')
    print ('-------------------------')
    print (f'Winner: {winner}')
    print ('-------------------------')


# Writing the output to the file
desired_output_path = '../analysis'                     # setting up the desired path as one folder up from cwd and then analysis folder.
os.chdir(desired_output_path)
path = os.getcwd()
output_file_path = os.path.join(path, 'analysis.txt')


with open(output_file_path, "w") as txt_file:              # opening the file as txt_file and giving it the write access.
    
    # Write methods to print the Analysis Summary
    txt_file.write (f'Election Results\n')
    txt_file.write ('-------------------------\n')
    txt_file.write (f'Total Votes: {ballots}\n')
    txt_file.write ('-------------------------\n')
    txt_file.write (f'Charles Casper Stockham: {charles_votes/ballots:.3%} ({charles_votes})\n')
    txt_file.write (f'Diana DeGette: {diana_votes/ballots:.3%} ({diana_votes})\n')
    txt_file.write (f'Raymon Anthony Doane: {raymon_votes/ballots:.3%} ({raymon_votes})\n')
    txt_file.write ('-------------------------\n')
    txt_file.write (f'Winner: {winner}\n')
    txt_file.write ('-------------------------\n')