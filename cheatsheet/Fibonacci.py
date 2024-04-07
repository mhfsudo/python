# without Memoization
def fibonacci(n):
    # Check that the input is a positive integer
    if type(n) != int:
        raise TypeError("n must be a positive int")
    if n < 1:
        raise ValueError("n must be a positive int")

    # comput the Nth term
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci(n-1) + fibonacci(n-2)

for n in range(1, 36):
    print(n, ";", fibonacci(n))

# Memoization (Cache values)
fibonacci_cache = {}

def fibonacci(n):
    # Check that the input is a positive integer
    if type(n) != int:
        raise TypeError("n must be a positive int")
    if n < 1:
        raise ValueError("n must be a positive int")

    # If we habe cached the value, the return it
    if n in fibonacci_cache:
        return fibonacci_cache[n]

    # comput the Nth term
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        value = fibonacci(n-1) + fibonacci(n-2)

    # Cache the value and return it
    fibonacci_cache[n] = value
    return value

for n in range(1, 36):
    print(n, ";", fibonacci(n))

# Easy Memoization with Build in Tool (LRU = Least Recently Used Cache)
from functools import lru_cache

@lru_cache(maxsize = 1000)
def fibonacci(n):
    # Check that the input is a positive integer
    if type(n) != int:
        raise TypeError("n must be a positive int")
    if n < 1:
        raise ValueError("n must be a positive int")

    # comput the Nth term
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci(n-1) + fibonacci(n-2)

for n in range(1, 36):
    print(n, ";", fibonacci(n))
    print(fibonacci(n+1) / fibonacci(n))