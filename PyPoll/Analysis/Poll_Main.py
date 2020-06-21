import os
import csv

poll_csv = os.path.join("..", "Resources", "election_data.csv")

# Create empty dictionary to store name and vote results
election_results = {}

# Set total votes to 0 for count
total_votes = 0

with open(poll_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)

    for row in csvreader:

        # Add 1 vote through every loop
        total_votes += 1
        # Set column value for name pull
        candidate_name = row[2]
        # If name not in election_results dict, add name and 1 point
        if candidate_name not in election_results:
            election_results[candidate_name] = 1
        # If in election_results dict, add point to name key
        else:
            election_results[candidate_name] += 1

# Calculate Winner
winner = max(election_results, key=election_results.get)


print("Election Results")
print("-------------------------")
print(f"Total Votes: {str(total_votes)}")
print("-------------------------")
print(f'Khan: {election_results["Khan"] / total_votes:.3%} ({election_results["Khan"]})')
print(f'Correy: {election_results["Correy"] / total_votes:.3%} ({election_results["Correy"]})')
print(f'Li: {election_results["Li"] / total_votes:.3%} ({election_results["Li"]})')
# Would not print as f string. Had to use this format to print O'Tooley's results
print("O'Tooley: " + "{:.3%}".format(election_results["O'Tooley"] / total_votes) + " (" + (str(election_results["O'Tooley"])) + ")")
print("-------------------------")
print(f"Winner: {str(winner)}")
print("-------------------------")

output_path = os.path.join("Election_Results.txt")

with open(output_path, 'w') as datafile:

    datafile.write("Election Results\n")
    datafile.write("------------------------\n")
    datafile.write(f"Total Votes: {str(total_votes)}\n")
    datafile.write("------------------------\n")
    datafile.write(f'Khan: {election_results["Khan"] / total_votes:.3%} ({election_results["Khan"]})\n')
    datafile.write(f'Correy: {election_results["Correy"] / total_votes:.3%} ({election_results["Correy"]})\n')
    datafile.write(f'Li: {election_results["Li"] / total_votes:.3%} ({election_results["Li"]})\n')
    datafile.write("O'Tooley: " + "{:.3%}".format(election_results["O'Tooley"] / total_votes) + " (" + (str(election_results["O'Tooley"])) + ")\n")
    datafile.write("------------------------\n")
    datafile.write(f"Winner: {str(winner)}\n")
    datafile.write("------------------------\n")