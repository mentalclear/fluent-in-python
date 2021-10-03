# Goal
# Print the names of 10 Jeopardy categories.

import sqlite3
from sqlite3.dbapi2 import Cursor

connection = sqlite3.connect("inetrmediate_python_prog/jeopardy/jeopardy.db")
cursor = connection.cursor()

results = cursor.execute("SELECT name FROM category LIMIT 10").fetchall()

print("Example categories: \n")
for category in results:
    print(category[0])


connection.close()    
