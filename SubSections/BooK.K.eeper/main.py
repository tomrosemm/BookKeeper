import os
import sqlite3
import pandas as pd
from datetime import datetime


# Seperate properly the lines that should be used specifically to create the new database, menu after that

# Need to allow for the checking out of books by
# adding a row to the checked_out table and reducing a copy appropriately

# Needs to allow for returning of books by deleting corresponding row from checked out and adding back to copies
# enter ISBN or sID to find checked out item(s)

# Allow users to browse books in some sort of presentable interface

# Need to allow for future addition of data using tools, the verification and addition of data after introducing new
# data, and needs to update initial data files when books are added to or subtracted from

# When shutting down database, export info to new csv files, delete database; set up to properly reload itself upon
# reloading application. Try to not require constant uptime


# Create Tables Function
def createTables():

    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS books(ISBN CHAR(13) PRIMARY KEY, title VARCHAR(200), authors VARCHAR(200),"
                "summary VARCHAR(2000))")
    cur.execute("CREATE TABLE IF NOT EXISTS copies(ISBN CHAR(13) REFERENCES books ON DELETE CASCADE, copyNum INT,"
                "condition VARCHAR(10), PRIMARY KEY(ISBN, copyNum))")
    cur.execute("CREATE TABLE IF NOT EXISTS students(sID CHAR(8) PRIMARY KEY, sName VARCHAR(50))")
    cur.execute("CREATE TABLE IF NOT EXISTS checked_out(sID CHAR(8) REFERENCES students, ISBN CHAR(13) REFERENCES books,"
                "dateCheckedOut DATE, PRIMARY KEY (sID, ISBN))")

# Drop Tables Function
def dropTables():
    cur = con.cursor()
    cur.execute("DROP TABLE checked_out")
    cur.execute("DROP TABLE students")
    cur.execute("DROP TABLE copies")
    cur.execute("DROP TABLE books")

    con.commit()

# Populate Table Function
def populateTables(table_name, csv_file):
    df = pd.read_csv(csv_file)
    df.to_sql(table_name, con, if_exists='append', index=False)


# Aggregate for initial tables
def populateAllInitialTables():
    populateTables("books", "books.csv")
    populateTables("copies", "copies.csv")
    populateTables("students", "cleaned_students.csv")
    populateTables("checked_out", "checked_out.csv")
    con.commit()

# Delete Database Function
def deleteDatabase():
    try:
        os.remove("bookshelf.db")
        print("Database deleted successfully.")
    except FileNotFoundError:
        print("Database does not exist.")



def menuInterface():

    print("Choose from the following options:")
    print("1. Checkout a book")
    print("2. Return a book")
    print("3. Browse the collection of books")
    print("4. Current date")
    choice = input("Your choice: ")

    menuSwitch(choice)


def checkOutABook():

    # Need to allow for the checking out of books by
    # adding a row to the checked_out table and reducing a copy appropriately
    print("1")
    return


def returnABook():

    # Needs to allow for returning of books by deleting corresponding row from checked out and adding back to copies
    # enter ISBN or sID to find checked out item(s)
    print("2")
    return


def browseBooks():
    print("3")
    return


def menuSwitch(option):

    if option == "1":
        checkOutABook()
        return

    if option == "2":
        returnABook()
        return

    if option == "3":
        browseBooks()
        return

    if option == "4":
        print(getCurrentDate())
        return


def createDatabase():

    # Create Database
    global con
    con = sqlite3.connect("bookshelf.db")

    print("Created the database successfully.")


def loadInfo():
    createTables()
    populateAllInitialTables()

def getCurrentDate():
    current_date = datetime.now().date()
    return current_date


if __name__ == '__main__':

    createDatabase()

    loadInfo()

    menuInterface()

    # Close connection
    con.close()

    # Be sure to call after connection is closed if needed, and to keep live when testing repeatedly to not have to
    # manually delete database each time
    deleteDatabase()
