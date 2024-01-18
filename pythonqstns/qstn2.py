invited_people = []

def display_manage_list():
    print('list of invited people : ')
    
    for i in range(len(invited_people)):
        print(f"{i+1} : {invited_people[i]}")
        
    choose_name = input('choose a name from the list (or type "done" to finish ): ')
    if choose_name.lower()== 'done':
        return False
    if choose_name in invited_people:
        position = invited_people.index(choose_name) + 1
        print(f"{choose_name} is at position {position} in the list ")
        response = input(f"do you still want {choose_name} to attend the party ? (yes/no) ")
        if response.lower() == 'no':
            invited_people.remove(choose_name)
            print(f"{choose_name} is removed from this list ")
    else:
        print(f"{choose_name} is not in the list")
    return True

while True:
    name = input('Enter the name of person you want to invite party :')
    invited_people.append(name)
    if not display_manage_list():
        break
    
print(invited_people)