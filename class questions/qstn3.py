class Square:
    def __init__(self, side_length):
        self.side_length = side_length

    def calculate_area(self):
        area = self.side_length ** 2
        return area

    def calculate_perimeter(self):
        perimeter = 4 * self.side_length
        return perimeter

square1 = Square(3)
area1 = square1.calculate_area()
print(f"Area of square: {area1}")
perimeter1 = square1.calculate_perimeter()
print(f"Perimeter of square: {perimeter1}")
