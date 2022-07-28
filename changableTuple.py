x=(1,2,3,4,6,7)
y=list(x)




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
        y.append(n)
        x=tuple(y)
        print(x)
    elif c==2:
       if len(y)==0:
        print("Enpty stack")
       else :
           p=y.pop()
           x=tuple(y)
           print(x)
    elif c==3:
      if len(list)==0:
        print("stack empty")
      else:
        print("The last element of stack" ,x[-1])
    elif c==4 :
        print("display list", x)
    elif c==5:
     break
    else :
     exit(0)