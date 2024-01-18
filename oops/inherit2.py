class Vehicle:
    def __init__(self,model,brand):
        self.model = model
        self.brand = brand

    def start_eng(self):
        print('engine started')
    def stop_eng(self):
        print('stop engine')

class Car(Vehicle):
    def __init__(self, model, brand,no_of_doors,year):
        Vehicle.__init__(self,model, brand)
        self.no_of_doors = no_of_doors
        self.year = year
    def car_details(self):
        print(self.model)
        print(self.brand)
        print(self.year)
        print(self.no_of_doors)
c1 = Car('ca','benz',4,2002)
c1.car_details()
c1.start_eng()
c1.stop_eng()    