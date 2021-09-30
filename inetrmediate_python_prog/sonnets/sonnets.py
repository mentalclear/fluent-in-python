import time

def first_iter():
    my_words = [elt.strip() for elt in open("inetrmediate_python_prog/sonnets/sonnet_words.txt", "r").readlines()]
    word_list = [elt.strip() for elt in open("inetrmediate_python_prog/sonnets/sowpods.txt", "r").readlines()]

    counter = 0

    start = time.time()
    for word in my_words:
        if word not in word_list:
            print(word)
            counter += 1
    stop = time.time()

    print(f"Total new words: {counter}")
    print(f"Time elapsed: {stop-start}")

#first_iter()

def second_iter():
    my_words = [elt.strip() for elt in open("inetrmediate_python_prog/sonnets/sonnet_words.txt", "r").readlines()]
    word_list = [elt.strip() for elt in open("inetrmediate_python_prog/sonnets/sowpods.txt", "r").readlines()]
    word_dict = dict((elt, 1) for elt in word_list)

    counter = 0

    start = time.time()
    for word in my_words:
        if word not in word_dict:
            print(word)
            counter += 1
    stop = time.time()

    print(f"Total new words: {counter}")
    print(f"Time elapsed: {stop-start}")

second_iter()