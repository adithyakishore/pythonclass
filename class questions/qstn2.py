class Staff:
    def __init__(self,name,salary,age):
        self.name = name
        self.salary = salary
        self.age = age
    
class Teacher(Staff):
    def __init__(self, name, salary, age,subject):
        super().__init__(name, salary, age)
        self.subject = subject
        
obj = Teacher('hy',9,12,'uu')
print(obj.subject)