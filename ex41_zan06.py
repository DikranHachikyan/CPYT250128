
def foo( a=None, b=None):
    if not a:
        a = []
    if not b:
        b = {}
     
    print(f'a={a} b={b}')
    print('-' * 40 )

    n = len(a)
    a.append(n)
    b[n] = n


if __name__ == '__main__':
    
    foo()

    foo([2, 4, 5], {'z':20})

    foo()

    foo([22, 14, 45], {'x':10})

    foo()
    
    foo()

    print('---')