# Read a .txt file of ISBNs and populate a new 'copies.csv' file with all the data relevant to its table

import pandas as pd

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


'''
# Print statement for terminal progress assurance
print("Marathon - Start")

# Call the function with the input and output file names
marathon('isbn_list.txt', 'copies.csv')

# Print statement for terminal progress assurance
print("Marathon - End")
'''