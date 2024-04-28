import pandas as pd
import urllib.request
import json
import csv
import time
import os


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


def marathon(input_file, output_file):
    # Read ISBNs from the input text file
    with open(input_file, 'r') as file:
        isbn_list = [line.strip() for line in file]

    # Create a DataFrame with the ISBNs
    df = pd.DataFrame({'ISBN': isbn_list})

    # Group by ISBN and count copies
    df['copyNum'] = df.groupby('ISBN').cumcount() + 1

    # Add a default condition column
    df['condition'] = 'unset'

    # Reorder columns
    df = df[['ISBN', 'copyNum', 'condition']]

    # Write the DataFrame to a new CSV file
    df.to_csv(output_file, index=False)


def jongara(input_filepath, output_filepath, initial_delay=2, max_retries=7):
    delay = initial_delay

    # Open text file of ISBNs to read
    with open(input_filepath, "r") as f_in:

        # Open a CSV file to store finished data
        with open(output_filepath, "a", encoding="utf-8", newline='') as f_out:

            # Create a CSV writer object
            writer = csv.writer(f_out)

            # If the output file is empty, write the header
            if f_out.tell() == 0:
                writer.writerow(['ISBN', 'title', 'authors', 'summary'])

            # Loop through each ISBN in the input file
            for current_ISBN in f_in:
                retries = 0
                success = False

                while not success and retries < max_retries:
                    # Connect to Google Books API
                    base_api_link = "https://www.googleapis.com/books/v1/volumes?q=isbn:"
                    try:
                        with urllib.request.urlopen(base_api_link + current_ISBN.strip()) as response:
                            text = response.read()
                            decoded_text = text.decode("utf-8")
                            obj = json.loads(decoded_text)

                            # Check if book data is available
                            if "items" in obj and len(obj["items"]) > 0:

                                # Extract relevant information
                                volume_info = obj["items"][0]["volumeInfo"]
                                current_title = volume_info.get("title", "N/A")
                                current_authors = volume_info.get("authors", ["N/A"])
                                current_summary = volume_info.get("description", "N/A")

                                # Ensure proper CSV formatting
                                current_title = current_title.replace('"', '""')
                                current_summary = current_summary.replace('"', '""')

                                # Write extracted data to CSV file
                                writer.writerow([current_ISBN.strip(), current_title, ', '.join(current_authors), current_summary])
                                success = True

                            else:
                                # If no book found for the ISBN, write a placeholder to the CSV file
                                writer.writerow([current_ISBN.strip(), "N/A", "N/A", "N/A"])
                                success = True

                    except urllib.error.HTTPError as e:
                        # Handle HTTP errors (e.g., too many requests)
                        if e.code == 429:
                            retries += 1
                            time.sleep(delay)
                            delay *= 2  # Exponential backoff
                        else:
                            break
                    except Exception as e:
                        break

                print("Processed ISBN:", current_ISBN.strip())

                # Reset delay for next iteration
                delay = initial_delay

    print("Processing complete.")


def strip_unique_isbns(input_filepath, output_filepath):
    # Set to store unique ISBNs
    unique_isbns = set()

    # Read the file and extract unique ISBNs
    with open(input_filepath, "r") as file:
        for line in file:
            isbn = line.strip()
            if isbn:  # Check if the line is not empty
                unique_isbns.add(isbn)

    # Write unique ISBNs to a text file
    with open(output_filepath, "w") as output_file:
        for isbn in unique_isbns:
            output_file.write(isbn + '\n')


def samba(csv_file, overwrite_original=False):
    # Check if the CSV file exists
    if not os.path.isfile(csv_file):
        raise FileNotFoundError(f"CSV file '{csv_file}' not found.")

    # Read CSV file into a DataFrame
    df = pd.read_csv(csv_file)

    # Find blank cells or cells with "N/A" values
    blank_cells = df.isna() | (df == 'N/A')

    # Track the last edited cell
    last_edited_cell = None

    try:
        # Iterate over rows with blank cells
        for index, row in blank_cells.iterrows():
            if row.any():  # Check if the row has at least one blank cell
                print(df.loc[index])  # Print the row for reference

                # Prompt user for input for missing information
                for column in df.columns:
                    if pd.isna(df.at[index, column]) or df.at[index, column] == 'N/A':
                        value = None
                        while value is None:
                            value = input(f"Enter {column} (press 'p' to go back to previous edited cell): ").strip()
                            if value.lower() == 'p':
                                if last_edited_cell is not None:
                                    row_index, col_index = last_edited_cell
                                    print(f"Previous value in {df.columns[col_index]}: {df.iat[row_index, col_index]}")
                                    value = df.iat[row_index, col_index]
                                else:
                                    print("No previous edited cell. Continuing to next cell.")
                            else:
                                # Check if the value ends with a newline character
                                if value.endswith('\n'):
                                    confirm = input(
                                        "The entered value ends with a newline. Do you want to proceed? (y/n): ").strip().lower()
                                    if confirm == 'y':
                                        df.at[index, column] = format_csv_value(value)
                                        last_edited_cell = (index, df.columns.get_loc(column))
                                    else:
                                        value = None  # Prompt for input again
                                else:
                                    df.at[index, column] = format_csv_value(value)
                                    last_edited_cell = (index, df.columns.get_loc(column))

                print()  # Add a blank line for readability

    except KeyboardInterrupt:
        save_changes = input("\nDo you want to save changes? (y/n): ").strip().lower()
        if save_changes == 'y':
            if overwrite_original:
                # Write the updated DataFrame back to the original CSV file
                df.to_csv(csv_file, index=False)
                print("Changes saved to the original file.")
            else:
                # Determine the new file path for the cleaned data
                output_file_path = csv_file.replace('.csv', '_cleaned.csv')

                # Write the updated DataFrame to a new CSV file
                df.to_csv(output_file_path, index=False)
                print("Changes saved to a new file:", output_file_path)
        else:
            print("Changes have not been saved.")

    return df
