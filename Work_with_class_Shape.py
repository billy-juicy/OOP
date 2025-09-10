class Shape:

    def __init__(self, color, edge=0):
        self.color = color
        self.edge = edge

    def move(self):
        raise NotImplementedError("Переопределить методы в производных классах!")


class Circle(Shape):

    def __init__(self, color, edge=0):
        super().__init__(color, edge)

    def move(self):
        return "Катится"


class Rectangle(Shape):

    def __init__(self, color, edge=4):
        super().__init__(color, edge)

    def move(self):
        return "Лежит плашмя"

shape_circle = Circle('yellow')
shape_rectangle = Rectangle('black')
print(shape_circle.move())
print()
print(shape_rectangle.move())
