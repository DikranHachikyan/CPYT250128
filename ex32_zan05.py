# port - глобална променлива
port = 1521
# 1. дефиниция
def sum_numbers(a, b, *args ):
    # c - локална променлива
    print(f'type of args: {type(args)} args:{args}')
    c = a + b
    for i in args:
        c += i
    return c

if __name__ == '__main__':
    
    # 2. извикване на функцията
    result  = sum_numbers( 5, 7)
    print(f'result = {result}')

    x, y, z, s = 10, 20, 2, 5
    result = sum_numbers(x, y, z, s)
    
    print(f'{x} + {y} + {z} + {s} = {result}')

    arr = [ 1, 2, 3, 4, 5 ]

    result = sum_numbers( x, y, *arr)

    print(f'{x} + {y} + {" + ".join(map(str, arr))} = {result}')

    print('---')