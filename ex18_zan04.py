# print(f'name:{__name__}')
# 2 + 4 + .... + 100 = 2550


if __name__ == '__main__':
    i = 1
    sum_n = 0
    
 
    while i <= 8:
        i += 1
        if ( i % 2 ) != 0:
            continue
        sum_n += i

    print(f'2 + 4 + ... + 98 + 100 = {sum_n}')
    print('---')