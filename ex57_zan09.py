def print_key( key, **kwargs):
    try:
        print(f'{key} => {kwargs[key]}')
    except KeyError as e:
        # 3. обичайно решения
        raise
        # 2. още по-лоша идея
        # pass

        # 1. лоша идея!!!
        # print(f'invalid key:{key} module:{__name__}')
    print('--- end of print key ---')

if __name__ == '__main__':

    conn ={
        'host':'localhost',
        'port': 1521,
        'service': 'oracle-xe'
    }

    try:
        print_key('host', **conn)
        print_key('ip', **conn)
    except KeyError as e:
        print(f'connection object does not contain ip key')

    print('---')