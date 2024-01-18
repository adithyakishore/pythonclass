class product:
    count = 0
    def __init__(self,name,category,price):
        self.name = name
        self.category = category
        self.__price = price
        product.count = product.count + 1
        print('init works')
        
    def display_product(self):
        print("name:",self.name)
        print("category:",self.category)
        print("name:",self.__price)

    def product_count(self):
        print("total number of products: %d" %product.count) 

    def set__price(self,price):
        self.__price = price
    def get__price(self):
        return self.__price

prod1 =product('pen', 'stationary',20) 
prod2 =product('orange', 'food' ,70) 
prod3 =product('orange', 'food' ,70) 
print(prod1.name)
print(prod2.category)
prod1.display_product()
prod2.display_product()
# print(prod2.__price)
print(prod1.get__price())
prod1.set__price(40)
print(prod1.get__price())