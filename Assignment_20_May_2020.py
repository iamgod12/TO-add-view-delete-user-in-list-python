options = """
    Press 1: To add user
    Press 2: To view Users
    Press 3: Update User
    Press 4: Delete User
    Press 5: To Exit
"""
print(options)
users=[]
while True:
    
    choice=input("Enter Choice: ")
    if choice=="1":
        name = input("Enter User name to add: ")
        if name in users:
            print("user already exit")
        else:
            users.append(name)
            print(name,"added Successfully")
        
    elif choice=="2":
            print("Total Users are : ",format(len(users)))
            for (i, user) in enumerate(users, start=1):
                print(i, user)
       
    elif choice=="3":
            ind=int(input("Enter User name index to update: "))
            up=input("Enter New User name: ")
            if name in users:
                pass
            else:
                print("User does not exist")
            users.append(name)
            print(name,"added Successfully")
            users[ind-1]=up  
            for (i, user) in enumerate(users, start=1):
                print(i, user)
            print("New User Name updated Successfully")
    elif choice=="4":
        fr=str(input("Enter User name to be deleted: "))
        users.remove(fr)
        print(fr,"deleted Successfully")
                     
    elif choice=="5":
        break
    else:
        print("Invalid Choice")
        
