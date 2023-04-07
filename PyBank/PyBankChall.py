import os
import csv

budget_csv = os.path.join("resources","budget_data.csv")


total_months = 0
total_PRLO = 0
initial_change = 0
agg_change = 0 

with open (budget_csv, "r") as csvfile:
    csvreader=csv.reader(csvfile)
    header = next(csvreader)
    csv_reader=next(csvreader)
    first_row = next(csvreader)
    total_PRLO = int(first_row[1]) + total_PRLO
    total_months = total_months + 1 
    initial_change = int(first_row[1])
    

    for row in csvreader:
        total_months += 1 
        profit = int(row[1])
        total_PRLO = profit + total_PRLO
        agg_change += (profit - initial_change)
        initial_change = profit

    average_PROLO_change = round(agg_change/(total_months - 1), 2)

greatest_increase_in_profits = max(monthly_changes)
greatest_decrease_in_profits = min(monthly_changes)

print("ByBank23 analysis\n")
print("-----------\n")
print(f"total months: {total_months}")
print(f"total: ${total_PRLO}")
print(f"average change in profits: ${average_PROLO_change})\n")
print(f"Greatest increase in profits: ${greatest_increase_in_profits}\n")
print(f"Greatest decrease in profits: ${greatest_decrease_in_profits}\n")

      
