#import os and csv module
import os 
import csv 

#create a path to our csv file
#note i used the full path due to it not recognising the resources folder
csvpath = 'C:\\Users\\riona\\pythonn-challenge\\PyBank\\Resources\\budget_data.csv'

#create an empty list for the financial data 
financial_data = []

# Open the CSV file and read the data
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    
    #create a loop through each row in the csv and append it to the financial data list 
    for row in csvreader:
        financial_data.append(row)

# Calculate total months
total_months = len(financial_data)

#calculaate the net_total of profit/losses
net_total = sum(int(row[1]) for row in financial_data)

# Calculate the change in profit for each month
change_in_profit = []
for i in range(1, len(financial_data)):
    current_profit = int(financial_data[i][1])
    previous_profit = int(financial_data[i - 1][1])
    change_in_profit.append(current_profit - previous_profit)

# calcualte the average change using sum 
average_change = sum(change_in_profit) / len(change_in_profit)

#calculate greatest profit increase using max
greatest_increase = max(change_in_profit)
greatest_increase_index = change_in_profit.index(greatest_increase)
greatest_increase_date = financial_data[greatest_increase_index + 1][0]

#calculate greatest decreate profit using min 
greatest_decrease = min(change_in_profit)
greatest_decrease_index = change_in_profit.index(greatest_decrease)
greatest_decrease_date = financial_data[greatest_decrease_index + 1][0]

# Print the financial analysis results
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")

# Save the financial analysis results to a text file
output_file = "financial_analysis.txt"
with open(output_file, "w") as txtfile:
    txtfile.write("Financial Analysis\n")
    txtfile.write("----------------------------\n")
    txtfile.write(f"Total Months: {total_months}\n")
    txtfile.write(f"Total: ${net_total}\n")
    txtfile.write(f"Average Change: ${average_change:.2f}\n")
    txtfile.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n")
    txtfile.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n")
