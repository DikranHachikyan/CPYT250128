# print(f'name:{__name__}')
# 1 + 2 + 3 + .... + 100 = 5050


if __name__ == '__main__':
    i = 1
    sum_n = 0

    while i <= 100:
        sum_n = sum_n + i
        # !! inf loop !!
        i = i + 1

    print(f'1+2+3+ ... +99+100={sum_n}')
    print('---')