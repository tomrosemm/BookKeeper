import os
import pandas as pd


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


def format_csv_value(value):
    # You can define your own formatting logic here if needed
    return value


'''
# Usage examples:

# Overwriting the original file
samba("books.csv", overwrite_original=True)

# Creating a new file with cleaned data
samba("books.csv", overwrite_original=False)


# Example usage
filled_df = fill_blank_cells()

# print(filled_df)
'''