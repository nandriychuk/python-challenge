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

    # counting number of rows in the dataset (minus the header)
    # as it represents the number of months in this case
    data = list(csvreader)
    months_count = len(data)
    
print("Financial Analysis:")
print("--------------------------------")
print(f'Total Months: {months_count}')

profit_loss_column = []
months_column = []
#fail - ask why
# profit_loss_column = [profit_loss_column for row in data]
# print(profit_loss_column)
# Iterating thoroug the "Profit/Losses" column to sum all the values
total = 0
for row in data:
    profit_loss_column.append(row[1])
    months_column.append(row[0])

    #for number in column_sum: ----I wa trying to do the nested for loop here since I thought 
    #that I need to iterate thtough eact munber in the column sum, since I thought that 
    # we ned to put it one list and then iterate through it, but I was able to iterate throug the row
    total = total + int(row[1])
print(f'Total: ${total}')
# print(months_column)

def average_change():
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

        # Looking up the max and min value index in order to find out the corresponding
        # month value in the month_column.  

        index_max_value = months_change_list.index(max_value)
        index_min_value = months_change_list.index(min_value)
        increase_month = months_column[index_max_value + 1]
        decrease_month = months_column[index_min_value + 1] 
    return print(f'Average Change: {average_change}\nGreatest Increase in Profits: {increase_month} (${max_value})\nGreatest Decrease in Profits: {decrease_month} (${min_value}) ')
average_change()

#print(f'Total Months: {months_count}')

#Average  Change: $-2315.12
#   Greatest Increase in Profits: Feb-2012 ($1926159)
#   Greatest Decrease in Profits: Sep-2013 ($-2196167)


#for value in average_change:
#you'll need that for task 4 and 5
    # max_value = max(average_change)
    # min_value = min(average_change)
    #print(max_value, min_value)
#print(min_value)
    
# for x in profit_loss_column:
#     profit_change = [x[i] - x[i+1] for x in profit_loss_column]
# print(profit_change)






    #print(row[0])
#

#type(row))
# column_sum  = [row.sum() for row in data]
# print (column_sum)
        #print(row[1])
# column = 1
# print (sum(row[column] for row in data))

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
    
    