# Removes blank lines from end of csv files, aka possibly one of the most pointless pieces of software to exist

import pandas as pd


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


'''
# Usage
filename = 'example.csv'

# Remove blank lines and replace the original file
condor(filename, replace_original=True)

# Or, remove blank lines and get the cleaned DataFrame without modifying the original file
cleaned_df = condor(filename)
print(cleaned_df)
'''


'''
# Runtime monitoring to terminal
print("Condor - Start")

booksFile = r"C:\Users\trose\PycharmProjects\Jongara\books.csv"
copiesFile = r"C:\Users\trose\PycharmProjects\Marathon\copies.csv"
studentsFile = r"C:\Users\trose\PycharmProjects\TechnoPop\cleaned_students.csv"

# The future checked_out table
# checked_outFile = ""

remove_blank_lines_from_csv(booksFile)
print("Blank lines removed from", booksFile)

remove_blank_lines_from_csv(copiesFile)
print("Blank lines removed from", copiesFile)

remove_blank_lines_from_csv(studentsFile)
print("Blank lines removed from", studentsFile)
'''

