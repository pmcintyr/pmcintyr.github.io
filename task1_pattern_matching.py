import csv
from collections import defaultdict
from Levenshtein import distance

# Step 1: Read the CSV file
with open('task1_cleaning_duplicates.csv', 'r') as file:
    data = list(csv.reader(file))

# Step 2: Create a dictionary with the first 100 street names
street_dict = {}
for row in data[:100]:
    street_name = row[0]
    street_dict[street_name] = street_name

# Step 3 and 4: Match the remaining rows and suggest real street names
for row in data[100:]:
    street_name = row[0]
    min_distance = float('inf')
    suggested_street = None
    for key in street_dict:
        dist = distance(street_name, key)
        if dist < min_distance:
            min_distance = dist
            suggested_street = key
    row.append(suggested_street)

# Print the updated data
for row in data:
    print(row)
