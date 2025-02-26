

if __name__ == '__main__':
    actions = {
        '+': lambda a, b: a + b,
        '/': lambda a, b: a / b
    }

    while True:
        try:
            op = input('actions (+, /, q-quit):')

            if op == 'q':
                break

            a_value = float( input('first number:'))
            b_value = float( input('second number:'))

            result = actions[op]( a_value, b_value)

        except (KeyError, ValueError) as e:
            print(f'Unsupported operation or invalid number:{e}')
        except Exception as e:
            print(f'Unknown error!({e})')
        # 1. python only 
        else:
            print(f'{a_value} {op} {b_value} = {result}')
            # continue
            # quit()
        # 2. python (not only)
        finally:
            print('--- finally ---')

    print('---')