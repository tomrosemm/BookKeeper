# Searches students csv file for duplicate rows and deletes them, outputs to either a new csv with _cleaned attached or
# Replaces original

import pandas as pd
import os


# Searches students csv file for duplicate rows and deletes them, outputs to either a new csv with _cleaned attached or
# Replaces original
def technopop(input_file_path, overwrite_original=False):
    # Progress indicators to console for user
    print("Technopop - Start")

    # Read the CSV file
    df = pd.read_csv(input_file_path)

    # Remove duplicate rows based on 'ID' and 'name' columns
    df_cleaned = df.drop_duplicates(subset=['sID', 'sName'], keep='first')

    if overwrite_original:
        # Overwrite the original CSV file with the cleaned data
        df_cleaned.to_csv(input_file_path, index=False)
        print("Original file overwritten with cleaned data:", input_file_path)
    else:
        # Determine the new file path for the cleaned data
        output_file_path = input_file_path.replace('.csv', '_cleaned.csv')

        # Write the cleaned data to a new CSV file
        df_cleaned.to_csv(output_file_path, index=False)
        print("New file created with cleaned data:", output_file_path)

    # Progress indicators to console for user
    print("Technopop - End")


''''
# Usage with overwrite_original=True
input_file_path = r"path\to\students.csv"  # Replace with the path to your students.csv file
technopop("students.csv", overwrite_original=True)

# Usage with overwrite_original=False
input_file_path = r"path\to\students.csv"  # Replace with the path to your students.csv file
technopop(input_file_path, overwrite_original=False)
'''
