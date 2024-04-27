# Removes blank lines from end of csv files, aka possibly one of the most pointless pieces of software to exist

import pandas as pd


def remove_blank_lines_from_csv(filename):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(filename)

    # Remove blank lines from the end of the DataFrame
    while df.empty or df.iloc[-1].isnull().all():
        df = df[:-1]

    # Write the cleaned DataFrame back to the original file
    df.to_csv(filename, index=False)


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
