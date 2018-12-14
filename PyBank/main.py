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
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")
    #print(csvreader)

    # counting number of rows in the dataset 
    # as it represents the number of months in this case
    data = list(csvreader)
    months_count = len(data)
    
print("Financial Analysis:")
print("--------------------------------")
print(f'Total Months: {months_count}')

profit_loss_column = []
months_column = []

# Iterating thoroug the "Profit/Losses" column to sum all the values
total = 0
for row in data:
    profit_loss_column.append(row[1])
    months_column.append(row[0])

    #counting the total sum of profit/loses over the entire period
    total = total + int(row[1])
print(f'Total: ${total}')


current_index = 0
next_index = current_index + 1
months_change_list = []

    # for value in profit_loss_column:
for value in range(len(profit_loss_column)-1):
    change = int(profit_loss_column[next_index]) - int(profit_loss_column[current_index])
    months_change_list.append(change)
    current_index += 1
    next_index = current_index + 1

        # calculating the average change by summing all values in the created 
        # months_change_list and dividing them by total months - 1 since the first change
        # occurs after the second month 
    average_change = round(sum(months_change_list)/(months_count - 1),2)

        #finding max and min values on the months_change_list
    max_value = max(months_change_list)
    min_value = min(months_change_list)

        # Looking up the max and min value index in the list 
    index_max_value = months_change_list.index(max_value)
    index_min_value = months_change_list.index(min_value)

        #matching the max and min index value wit the corresponding
        # month value in the month_column.  
    increase_month = months_column[index_max_value + 1]
    decrease_month = months_column[index_min_value + 1] 
print(f'Average Change: {average_change}\nGreatest Increase in Profits: {increase_month} (${max_value})\nGreatest Decrease in Profits: {decrease_month} (${min_value})')


#ask about the strange values in the final .txt
with open("budget_data_analysis.txt", 'w') as text:
    text.write("Financial Analysis:\n")
    text.write("---------------------------------------\n")
    text.write(f'Total Months: {months_count}\n')
    text.write(f'Total: ${total}\nAverage Change: {average_change}\nGreatest Increase in Profits: {increase_month} (${max_value})\nGreatest Decrease in Profits: {decrease_month} (${min_value})')