Todo_list=[]

while True:
    print("1. Add A Task")
    print("2. view all the task")
    print("3. Delete a task")
    print("4. Exit")
    i=int(input("enter your choice  "))
    if i==1:
        task=input("enter your task")
        Todo_list.append(task)
    elif i==2:
        for choice in Todo_list:
            print(choice)
    elif i==3:
        task=input("enter task you want to remove")
        Todo_list.remove(task)
    elif i==4:
        break
    else:        print("invalid input")