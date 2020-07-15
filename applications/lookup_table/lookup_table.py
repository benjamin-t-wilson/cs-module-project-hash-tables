# Your code here
import random
import math

def slowfun_too_slow(x, y):
    v = math.pow(x, y)
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653

    return v

cache = {}

def slowfun(x, y):
    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.
    """
    # Your code here
    if f'{x},{y},pow' not in cache:
        cache[f'{x},{y},pow'] = math.pow(x, y)
    if f'{x},{y},fac' not in cache:
        cache[f'{x},{y},fac'] = math.factorial(cache[f'{x},{y},pow'])
    if f'{x},{y},div' not in cache:
        cache[f'{x},{y},div'] = cache[f'{x},{y},fac'] // (x + y)
    if f'{x},{y},mod' not in cache:
        cache[f'{x},{y},mod'] = cache[f'{x},{y},div'] % 982451653
    return cache[f'{x},{y},mod']



# Do not modify below this line!

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')