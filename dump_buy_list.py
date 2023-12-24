import os
import pickle
import csv

# Directory containing the pickle files
directory = 'pickles/buy_list'
count = 0
# Iterate over files in the directory
for filename in os.listdir(directory):
    if filename.endswith('.p'):
        # Construct the full file path
        file_path = os.path.join(directory, filename)

        # Open the pickle file and read its contents
        with open(file_path, 'rb') as f:
            # Read the lines from the pickle file
            lines = f.readlines()

        # Combine the lines into sets of four lines (each set represents a row of data)
        variable_sets = [lines[i:i + 4] for i in range(0, len(lines), 4)]

        # Strip newline characters and combine into a single row
        variable_sets = [[line.strip() for line in variable_set] for variable_set in variable_sets]

        # Create a CSV file name based on the pickle file name
        csv_file_path = os.path.splitext(file_path)[0] + '.csv'

        # Write the data to a CSV file
        with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)

            # Write each set of variables as a separate row in the CSV file
            for variable_set in variable_sets:
                writer.writerow(variable_set)
