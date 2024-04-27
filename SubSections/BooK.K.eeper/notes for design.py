# *CAN WE USE SCANNER TO SCAN HER SCHOOL ID OR LICENSE OR SOME HOMEBREW LABEL OR SOMETHING INSTEAD 
#   *OF NEEEDING TO ENTER PASSWORD EVERY TIME? USING SCANNER FOR STUDENT TO ENTER AN ISBN
# *DOES SHE NEED TO BE ABLE TO ADD BOOKS AND ADD DETAILS TO BOOKS AT LATER TIMES?
# *POWER SITUATION: CAN BE LEFT ON OVERNIGHT? POWER OUTAGES COMMON?
# 
# During operation, backup new relevant tables during each transaction in case of program failure or external interruption
# When checking out or returning a book, try and allow scanner to enter ISBN
# Look for error points and handle gracefully
# 
# Backend Program
# (FIRST RUN)
# 1 - Create a copy of ISBN list with any duplicates removed
# 2 - Use unique ISBNs to run Jongara and build books.csv
# 3 - Allow user to progress through books and manually add data that is missing with Samba
# 4 - Use multiples ISBNs to create copies.csv with Marathon, counting the number of times the ISBN occurs. Currently doesn't work
# 5 - Create cleaned_students.csv by reading students.csv and deleting duplicate rows, with Technopop I believe
# (FIRST RUN END)
#
# (WHEN RUNNING FRONT END)
# 6 - Create database for information
# 7 - Create tables for books, copies, students, and checked_out
# 8 - Check if backups exist, populate tables with backup csv if so, from above 4 files if not
#
# (UPON SHUTDOWN)
#  - Backup each table to a csv file
#  - Delete database
#
# (MAINTINENCE OPTIONS)
# - Manually add data to rows in books.csv with missing data
# - Add new books by isbn, populating the books csv file with info gathered from jongara and update copies csv
#
# (BACKEND PROGRAM OVERVIEW)
#
# Menu Options:
#   Initialize System - first time
#   Add Missing book details Jongara manually
#   Add books to isbn list, update appropriate csv files
#   Manually edit values of books.csv to correct for erronous entries
