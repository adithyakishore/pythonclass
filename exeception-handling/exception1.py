# num1 = 1
# num2 = 0
# result = 0
# result = num1/num2
# print(result)
# print('halo')

num1 = 3
num2 = 0
result = 0

try:
    result = num1/num2
except ZeroDivisionError as e:
    print(e)
print('halo')