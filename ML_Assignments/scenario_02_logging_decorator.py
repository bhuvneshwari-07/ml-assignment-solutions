# Scenario 2: Logging Decorator
# Task: Create a decorator to log the execution time of a function.

import time

def log_execution_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} executed in {end - start:.5f} seconds")
        return result
    return wrapper

@log_execution_time
def calculate_sum(n):
    return sum(range(1, n + 1))


if __name__ == "__main__":
    print("Sum:", calculate_sum(1000000))