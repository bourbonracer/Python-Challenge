import os
import csv

budget_csv = os.path.join("..", "Resources", "budget_data.csv")

# Set variables
greatest_inc_amt = 0
greatest_dec_amt = 0
running_total = 0
running_diff = 0
total_months = 0
last_amt = 0
diff_total = 0
average_diff = 0


with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)

    # Managing first row of data
    first = next(csvreader)
    last_amt = int(first[1])
    total_months += 1

    for row in csvreader:
        month = row[0]
        profit_loss = int(row[1])

        total_months += 1

        # Running total as profit and losses are added
        running_total = running_total + profit_loss

        # The difference between current profit_loss and previous
        running_diff = profit_loss - last_amt

        # Tracking last profit loss number
        last_amt = profit_loss

        if running_diff > greatest_inc_amt:
            greatest_inc_amt = running_diff
            greatest_inc_month = month
        elif running_diff < greatest_dec_amt:
            greatest_dec_amt = running_diff
            greatest_dec_month = month

        # Sum of differences between months
        diff_total = diff_total + running_diff

average_diff = round(diff_total / (total_months - 1),2)

print("Financial Analysis")
print("-------------------------------")
print(f"Total Months: {str(total_months)}")
print(f"Total: ${str(running_total)}")
print(f"Average Change: {str(average_diff)}")
print(f"Greatest Increase in Profits: {str(greatest_inc_month)} (${str(greatest_inc_amt)})")
print(f"Greatest Decrease in Profits: {str(greatest_dec_month)} (${str(greatest_dec_amt)})")

output_path = os.path.join("Financial_Results.txt")

with open(output_path, 'w') as datafile:
    datafile.write("Financial Analysis\n")
    datafile.write("-------------------------------\n")
    datafile.write(f"Total Months: {str(total_months)}\n")
    datafile.write(f"Total: ${str(running_total)}\n")
    datafile.write(f"Average Change: {str(average_diff)}\n")
    datafile.write(f"Greatest Increase in Profits: {str(greatest_inc_month)} (${str(greatest_inc_amt)})\n")
    datafile.write(f"Greatest Decrease in Profits: {str(greatest_dec_month)} (${str(greatest_dec_amt)})\n")