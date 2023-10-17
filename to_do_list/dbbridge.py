import sqlite3

conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()

# create the table if not exist
cursor.execute('''CREATE TABLE IF NOT EXISTS entries (
                   id INTEGER PRIMARY KEY,
                   person_or_organization TEXT,
                   location TEXT,
                   date TEXT,
                   time TEXT
                )''')

# take the inputs from user
person_or_organization = input("Person or Organization: ")
location = input("Location: ")
date = input("Date (Day Month Year): ")
time = input("Time: ")

# add inputs to the database
cursor.execute("INSERT INTO entries (person_or_organization, location, date, time) VALUES (?, ?, ?, ?)",
               (person_or_organization, location, date, time))

# save the changes and close the db connection
conn.commit()
conn.close()
