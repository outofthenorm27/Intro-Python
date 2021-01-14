# Dependencies
import os
import csv

# Specify the file name and path
output_path = os.path.join("Data","Output","new.csv")

# print(output_path)

# Open the file using the "write" mode 'w'
with open(output_path,'w', newline='') as csvfile:

    # Intialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=",")

    # Write the first row (column headers)
    csvwriter.writerow(['Height','Weight','Age'])

    # Write a second row
    csvwriter.writerow(["5'11", 205, 35])
    