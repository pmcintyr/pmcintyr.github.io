![Photo of Lausanne](/docs/assets/lausanne.jpg)

### Task 1
Identify streets with unique or multiple spellings by comparing yearly files and building a [dictionary](https://github.com/pmcintyr/pmcintyr.github.io/blob/main/dictionary.csv) of the top 100 most popular street names.✔️

### Task 2
Find mistakes in street names (spaces, numbers, different spellings, missing characters, overflows in next column/row).
Correct mistakes and log changes.✔️ (This was achieved by manual dictionary and suggestion modifications in the notebook).

### Task 3
Provide [mappings](https://github.com/pmcintyr/pmcintyr.github.io/blob/main/mappings.csv) between uniquely named and non-uniquely named streets with their corresponding modern street names. (This will be done by cross-examining street names with Lausanne [toponyms](https://github.com/RPetitpierre/merian/blob/main/assets/data/toponyms.geojson)).

### Task 4
Verify the house numbers are in strictly increasing order for a same street, by adding an error detection column with encoded values based on error type.

### Task 5
Track the homeowner name continuity by comparing yearly files for a same address.

### Task 6
Map rows between each yearly file
Make a streetmap with yearly evolution of the best homeowner mappings.
