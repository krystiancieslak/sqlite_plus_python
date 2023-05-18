import os
import sqlite3

database_dir = "database"
database_file = f"{database_dir}/testDB.db"

def check_database():
    if not os.path.exists(database_file):
        # Creating new database
        os.makedirs(database_dir, exist_ok=True)
        con = sqlite3.connect(database_file)
        cur = con.cursor()
        creating_table(cur)
        inserting_values(cur, con)
        cur.close()
        con.close()
        print("New database has been created.")
    else:
        print("Database already exists.")

def creating_table(cur):
    cur.execute("CREATE TABLE IF NOT EXISTS books(id, title, author)")
    print("Creating table.")

def inserting_values(cur, con):
    cur.execute("INSERT INTO books VALUES (1, 'Lord of the rings', 'J.R.R. Tolkien')")
    cur.execute("INSERT INTO books VALUES (2, 'Harry Potter and the goblet of fire', 'J.K. Rowling')")
    con.commit()
    print("Inserted values into table.")

def main():
    check_database()

if __name__ == "__main__":
    main()