import os
import pandas as pd

# Create an empty dictionary to store the counts of each value
value_counts = {}

# Define the folder path
folder_path = 'c:/Users/pmcintyr/Desktop/MA3/SHS/recensements'

# Iterate through each file in the folder
for filename in os.listdir(folder_path):
    if filename.endswith(".xlsx"):
        file_path = os.path.join(folder_path, filename)
        # Read the Excel file
        df = pd.read_excel(file_path)
        # Get the second column
        column_values = df.iloc[:, 1]
        # Count the occurrences of each value in the second column
        for value in column_values:
            if value in value_counts:
                value_counts[value] += 1
            else:
                value_counts[value] = 1

# Convert the dictionary to a pandas DataFrame
result_df = pd.DataFrame(list(value_counts.items()), columns=['Value', 'Count'])

# Sort the DataFrame by the 'Count' column in descending order
result_df = result_df.sort_values('Count', ascending=False)

# Save the DataFrame to a CSV file
result_df.to_csv("task1.csv", index=False)