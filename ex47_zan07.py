from time import time, sleep
from functools import wraps

# 1. дефиниция на декоратора
def measure_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        t = time()
        func(*args, **kwargs)
        print(f'1 name:{func.__name__} doc str:{func.__doc__} time:{time()-t:.3f}')
    
    return wrapper    

@measure_time
def foo(sleep_time=0.5):
    '''Function foo sleeps sleep_time seconds'''
    sleep(sleep_time)

if __name__ == '__main__':

    foo()

    foo(0.8)

    print(f'2 name:{foo.__name__} doc str:{foo.__doc__}')
    print('---')