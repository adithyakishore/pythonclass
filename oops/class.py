class Student:
    count = 0
    students=[]
    def __init__(self,student_id,name,age,grade):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.grade = grade
        Student.count = Student.count + 1
        Student.students.append(self)
        
    def display_student(self):
        print("student_id:", self.student_id)
        print("name : ",self.name)
        print("age : ",self.age)
        print("grade : ",self.grade)
        
    def display_studentCount(self):
        print("Total number of students: %d" %Student.count)
        
    def view_students(self):
        print("student list")
        for student in Student.students:
            student.display_student()
            
stu1 = Student(1,"Dhaya",20,"a")
stu1.display_student()

def add_students():
    student_id = int(input("Enter the id of the student:"))
    name = input("Enter the name of the student : ")
    age = int(input("Enter the age of the student : "))
    grade = input("Enter the grade of the student : ")
    
    Student(student_id,name,age,grade)
    print(f"\nstudent with id {student_id} added sccessfully")
add_students()
stu1.view_students()


while True:
    print("\nOptions")
    print("1.Add students")
    print("2.View students")
    print("3.Exit")
    
    choice = input("Select any one of the above Options")
    if choice == "1":
        add_students()
    elif choice == "2":
       stu1.view_students()
    elif choice == "3":
        print("You are exited")
        break
    else:
        print("Invalid Option")