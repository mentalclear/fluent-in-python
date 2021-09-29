import scrabble

# print all words that have "uu"
for word in scrabble.wordlist:
    if "uu" in word:
        print(word)