class DemoClass :
    a=0
    b=0
    c=0
    def __init__(self) :

        self.a=int(input("Enter first value"))
        self.b=int(input("Enter second value"))


    def sum (self) :
        self.c=self.a+self.b
        print(self.c)

    def sub(self):
        self.c = self.a - self.b

        print(self.c)

    def mult(self):
        self.c = self.a * self.b

        print(self.c)

    def dev(self):
        self.c = self.a / self.b

        print(self.c)


obj=DemoClass()
while True :
    n = int(input('''
      1. Addition
      2.Subtraction
      3. Multiplication
      4. devision
    
      '''))
    if n==1:
        obj.sum()
    elif n==2:
        obj.sub()
    elif n==3:
        obj.mult()
    elif n==4:
        obj.dev()

    else :
        break
