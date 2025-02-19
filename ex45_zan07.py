def get_squares(n):
    return [ i ** 2 for i in range(1, n + 1)]

# 1. дефиниция
def generate_squares(n):
    for i in range(1, n + 1):
        yield i ** 2

if __name__ == '__main__':

    values = get_squares(5)
    print(f'values={values}')

    # 2. присвояваме функ. генератор на променлива
    gs = generate_squares(10)

    print(f'types: generate_squares is:{type(generate_squares)}, gs is:{type(gs)}')

    # 3. консумираме съдържанието
    print(f'1=>{next(gs)}')
    print(f'2=>{next(gs)}')
    print(f'3=>{next(gs)}')
    print(f'4=>{next(gs)}')

    arr = list(gs)
    print(f'arr={arr}')

    # print(f'!! 5=>{next(gs)} !!')

    gs2 = generate_squares(5)

    for v in gs2:
        print(f'v={v}')
        
    print('---')