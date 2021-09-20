def move(period, speed):
    for _ in range(period):
        yield speed

def pause(delay):
    for _ in range(delay):
        yield 0

def animate():
    for delta in move(4, 5.0):
        yield delta

    for delta in pause(3):
        yield delta

    for delta in move(2, 3.0):
        yield delta
    
def render(delta):
    print(f'Delta: {delta: .1f}')

def run(func):
    for delta in func():
        render(delta)

run(animate)

# animate function looks really repetitive

def animate_composed():
    yield from move(4, 5.0)
    yield from pause(3)
    yield from move(2, 3.0)

run (animate_composed)