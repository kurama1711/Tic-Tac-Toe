class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def getArea(self):
        return self.a * self.b


class Square (Rectangle):
    def __init__(self, a):
        self.a = a

    def getSquareArea(self):
        return self.a ** 2

class Circle:
    def __init__(self, r):
        self.r = r

    def getArea(self):
        return 3.14 * self.r ** 2
