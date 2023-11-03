import pandas as pd

# Read the CSV file
df = pd.read_csv('task1_cleaning_duplicates.csv', header=None, delimiter=";")

# Remove rows with no alphabetic characters and only numbers
df = df[~df[0].astype(str).str.match(r'^\d+\.?\d*$')]

# Save the modified DataFrame back to CSV
df.to_csv('modified_file.csv', index=False, header=False)
