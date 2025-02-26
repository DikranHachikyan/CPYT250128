# 1. дефиниция на класа

class Point:
    
    def __init__(self, *, x=0, y=0, **kwargs):
        print('--- init Point ---')
        # данни на обекта
        self.x = x
        self.y = y

    def draw(self):
        print(f'draw point at ({self.x}, {self.y})')

    def move_to(self, dx, dy):
        self.x += dx
        self.y += dy

if __name__ == '__main__':

    # 2. декларираме променлива от тип Point
    # клас -типът, който сме дефинирали (Point)
    # обект - променливата, представител на класа
    print('--- begin ---') 
    p1 = Point()
    p2 = Point( x=10, y=30)

    p1.draw()
    p2.draw()
    
    p1.move_to(-5, 8)
    p1.draw()

    print('--- end ---')