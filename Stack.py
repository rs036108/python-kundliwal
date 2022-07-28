list=[]

while True :
    c=int(input('''
    1 Push elements
    2 Pop element
    3 peek element
    4 display stack
    5 Exit
    '''))
    if c==1:
        n=int(input("Enter the element"))
        list.append(n)
        print(list)
    elif c==2:
       if len(list)==0:
        print("Enpty stack")
       else :
           p=list.pop()
           print(p)
           print(list)
    elif c==3:
      if len(list)==0:
        print("stack empty")
      else:
        print("The last element of stack" ,list[-1])
    elif c==4 :
        print("display list", list)
    elif c==5:
     break
    else :
     exit(0)