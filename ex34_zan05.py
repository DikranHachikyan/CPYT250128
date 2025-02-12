# 1. дефиниция
def show(title, ver='1.3.2', *args, **kwargs):
    
    print(f'title (positional):{title}')

    print(f'ver (optional):{ver}')

    print('args:')
    for i in args:
        print(i, end=' ')
    print()

    kw = {
        'color': kwargs.get('color', 'black'),
        'font': kwargs.get('font', 'sans-serif'),
        'size': kwargs.get('size', 16)
    }
    print(f'keyword args:{kw}')

    print()

if __name__ == '__main__':

    ui = {
        'size': 10,  
        'font':'Monospace', 
        'color':'red',
        'platform':'mobile',
        'width': 800
    }
    # 4.
    show('Web App', '1.1.1' , 1, 2, 3, 4, 5, **ui )

    print('---')