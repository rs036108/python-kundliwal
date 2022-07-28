list=[]
while True :
    n=int(input('''
    1. Insert  element
    2. Delet element
    3. Rear element
    4. Front element
    5.Display Queue
    6.Exit
    '''))
    if n==1:
        a=int(input("Enter the element"))
        list.append(a)
        print(list)
    elif n==2:
        if len(list)==0:
            print("Queue is empty")
        else :
            del list[0]

            print(list)
    elif n==3:
        if len(list)==0:
            print("Queue is empty")
        else:
            print(list[-1])

    elif n==4:
        if len(list)==0:
            print("Queue is empty")
        else:
            print(list[0])
    elif n==5:
        print(list)
    else:
        break