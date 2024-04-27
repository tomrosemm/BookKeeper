from datetime import datetime
import sqlite3
import pandas as pd
import os
import csv


# Create Tables Function
def create_tables():
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS books(ISBN CHAR(13) PRIMARY KEY, title VARCHAR(200), authors VARCHAR(200),"
                "summary VARCHAR(2000))")
    cur.execute("CREATE TABLE IF NOT EXISTS copies(ISBN CHAR(13) REFERENCES books ON DELETE CASCADE, copyNum INT,"
                "condition VARCHAR(10), PRIMARY KEY(ISBN, copyNum))")
    cur.execute("CREATE TABLE IF NOT EXISTS students(sID CHAR(8) PRIMARY KEY, sName VARCHAR(50))")
    cur.execute("CREATE TABLE IF NOT EXISTS checked_out(sID CHAR(8) REFERENCES students, ISBN CHAR(13) REFERENCES books,"
                "dateCheckedOut DATE, PRIMARY KEY (sID, ISBN))")


# Drop Tables Function
def drop_tables():
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS checked_out")
    cur.execute("DROP TABLE IF EXISTS students")
    cur.execute("DROP TABLE IF EXISTS copies")
    cur.execute("DROP TABLE IF EXISTS books")

    con.commit()


# Populate Table Function
def populate_tables(table_name, csv_file):
    df = pd.read_csv(csv_file)
    df.to_sql(table_name, con, if_exists='replace', index=False)


# Aggregate for initial tables
def populate_all_initial_tables():
    populate_tables("books", "books.csv")
    populate_tables("copies", "copies.csv")
    populate_tables("students", "cleaned_students.csv")
    populate_tables("checked_out", "checked_out.csv")
    con.commit()


# Backup Tables Function
def backup_tables():
    if not os.path.exists('backups'):
        os.makedirs('backups')

    cur = con.cursor()
    table_names = ['books', 'copies', 'students', 'checked_out']
    for table_name in table_names:
        cur.execute(f"SELECT * FROM {table_name}")
        rows = cur.fetchall()
        with open(f'backups/{table_name}.csv', 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([i[0] for i in cur.description])
            writer.writerows(rows)


# Delete Database Function
def delete_database():
    try:
        os.remove("bookshelf.db")
        print("Database deleted successfully.")
    except FileNotFoundError:
        print("Database does not exist.")


def create_database():
    global con
    con = sqlite3.connect("bookshelf.db")
    print("Created the database successfully.")


# Load Initial Data Function
def load_initial_data():
    create_tables()


    # Check if backup files exist
    backup_files_exist = all(os.path.exists(f'backups/{table_name}.csv') for table_name in ['books', 'copies', 'students', 'checked_out'])

    if backup_files_exist:
        print("Loading data from backup files...")
        for table_name in ['books', 'copies', 'students', 'checked_out']:
            df = pd.read_csv(f'backups/{table_name}.csv')
            df.to_sql(table_name, con, if_exists='replace', index=False)
    else:
        print("No backup files found. Loading data from original CSV files.")
        populate_all_initial_tables()


# Main Menu Interface Function
def menu_interface():
    print("Choose from the following options:")
    print("1. Checkout a book")
    print("2. Return a book")
    print("3. Browse the collection of books")
    print("4. Current date")
    print("5. Exit")
    choice = input("Your choice: ")
    menu_switch(choice)


# Function to Check out a Book
def checkout_book():
    print("1")
    return


# Function to Return a Book
def return_book():
    print("2")
    return


# Function to Browse Books
def browse_books():
    print("3")
    return


# Function to Switch Menu Options
def menu_switch(option):
    if option == "1":
        checkout_book()
        return
    if option == "2":
        return_book()
        return
    if option == "3":
        browse_books()
        return
    if option == "4":
        print(get_current_date())
        return
    if option == "5":
        backup_tables()
        con.close()
        delete_database()
        quit()


# Function to Get Current Date
def get_current_date():
    current_date = datetime.now().date()
    return current_date


if __name__ == '__main__':

    create_database()
    load_initial_data()
    menu_interface()

    # Close connection
    con.close()

    # Delete the database
    delete_database()
