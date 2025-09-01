import logging
from functools import wraps
from generators import even_numbers, fibonacci_up_to
from iterators import ReverseListIterator, EvenIterator

# Logger settings
logging.basicConfig(
    filename="app.log",       # log file
    level=logging.INFO,       # logging level
    format="%(asctime)s [%(levelname)s] %(message)s",  # log format
    datefmt="%Y-%m-%d %H:%M:%S"
)

logger = logging.getLogger(__name__)


# DECORATORS

# Decorator for logging arguments and results
def log_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logger.info(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        logger.info(f"{func.__name__} returned {result}")
        return result
    return wrapper


# Decorator for exception handling
def exception_handler(message="An error occurred"):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                logger.error(f"{message} in {func.__name__}: {e}")
        return wrapper
    return decorator


# EXAMPLES
if __name__ == "__main__":
    print("Even number generator up to 20:")
    for num in even_numbers(20):
        print(num, end=" ")
    print("\n")

    print("Fibonacci generator up to 999:")
    for num in fibonacci_up_to(999):
        print(num, end=" ")
    print("\n")

    print("Iterator for a reverse list [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:")
    for item in ReverseListIterator([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]):
        print(item, end=" ")
    print("\n")

    print("Iterator of even numbers up to 40:")
    for number in EvenIterator(40):
        print(number, end=" ")
    print("\n")

    print("Logging decorator test:")

    @log_decorator
    def add(a, b):
        """Adds two numbers."""
        return a + b

    add(5, 3)
    print()

    print("Exception handling decorator test:")

    @exception_handler("Custom error")
    def divide(a, b):
        """Divides two numbers."""
        return a / b

    divide(10, 2)  # OK
    divide(10, 0)  # Division by zero
