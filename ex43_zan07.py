

if __name__ == '__main__':
    
    pow_xy = lambda x, y: x ** y

    z = pow_xy( 2, 4)
    print(f'z={z}')

    numbers = [ 4, 2, 3, 5, 1]

    # for v in map( lambda el: pow_xy(el,2), numbers ):
    for v in map( lambda el: el ** 2, numbers ):
        print(f'v={v}')

    print('---')