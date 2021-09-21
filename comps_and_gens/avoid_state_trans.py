class MyError(Exception):
    pass

# def my_generator():
#     yield 1
#     yield 2
#     yield 3

# it = my_generator()
# print(next(it)) # Yield 1
# print(next(it)) # Yield 2
# print(it.throw(MyError('test error')))

def my_generator():
    yield 1

    try:
        yield 2
    except MyError:
        print('Got MyError!')
    else:
        yield 3

    yield 4

it = my_generator()
print(next(it)) # Yield 1
print(next(it)) # Yield 2
print(it.throw(MyError('test error')))


class Reset(Exception):
   pass

def timer(period):
    current = period
    while current:
        current -= 1
        try:
            yield current
        except Reset:
            current = period

def check_for_reset():
    # Poll for external event
    ...

def announce(remaining):
    print(f'{remaining} ticks remaining')

def run():
    it = timer(4)
    while True:
        try:
            if check_for_reset():
                current = it.throw(Reset())
            else:
                current = next(it)
        except StopIteration:
            break
        else:
            announce(current)

run()

# Rewritten
print("\n")

class Timer:
    def __init__(self, period):
        self.current = period
        self.period = period

    def reset(self):
        self.current = self.period

    def __iter__(self):
        while self.current:
            self.current -= 1
            yield self.current

def run():
    timer = Timer(4)
    for current in timer:
        if check_for_reset():
            timer.reset()
        announce(current)

run()

