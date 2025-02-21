from functools import wraps

# 1. дефиниция на декоратора
def to_upper( func ):
    @wraps(func)
    def wrapper( *args, **kwargs ):
        wrapper.original = func
        args = [ f'{v}'.upper() for v in args]
        return func( *args, **kwargs )
    return wrapper


if __name__ == '__main__':
    users = [ 'anna', 'maria', 'markus', 'jorg' ]

    print(*users)

    print = to_upper(print)
    print(*users)
    print('hello python')

    print = print.original
    
    print(*users)
    print('hello python')

    print('---')