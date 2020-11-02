from figures import Rectangle, Square, Circle

rect_1 = Rectangle(3, 4)
rect_2 = Rectangle(12, 5)

print(f"Площадь 1го прямоугольника: {rect_1.getArea()}")
print(f"Площадь 2го прямоугольника: {rect_2.getArea()}")

square_1 = Square(5)
square_2 = Square(10)

print(f"\nПлощадь 1го квадрата: {square_1.getSquareArea()}")
print(f"Площадь 2го квадрата: {square_2.getSquareArea()}")

circle_1 = Circle(3)
circle_2 = Circle(4)

print(f"\nПлощадь 1го круга: {circle_1.getArea()}")
print(f"Площадь 2го круга: {circle_2.getArea()}")

my_figures = [rect_1, rect_2,
              square_1, square_2,
              circle_1, circle_2]

print("\nПлощади всех имеющихся фигур:")

for elem in my_figures:
    if isinstance(elem, Square):
        print(elem.getSquareArea())
    else:
        print(elem.getArea())
