import sqlite3

try:
  #initalizes a new sqlite database
  with sqlite3.connect("storedMail.db") as conn:  #connect() function accepts the database_file argument that specifies the location of the SQLite database
    print(f"Opened SQLite database with version {sqlite3.sqlite_version} successfully")

except sqlite3.OperationalError as e:
  print("Failed to open database:", e)
  


