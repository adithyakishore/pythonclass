list = [[2,5,8] ,[3,7,4] ,[1,6,9] ,[4,2,0]]

def display_rows(rows):
    for i in range(len(rows)):
        print(f"{i+1} : {rows[i]}")
    print()

def add_value_to_row(row,value):
    row.append(value)
    return row

while True:
    print('available row')
    display_rows(list)
    row_number = input('enter the row number you want to display(or "exit") : ')
    if row_number.lower() == 'exit':
        break
