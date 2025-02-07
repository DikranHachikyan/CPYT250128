

if __name__ == '__main__':
    
    values = [ i ** 2 for i in range(0, 11)]

    print(f'values = {values}')

    txt = 'Lorem ipsum dolor sit'

    symb = [ f'-{s}-' for s in txt]

    print(f'symb={symb}')

    print(f'txt={ "".join(symb)}')

    values = [ f'i={i},j={j}' for i in range(3) for j in range(4)]

    print(f'values={values}')

    # for i in range(3):
    #     for j in range(4):
    #         print(f'i={i},j={j}')
        
    print('---')