import os
import sqlite3

con = None
cur = None

def check_database():
    global con, cur
    if not os.path.exists("testDB.db"):
        con = sqlite3.connect("testDB.db")
        cur = con.cursor()
        creating_table()
        inserting_values()
    else:
        con = sqlite3.connect("testDB.db")
        cur = con.cursor()
        if not table_exists("books"):
            creating_table()
            inserting_values()

def table_exists(table_name):
    cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (table_name,))
    result = cur.fetchone()
    return result is not None

def creating_table():
    try:
        cur.execute("CREATE TABLE books(id, title, author)")
        print("Table 'books' has been created.")
    except sqlite3.OperationalError:
        print("Table 'books' already exists.")

def inserting_values():
    cur.execute("""
    INSERT INTO books VALUES
        (1, 'Lord of the rings', 'J.R.R. Tolkien'),
        (2, 'Harry Potter and the goblet of fire', 'J.K. Rowling'),
        (3, 'I Heard You Paint Houses', 'Charles Brandt'),
        (4, 'Before coffee gets cold', 'Toshikazu Kawaguchi')
    """)
    con.commit()

def main():
    check_database()

if __name__ == "__main__":
    main()