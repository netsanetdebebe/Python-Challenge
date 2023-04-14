import os
import csv

budget_csv = os.path.join("Resources","budget_data.csv")
file_to_output = os.path.join("PyBank Analysis re-do", "Budget_analysis_.txt")

total_months = 0
total_PRLO = 0
initial_change = 0
agg_change_list = []
greatest_increase_in_profits = ["", 0]
greatest_decrease_in_profits = ["", 99999999999]


with open (budget_csv, "r") as csvfile:
    csvreader=csv.reader(csvfile)

    header = next(csvreader)

    first_row = next(csvreader)
    total_months += 1 
    total_PRLO += int(first_row[1]) 
    initial_change = int(first_row[1])
    

    for row in csvreader:
        total_months += 1 
        profit = int(row[1])

        agg_change = int(row[1]) - initial_change
        initial_change = int(row[1])
        agg_change_list.append(agg_change)   
        total_PRLO = profit + total_PRLO
        

        if agg_change > greatest_increase_in_profits[1]:
            greatest_increase_in_profits[0] = row[0]
            greatest_increase_in_profits[1] = agg_change

        if agg_change < greatest_decrease_in_profits[1]:
            greatest_decrease_in_profits[0] = row[0]
            greatest_decrease_in_profits[1] = agg_change

net_average = sum(agg_change_list) / len(agg_change_list)


output = (
    f"PyBank Analysis re-do\n"
    f"-----------\n"
    f"total months: {total_months}\n"
    f"total: ${profit}\n"
    f"average change: ${net_average:.2f}\n"
    f"Geatest increase in profits: {greatest_increase_in_profits[0]} (${greatest_increase_in_profits[1]})\n"
    f"Greatest decrease in profits: {greatest_decrease_in_profits[0]} (${greatest_decrease_in_profits[1]})\n")

print(output)

with open(file_to_output,"w") as txt_file:
    txt_file.write(output)

