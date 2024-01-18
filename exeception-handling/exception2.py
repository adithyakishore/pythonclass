try:
    a = int(input('enter a number : '))
    result = 10 / a
    print('result is',result)
except ZeroDivisionError as e:
    print('error : devision by zero')

except ValueError as e:
    print('error : invalid input')
else:
    print('no exception occured.Everything executed succesfully')
finally:
    print('this block is always excecuted')