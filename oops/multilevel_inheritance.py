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

class C(B):
    def __init__(self):
        super().__init__()

        print('from grandchild')

    def display_5(self):
        print('display 5 ...')
        
    def display_6(self):
        print('display 6 ...')


# obj1 = A()
# # print(obj1)
# # print(obj1.display_1())

# # print(obj1.display_3())


# obj2 = B()
# print(obj2)
# print(obj2.display_1())
# print(obj2.display_3())

obj3 = C()
print(obj3)
print(obj3.display_1())
print(obj3.display_2())