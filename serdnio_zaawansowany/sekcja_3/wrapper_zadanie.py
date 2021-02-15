import time
import functools

def wrapper_time(func):
    def func_with_wrapper(*args, **kwargs):
        time_start = time.time()
        result = func(*args, **kwargs)
        time_end = time.time()
        v = time_end - time_start
        print(f"Funkcja wykonywała się: {v}")
        return result
    return func_with_wrapper

@wrapper_time
def get_sequence(n): 
    if n <= 0:
        return 1
    else:
        v = 0
        for i in range(n):
            v += 1 + (get_sequence(i - 1) + get_sequence(i))/2
        return v


print(get_sequence(10))
