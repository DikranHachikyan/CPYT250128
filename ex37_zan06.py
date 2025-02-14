# port - глобална променлива
port = 1521

# 1. дефиниция
def show():
    global port
    # c - локална променлива
    c = 2
    port = 3306
    print(f'inside show port:{port}')

if __name__ == '__main__':

    print(f'(before) global variable port:{port}')
    show()
    print(f'(after) global variable port:{port}')
    
    print('---')