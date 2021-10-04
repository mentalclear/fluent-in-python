# Goal:
# Select a random game and print all of the categories from that game.

# SQL to get a random game:
# SELECT game FROM category ORDER BY RANDOM() LIMIT 1

# SQL to get the categories for a particular game:
# """SELECT name, round FROM category
#    WHERE game=%d ORDER BY round""" % (game_id,)

import sqlite3

connection = sqlite3.connect('inetrmediate_python_prog/jeopardy/jeopardy.db')
cursor = connection.cursor()

# Get a random game.
cursor.execute("SELECT game FROM category ORDER BY RANDOM() LIMIT 1")
results = cursor.fetchall()
game_id = results[0][0]
print(f"Categories for game #{game_id}:")

# Get the categories for that game.
query = """SELECT name, round FROM category
WHERE game=%d ORDER BY round""" % (game_id,)
cursor.execute(query)
results = cursor.fetchall()

for result in results:
    # Round 0 = Jeopardy round
    # Round 1 = Double Jeopardy
    # Round 2 = Final Jeopardy

    # name = result[0]
    # round = result[1]

    # same thing with tuple unpucking
    name, round = result
    print(f"Round {round}: {name}")

connection.close()
