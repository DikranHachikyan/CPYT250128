# port - глобална променлива
port = 1521
# 1. дефиниция
def sum_numbers(a, b):
    # c - локална променлива
    c = a + b
    return c

if __name__ == '__main__':
    
    # 2. извикване на функцията
    result  = sum_numbers( 5, 7)
    print(f'result = {result}')

    x, y = 10, 20
    result = sum_numbers(x, y)
    
    print(f'{x} + {y} = {result}')

    print('---')