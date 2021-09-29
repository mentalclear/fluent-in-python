import scrabble
import string

for letter in string.ascii_lowercase:
    exists = False
    for word in scrabble.wordlist:
        if letter * 2 in word:
            exists = True
            break

    if not exists:
        print(f"There are no English words with a double {letter}")    