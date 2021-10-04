import sqlite3

connection = sqlite3.connect('inetrmediate_python_prog/jeopardy/jeopardy.db')
cursor = connection.cursor()

results = cursor.execute("SELECT text, answer, value FROM clue LIMIT 10").fetchall()

for clue in results:       
    # What I wrote first time:
    # print("\n")
    # print(f"[${clue[2]}]")
    # print(f"Question: {clue[0]}")
    # print(f"Answer: {clue[1]}")

    text, answer, value = clue

    print("\n")
    print(f"[${value}]")
    print(f"Question: {text}")
    print(f"Answer: {answer}")
    

connection.close()
