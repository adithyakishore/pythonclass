class  A:
    def __init__(self):
        print('from parent')

    def display_1(self):
        print('display 1 ...')

    def display_2(self):
        print('display 2 ...')

class B(A):
    def __init__(self):
        super()

        print('from child')

    def display_3(self):
        print('display 3 ...')
        
    def display_4(self):
        print('display 4 ...')


obj1 = A()
# print(obj1)
# print(obj1.display_1())

# print(obj1.display_3())


obj2 = B()
print(obj2)
print(obj2.display_1())
print(obj2.display_3())