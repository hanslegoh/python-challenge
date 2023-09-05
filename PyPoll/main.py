import os
import csv

# Initialize variables to 0 or a list
TotalVotes = 0
CCS_Votes = 0
DD_Votes = 0
RAD_Votes = 0

# Set path to csv file
election_csv = os.path.join("..\..", "PyPoll", "Resources", "election_data.csv")

# Open the csv file
with open(election_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_file).strip().split(sep=',')

    # Loop through all the rows in the csv file
    for row in csv_reader:
        TotalVotes += 1
        
        # Count the vote for the respective candidate
        if row[2] == "Charles Casper Stockham":
            CCS_Votes += 1
        elif row[2] == "Diana DeGette":
            DD_Votes += 1
        elif row[2] == "Raymon Anthony Doane":
            RAD_Votes += 1
    
    # Calculate the percentage of votes for each candidate
    CCS_percent = round((CCS_Votes / TotalVotes) * 100, 3)
    DD_percent = round((DD_Votes / TotalVotes) * 100, 3)
    RAD_percent = round((RAD_Votes / TotalVotes) * 100, 3)

    # Determine the winning candidate
    MaxVotes = max(CCS_Votes,DD_Votes,RAD_Votes)
    if MaxVotes == CCS_Votes:
        Winner = "Charles Casper Stockham"
    elif MaxVotes == DD_Votes:
        Winner = "Diana DeGette"
    elif MaxVotes == RAD_Votes:
        Winner = "Raymon Anthony Doane"
    
    # Summarize the results
    ResultTable = ['Election Results'
                    ,' '
                    ,'----------------------------------'
                    ,' '
                    ,f'Total Votes: {TotalVotes}'
                    ,' '
                    ,'----------------------------------'
                    ,' '
                    ,f'Charles Casper Stockham: {CCS_percent}% ({CCS_Votes})'
                    ,' '
                    ,f'Diana DeGette: {DD_percent}% ({DD_Votes})'
                    ,' '
                    ,f'Raymon Anthony Doane: {RAD_percent}% ({RAD_Votes})'
                    ,' '
                    ,'----------------------------------'
                    ,' '
                    ,f'Winner: {Winner}'
                    ,' '
                    ,'----------------------------------']

    print(*ResultTable, sep="\n")

# Define a function to convert a list into a list of lists
def listoflists(list):
        res = []
        for element in list:
            sub = element.split(', ')
            res.append(sub)
        return(res)

# Create the export text file
export_file = os.path.join("analysis", "Election Results.txt")

# Open the txt file
with open(export_file, 'w', newline='') as ResultFile:
    txtwrite = csv.writer(ResultFile)

    # Write the summarized results to the txt file
    txtwrite.writerows(listoflists(ResultTable))

