class A:

    def input(self):
        self.a=int(input("Enter the value"))
        self.b=int(input("Enter second value"))

class B():
    def sum (self) :
        self.c=self.a+self.b
        print(self.c)


class C():
    def sub (self) :
        self.c=self.a-self.b
        print(self.c)

class D(A,B,C):
    def mult (self) :
        self.c=self.a*self.b
        print(self.c)



obj=D()
obj.input()
obj.sum()
obj.sub()
obj.mult()