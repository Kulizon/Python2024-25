import random

def zero_one_iterator():
    while True:
        yield 0
        yield 1

def random_direction_iterator():
    directions = ["N", "E", "S", "W"]
    while True:
        yield random.choice(directions)

def weekday_iterator():
    day = 0
    while True:
        yield day
        day = (day + 1) % 7

zero_one = zero_one_iterator()
print("Iterator 0, 1, 0, 1:", [next(zero_one) for _ in range(10)])

random_directions = random_direction_iterator()
print("Iterator losowy kierunek:", [next(random_directions) for _ in range(10)])

weekdays = weekday_iterator()
print("Iterator dni tygodnia:", [next(weekdays) for _ in range(14)])
