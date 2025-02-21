from functools import wraps

# 1. дефиниция на декоратора
def to_upper( func ):
    @wraps(func)
    def wrapper( *args, **kwargs ):
        wrapper.original = func
        args = [ f'{v}'.upper() for v in args]
        return func( *args, **kwargs )
    return wrapper

@to_upper
def concat( *args, **kwargs):
    '''Concatenate args with separator sep'''
    sep = kwargs.get('sep', ';')
    return sep.join(args)

if __name__ == '__main__':
    users = [ 'anna', 'maria', 'markus', 'jorg' ]

    print(f'users:{concat(*users)}')
    print(f'users:{concat(*users, sep=", ")}')

    values = [ 10, 23, 45, 67, 89 ]
    print(f'values:{concat(*values, sep="|")}')
    
    concat = concat.original
    print(f'users:{concat(*users)}')
    print('---')