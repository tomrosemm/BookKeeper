# Searches students csv file for duplicate rows and deletes them, outputs to a fresh CSV file

import pandas as pd

# Progress indicators to console for user
print("Technopop - Start")

# Read the CSV file
input_file_path = "students.csv"
output_file_path = "cleaned_students.csv"

df = pd.read_csv(input_file_path)

# Remove duplicate rows based on 'ID' and 'name' columns
df_cleaned = df.drop_duplicates(subset=['sID', 'sName'], keep='first')

# Write the cleaned data to a new CSV file
df_cleaned.to_csv(output_file_path, index=False)

# Progress indicators to console for user
print("Technopop - End")
