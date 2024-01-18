file = ''
try:
    file = open('./demofile.txt','r')
    print(file.read())
except FileNotFoundError:
    print('error : can \'t find file or read data ')
else:
    print('no exception occured')
finally:
     print('this block is always excecuted') 

# try: 

    # code were exception might occure
# except:

    # handling a specific exception
    # you can have multiple except block for a try block to handle different type of exception

# else:
    # executed if no exceptn occur in the try block

# # finally:
    # executed irrespective of whether an exception occur or not