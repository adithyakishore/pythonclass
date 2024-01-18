invited_people = []

for i in range(3):
    name = input('enter name of person you want to invite')
    invited_people.append(name)

print(invited_people)
while True:
    response = input('do you want to add another person?(yes/no): ')
    if response.lower() == 'yes':
       name = input('enter name of another person you want to invite')
       invited_people.append(name)
    else:
        break

num_invited = len(invited_people)
print("f you have invited {num_invited} people to the party")

