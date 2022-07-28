class Input :

    def __init__(self):
        self.x=eval(input("Enter  the  first value"))
        self.y=eval(input("Enter the second value"))

    def __display(self):
        print(self.x)
        print(self.y)
        print("Private function")
    def Help(self):
        self.__display()

obj=Input()
obj.Help()
obj._Input__display()


