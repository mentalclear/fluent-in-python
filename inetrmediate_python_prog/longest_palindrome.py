import scrabble

def first_solution():
    longest = ""
    for word in scrabble.wordlist:
        is_palindrome = True
        for index in range(len(word)):
            if word[index] != word[-(index + 1)]:
                is_palindrome = False
        if is_palindrome and len(word) > len(longest):
            longest = word

    print(longest)

first_solution()

# refactored:
def second_solution():
    longest = ""
    for word in scrabble.wordlist:
        if list(word) == list(reversed(word)) and len(word) > len(longest):
            longest = word

    print(longest)

second_solution()

def third_solution():
    longest = ""
    for word in scrabble.wordlist:
        if word == word[::-1] and len(word) > len(longest):
            longest = word
            
    print(longest)

third_solution()