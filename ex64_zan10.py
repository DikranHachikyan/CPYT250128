# 1. дефиниция на класа

class Point:
    
    def __init__(self, *, x=0, y=0, visible=True, **kwargs):
        print('--- init Point ---')
        # данни на обекта
        self.x = x
        self.y = y
        self.is_visible = visible

    def draw(self):
        print(f'draw point at ({self.x}, {self.y})')

    def move_to(self, dx, dy):
        self.x += dx
        self.y += dy

    # методи за достъп до данните (python)
    @property
    def x(self):
        return self.__x
    
    @x.setter
    def x(self, x):
        assert x >= 0, f'x must be positive number (x={x})'
        self.__x = x
    
    @property
    def y(self):
        return self.__y
    
    @y.setter
    def y(self,y):
        assert y >= 0, f'y must be positive number (y={y})'
        self.__y = y


    @property
    def is_visible(self):
        return self.__visible

    @is_visible.setter
    def is_visible(self, visible):
        assert type(visible) is bool, 'Type of visible must be bool'
        self.__visible = visible

    
if __name__ == '__main__':

    # 2. декларираме променлива от тип Point
    # клас -типът, който сме дефинирали (Point)
    # обект - променливата, представител на класа
    print('--- begin ---') 
    p1 = Point()
    p2 = Point( x=10, y=30)

    
    p1.x = 30
    p1.y = 3

    p1.draw()
    p2.draw()
    
    p1.move_to(5, 8)
    p1.draw()

    # p1.x = -3

    print('--- end ---')