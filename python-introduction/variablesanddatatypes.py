name = 'adi'
age = 10
marks = [10,50,40,70]
print(name)
print(age)
print(marks)


print(type(name))
print(type(age))
print(type(marks))
print("my name is %s and age is %d"%(name,age))

studentid = 100
studentname = "dhaya"
print("hello friends,my name is %s and my id is %d"%(studentname,studentid))


subjectname ="maths"
totalmark = 100
mymark =45
print("hi friends,i\'ve got %d marks outof %d in %s subject"%(totalmark,mymark,subjectname))

n1 = 10
n2 = 10.8
n3 = 2+3j
print(type(n1))
print(type(n2))
print(type(n3))

# to check boolien true or false
print(isinstance(n1,float))
print(isinstance(n3,complex))
print(isinstance(n2,int))


message = "Hello Cyber square"
print(message[0])
print(message[1:7])
print(message[2:])
print(message*5)
print(message +'test')
print(message[-1:])
print(message[-6:])
print(message[-11:15])
print(message[::3])
print(message[::-2])
print(message[::-3])



list1 = ["cyber",234,32.9,"square",8+2j]
list2 = ["adi",234,2.9,"dhaya",8+2j]
print(f"1 : {list1[0]}")
print(f"2 : {list1[1:4]}")
print(f"3 : {list1[2:]}")
print(f"4 : {list1*5}")
print(f"5 : {list1 + list2}")
print(f"6 : {list1[-1:]}")
print(f"7 : {list1[-6:]}")
print(f"8 : {list1[-11:15]}")
print(f"9 : {list1[::3]}")
print(f"10 : {list1[::-2]}")
print(f"11 : {list1[::-3]}")
list1[2] = 'demo'
print(list1)

tuple1 = ["cyber",234,32.9,"square",8+2j]
tuple2 = ["adi",234,2.9,"dhaya",8+2j]
print(f"1 : {tuple1[0]}")
print(f"2 : {tuple1[1:4]}")
print(f"3 : {tuple1[2:]}")
print(f"4 : {tuple1*5}")
print(f"5 : {tuple1 + list2}")
print(f"6 : {tuple1[-1:]}")
print(f"7 : {tuple1[-6:]}")
print(f"8 : {tuple1[-11:15]}")
print(f"9 : {tuple1[::3]}")
print(f"10 : {tuple1[::-2]}")
print(f"11 : {tuple1[::-3]}")
# tuple1[2] = 'demo'
print(tuple1)

tuple3 =(tuple1,tuple2,34,'adi')
print(tuple3)
print(tuple3[3])

student = {'name':'adithya','age':20,'marks':80}
print(student)
print(student['age'])
student['gender'] ='female'
print(student)
print(student.keys())
print(student.values())
student.clear()
print(student)

my_dict1 = {}
my_dict2 = {1:'grapes',2:'ball'}
my_dict3 = {'name': 'john',1:[2,4,3]}
my_dict4 = dict({1:'banana',2:'egg'})
my_dict5 = dict([(1,'apple'),(2,'eye')])

print(my_dict2)

print(my_dict3)