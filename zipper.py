# Dependencies
import csv
import os

# Three Lists
indexes = [1, 2, 3, 4]
players = ["Michael", "Magic", "Lebron", "KD"]
teams = ["Bulls", "Lakers", "Cavs", "Nets"]


# Zip all three lists together into 
roster = zip(indexes, players, teams)


# save the output file path
output_file = os.path.join("Data","Output","roster.csv")


# open the output file, create a header row, and then write the zipped object to the csv
with open(output_file, 'w', newline='') as csvfile:

    # Create an instance of the writer. "Putting pen to paper"
    writer = csv.writer(csvfile)

    # Write first row to csv, column headers
    writer.writerow(["Index","Player","Team"])

    # Write multiple rows
    writer.writerows(roster)