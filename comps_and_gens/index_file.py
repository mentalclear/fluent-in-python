import itertools

def index_file(handle):
    """ A generator that streams input from a file one line 
    at a time and yields outputs one word at a time """
    offset = 0
    for line in handle:
        if line:
            yield offset
        for letter in line:
            offset += 1
            if letter == ' ':
                yield offset

with open('address.txt', 'r') as f:
    it = index_file(f)
    results = itertools.islice(it, 0, 10)
    print(list(results))

# the callers must be aware that the iterators 
# returned are stateful and can’t be reused
