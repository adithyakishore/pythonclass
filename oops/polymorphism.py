import math
# num1 = 2
# num2 = 5
# sum = num1 + num2
# print(sum)

# fname = 'adithya'
# lname = 'k'
# print(fname + ' ' + lname)
# # print(f"{fname} {lname}")

# courses = ['python','react' , 'flutter' ,'mern' , 'angular' , 'java']

# user_data ={
#     'name' : 'samad',
#     'email': 'adithya',
#     'age' : '34'

# }
# print(len(user_data))
# print(len(fname))
# print(len(courses))


class Polygon:
    def render(self):
        print('rendering a polygon')

    def calculate_area():
        pass 


class Square(Polygon):
    def __init__(self,side_length):
        self.side_length = side_length
    
    def render(self):
        print('rendering a square')

    def calculate_area(self):
        
        area = self.side_length ** 2
        print(f'area of square is {area} units ')
        

class Circle(Polygon):
    def __init__(self,radius):
        self.radius = radius
    
    def render(self):
        print('rendering a Circle')

    def calculate_area(self):
        area = math.pi *  self.radius ** 2
        print(f'area of circle is {area:.2f} units ')

square1 = Square(3)
square1.render()
square1.calculate_area()

circle1 = Circle(5)
circle1.render()
circle1.calculate_area()
