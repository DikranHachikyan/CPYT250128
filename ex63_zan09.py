# 1. дефиниция на класа

class Point:
    
    def __init__(self, *, x=0, y=0, **kwargs):
        print('--- init Point ---')
        # данни на обекта
        self.set_x(x)
        self.__y = y

    def draw(self):
        print(f'draw point at ({self.get_x()}, {self.__y})')

    def move_to(self, dx, dy):
        self.set_x( self.get_x() + dx)
        self.__y += dy

    # методи за достъп до данните (класически подход)
    def set_x(self, x):
        assert x >= 0, f'x must be positive number (x={x})'
        self.__x = x

    def get_x(self):
        return self.__x

if __name__ == '__main__':

    # 2. декларираме променлива от тип Point
    # клас -типът, който сме дефинирали (Point)
    # обект - променливата, представител на класа
    print('--- begin ---') 
    p1 = Point()
    p2 = Point( x=10, y=30)

    # p1.x = -100
    # print(f'p1 __x is {p1.__x} p1 __y is {p1.__y}')
    # AttributeError: 'Point' object has no attribute '__x'
    
    # В Python атрибутите могат да се "закачат" динамично
    # p1.z = 20
    # print(f'p1 z:{p1.z} p2 z:{p2.z}')

    p1.set_x(30)
    p1.draw()
    p2.draw()
    
    p1.move_to(5, 8)
    p1.draw()

    print('--- end ---')