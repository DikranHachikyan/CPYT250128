from draw.point import Point


if __name__ == '__main__':

    # 2. декларираме променлива от тип Point
    # клас -типът, който сме дефинирали (Point)
    # обект - променливата, представител на класа
    print('--- begin ---') 
    p1 = Point( x=10, y=30)
    p2 = Point( x=10, y=30)

    print(f'Object p2:{p2}')
    
    print(f'P2 coords:' + str(p2) )
    
    if p1 == p2:
        print(f'1: {p1} equals {p2}')
    else:
        print(f'1: {p1} does not equal {p2}')

    p3 = p2
    if p3 == p2:
        print(f'2: {p3} equals {p2}')

    p3 = p1 + p2
    p3.draw()

    p3 = p2 + 10.5
    p3.draw()
    
    print('--- end ---')