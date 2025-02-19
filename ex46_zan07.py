# 1.
# import time
# print(f'now is:{time.time()}')

# 1.1
# import time as ts
# print(f'now is:{ts.time()}')

# 2.
# from time import time, sleep
# print(f'now is:{time()}')

#  2.1
# from time import time as now, sleep
# print(f'now is:{now()}')

from time import time, sleep

def foo(sleep_time=0.5):
    '''Function foo sleeps sleep_time seconds'''
    sleep(sleep_time)

if __name__ == '__main__':

    t = time()
    foo()
    print(f'exec time:{time() - t:.3f}s')

    t = time()
    foo(0.8)
    print(f'exec time:{time() - t:.3f}s')


    print('---')