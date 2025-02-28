# 1. дефиниция на класа

class Point:
    
    def __init__(self, *, x=0, y=0, visible=True, **kwargs):
        print('--- init Point ---')
        # данни на обекта
        self.set_x(x)
        self.set_y(y)
        self.set_visible(visible)

    def draw(self):
        print(f'draw point at ({self.get_x()}, {self.get_y()})')

    def move_to(self, dx, dy):
        self.set_x( self.get_x() + dx)
        self.set_y( self.get_y() + dy)

    # методи за достъп до данните (класически подход)
    def set_x(self, x):
        assert x >= 0, f'x must be positive number (x={x})'
        self.__x = x

    def get_x(self):
        return self.__x
    
    def set_y(self, y):
        assert y >= 0, f'y must be positive number (y={y})'
        self.__y = y

    def get_y(self):
        return self.__y

    def set_visible(self, visible):
        assert type(visible) is bool, 'Type of visible must be bool'
        self.__visible = visible

    def is_visible(self):
        return self.__visible

if __name__ == '__main__':

    # 2. декларираме променлива от тип Point
    # клас -типът, който сме дефинирали (Point)
    # обект - променливата, представител на класа
    print('--- begin ---') 
    p1 = Point()
    p2 = Point( x=10, y=30)

    
    if p1.is_visible():
        p1.draw()

    p1.set_x(30)
    p1.set_y(3)

    p1.draw()
    p2.draw()
    
    p1.move_to(5, 8)
    p1.draw()

    p1.set_x(-3)
    print('--- end ---')