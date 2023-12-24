import os
import pickle
import csv

# Directory containing the pickle files
directory = 'pickles/stock_prices'
count = 0
# Iterate over files in the directory
for filename in os.listdir(directory):
    if filename.endswith('.p'):
        # Construct the full file path
        file_path = os.path.join(directory, filename)

        # Open the pickle file and read its contents
        with open(file_path, 'rb') as f:
            # Load the data from the pickle file
            data = pickle.load(f)

        # Extract the list of dictionaries from the 'Success' key
        success_data = data['Success']

        # Preprocess the data to exclude time from datetime and exclude exchange_code, stock_code, volume
        processed_data = []
        for entry in success_data:
            # Exclude time from datetime
            entry['datetime'] = entry['datetime'].split()[0]
            # Exclude exchange_code, stock_code, volume
            del entry['exchange_code']
            del entry['stock_code']
            del entry['volume']
            # Reorder the fields as date, open, close
            processed_entry = {'date': entry['datetime'], 'open': entry['open'], 'close': entry['close']}
            processed_data.append(processed_entry)

        # Create a CSV file name based on the pickle file name
        csv_file_path = os.path.splitext(file_path)[0] + '.csv'

        # Write the data to a CSV file
        with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
            # Define the CSV writer
            fieldnames = ['date', 'open', 'close']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            # Write the header row
            writer.writeheader()

            # Write each processed entry as a separate row in the CSV file
            writer.writerows(processed_data)
        