import os
import pandas as pd
import urllib.request
import json
import csv
import time
import shutil

# Constant file paths
DEFAULT_CSV_FILE = "Files/books.csv"  # Default CSV file name - set in the main file


# Removes blank lines from end of csv files
# Now also pass a true or false boolean named replace_original to either replace the original file or make a new one
def condor(filename, replace_original=False):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(filename)

    # Remove blank lines from the end of the DataFrame
    while df.empty or df.iloc[-1].isnull().all():
        df = df[:-1]

    if replace_original:
        # Write the cleaned DataFrame back to the original file
        df.to_csv(filename, index=False)
    else:
        # Return the cleaned DataFrame
        return df


# Format a cell value for CSV in 2 ways:
# 1 - If the value contains commas, double quotes, or starts/ends with whitespace,
# enclose it in double quotes and escape double quotes.
# 2 - Remove newline characters (\n) from the value.
def format_csv_value(value):
    value = value.replace('\n', ' ')  # Replace newline characters with spaces
    if any([char in value for char in (',', '"')]) or value.strip() != value:
        return f'"{value.replace("\"", "\"\"")}"'
    return value


# Searches students csv file for duplicate rows and deletes them, outputs to either a new csv with _cleaned attached or
# Replaces original
def technopop(input_file_path, overwrite_original=False):

    # Console Readout
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
