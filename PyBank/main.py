import os
import csv

# Initialize variables to 0 or a list
PL = 0
MonthCount = 0
TotalPL = 0
ChangePL = 0
list_ChangePL = []
PrevPL = 0
IncreaseDate = 0
GreatestInProfits = 0
DecreaseDate = 0
GreatestDeProfits = 0

# Set path to csv file
budget_csv = os.path.join("..\..", "PyBank", "Resources", "budget_data.csv")

# Open the csv file
with open(budget_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_file).strip().split(sep=',')

    # Loop through all the rows in the csv file
    for row in csv_reader:
        PL = int(row[1])
        MonthCount += 1
        TotalPL += PL
        
        # Check for previous profit/loss value to calculate the change
        if PrevPL != 0:
            ChangePL = PL - PrevPL
            list_ChangePL.append(ChangePL)

        # Set the previous profit/loss value as the current profit/loss value to use for the next loop
        PrevPL = PL

        # Check and store the greatest increase in profits
        if GreatestInProfits < ChangePL:
            IncreaseDate = row[0]
            GreatestInProfits = ChangePL
        # Check and store the greatest decrease in profits
        elif GreatestDeProfits > ChangePL:
            DecreaseDate = row[0]
            GreatestDeProfits = ChangePL
        # Might not be necessary for this data, but the greatest values will not change if the ChangePL value is equal to it
        else:
            continue
    
    # Calculate the average change by summing the list and dividing  by one less than the number of months
    AverageChange = round((sum(list_ChangePL)) / (MonthCount - 1), 2)

    # Summarize the results
    ResultTable = ['Financial Analysis'
                    ,'----------------------------------'
                    ,f'Total Months: {MonthCount}'
                    ,f'Total: ${TotalPL}'
                    ,f'Average Change: ${AverageChange}'
                    ,f'Greatest Increase in Profits: {IncreaseDate} (${GreatestInProfits})'
                    ,f'Greatest Decrease in Profits: {DecreaseDate} (${GreatestDeProfits})']

    print(*ResultTable, sep="\n")

# Define a function to convert a list into a list of lists
def listoflists(list):
        res = []
        for element in list:
            sub = element.split(', ')
            res.append(sub)
        return(res)

# Create the export text file
export_file = os.path.join("analysis", "Financial Analysis.txt")

# Open the txt file
with open(export_file, 'w', newline='') as ResultFile:
    txtwrite = csv.writer(ResultFile)

    # Write the summarized results to the txt file
    txtwrite.writerows(listoflists(ResultTable))

