import os
import pandas as pd
import urllib.request
import json
import csv
import time
import shutil

DEFAULT_CSV_FILE = "books.csv"  # Default CSV file name

input_file_path = "students.csv"
output_file_path = "cleaned_students.csv"

# Make not relative, also determine if even need move step
destination = r'C:\Users\trose\PycharmProjects\Stale Cupcakes'


# Format a cell value for CSV: 1 - If the value contains commas, double quotes, or starts/ends with whitespace,
# enclose it in double quotes and escape double quotes. 2 - Remove newline characters (\n) from the value.
def format_csv_value(value):
    value = value.replace('\n', ' ')  # Replace newline characters with spaces
    if any([char in value for char in (',', '"')]) or value.strip() != value:
        return f'"{value.replace("\"", "\"\"")}"'
    return value


# Change this back to Jongara; the 95 limit was a test and was disproved immediately, but we are still maneuvering
# through the program as if it has a 95 limit. Refactor - remove loop counter, but reinstate the console feedback when
# a response is failed along with the wait time; only worry about reading through one .txt file;
def jongara(input_filepath, output_filepath=DEFAULT_CSV_FILE, initial_delay=2, max_retries=7):
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


# Search books.csv for rows with empty or N/A values and prompt user to replace the missing values in order, skip option
# Can overwrite fed file or make a new one
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


# Cleans students.csv
def technopop(input_file_path, output_file_path):

    # Progress indicators to console for user
    print("Technopop - Start")

    # Read the CSV file
    df = pd.read_csv(input_file_path)

    # Remove duplicate rows based on 'ID' and 'name' columns
    df_cleaned = df.drop_duplicates(subset=['sID', 'sName'], keep='first')

    # Write the cleaned data to a new CSV file
    df_cleaned.to_csv(output_file_path, index=False)

    # Progress indicators to console for user
    print("Technopop - End")


# Probably can be trimmed, offhand it was only created to test the 95 limit
def combine_txt_files(input_files, output_file):
    with open(output_file, 'w') as outfile:
        for file in input_files:
            with open(file, 'r') as infile:
                for line in infile:
                    outfile.write(line)


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


def main():

    # Do everything possible to condense the next 8 lines to just 'jongara(isbn_singleton.txt)'
    if os.path.exists(DEFAULT_CSV_FILE):
        print("books.csv already exists locally. Skipping Jongara process.")
    else:
        print("Jongara- start")  # Liar
        totalCount = jongara("list_of_isbn1.txt", 1)
        totalCount += jongara("list_of_isbn2.txt", 2)
        print("Extraction and writing of ", totalCount, " books and details to 'books.csv' total.")
        print("Jongara - end")  # Liar

    # Samba
    filleddf = samba()

    # Technopop
    technopop(input_file_path, output_file_path)


    input_files = ["list_of_isbn1.txt", "list_of_isbn1.txt"]
    output_file = "combined_files.txt"
    combine_txt_files(input_files, output_file)

    # Marathon -- currently kind of broken. Count not operating as expected. Fix in isolation
    marathon("combined_files.txt", "copies.csv")

    # Move shit
    source1 = 'books.csv'
    source2 = 'cleaned_students.csv'
    source3 = 'copies.csv'
    shutil.move(source1, destination)
    shutil.move(source2, destination)
    shutil.move(source3, destination)


main()
