# GENERATORS

# Even number generator from 0 to N
def even_numbers(n):
    for i in range(0, n + 1, 2):
        yield i

# Fibonacci generator up to N
def fibonacci_up_to(n):
    a, b = 0, 1
    while a <= n:
        yield a
        a, b = b, a + b
