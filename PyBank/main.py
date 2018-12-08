# Your task is to create a Python script that analyzes the records to calculate each of the following:


# The total number of months included in the dataset
# The total net amount of "Profit/Losses" over the entire period
# The average change in "Profit/Losses" between months over the entire period
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in losses (date and amount) over the entire period


# As an example, your analysis should look similar to the one below:


#   Financial Analysis
#   ----------------------------
#   Total Months: 86
#   Total: $38382578
#   Average  Change: $-2315.12
#   Greatest Increase in Profits: Feb-2012 ($1926159)
#   Greatest Decrease in Profits: Sep-2013 ($-2196167)


# Modules
import os
import csv

# Set path for csv file
csvpath = os.path.join("Resources", "budget_data.csv")

# Open the CSV
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #counting number of rows in the dataset (minus the header)
    #as it represents the number of months in this case
    data = list(csvreader)
    months_count = len(data) - 1
# print("Financial Analysis:")
# print("------------------------------")
# print(f'Total Months: {months_count}')

    # total = 0.0
    # for row in data:
        #total  = row[1]
column = 1
print (sum(row[column] for row in data))

# rows = csvreader.DictReader(csvfile)
# print (sum(float(csvfile['Profit/Losses']) for csvfile in rows) 
# def average(numbers):
#     length = len(numbers)
#     total = 0.0
#     for number in numbers:
#         #total = total+number
#         total += number
#     return total / length

    # for row in csvreader:
    #     print(row)
    #     if float(row[7]) >= 5:
    #         print(row)
    
    