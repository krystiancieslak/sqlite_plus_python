import sqlite3


con = sqlite3.connect("testDB.db")
cur = con.cursor()

def creating_table():
    try:
        cur.execute("CREATE TABLE books(id, title, author)")
        print("Table has been created.")
    except:
        print('Table already exists.')

def inserting_values():
    cur.execute("""
    INSERT INTO books VALUES
        (1, 'Lord of the rings', 'J.R.R. Tolkien'),
        (2, 'Harry Potter and the goblet of fire', 'J.K. Rowling'),
        (3, 'I Heard You Paint Houses', 'Charles Brandt'),
        (4, 'Before coffee gets cold', 'Toshikazu Kawaguchi')
    """)
    con.commit()
    
creating_table()
inserting_values()