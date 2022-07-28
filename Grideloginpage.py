from tkinter import *


class Calculator:
    def  __init__(self,master):
        master.title("Calculater")
        master.geometry("370x520+0+0")
        root.config(bg='gray')
        master.resizable(False,False)
        self.value=StringVar()
        self.equation=''
        Entry(width=17,font=('Arial bold',28),textvariable=self.value).place(x=0,y=0)
        Button(width=11, height=4, text=')', relief='flat', bg='white', command=lambda: self.show(')')).place(x=0, y=50)
        Button(width=11, height=4, text='(', relief='flat', bg='white', command=lambda: self.show('(')).place(x=90,
                                                                                                              y=50)
        Button(width=11, height=4, text='%', relief='flat', bg='white', command=lambda: self.show('%')).place(x=180,
                                                                                                              y=50)
        Button(width=11, height=4, text='1', relief='flat', bg='white', command=lambda: self.show('1')).place(x=0,
                                                                                                              y=125)
        Button(width=11, height=4, text='2', relief='flat', bg='white', command=lambda: self.show('2')).place(x=90,
                                                                                                              y=125)
        Button(width=11, height=4, text='3', relief='flat', bg='white', command=lambda: self.show('3')).place(x=180,
                                                                                                              y=125)
        Button(width=11, height=4, text='4', relief='flat', bg='white', command=lambda: self.show('4')).place(x=0,
                                                                                                              y=200)
        Button(width=11, height=4, text='5', relief='flat', bg='white', command=lambda: self.show('5')).place(x=90,
                                                                                                              y=200)
        Button(width=11, height=4, text='6', relief='flat', bg='white', command=lambda: self.show('6')).place(x=180,
                                                                                                              y=200)
        Button(width=11, height=4, text='7', relief='flat', bg='white', command=lambda: self.show('7')).place(x=0,
                                                                                                              y=275)
        Button(width=11, height=4, text='8', relief='flat', bg='white', command=lambda: self.show('8')).place(x=90,
                                                                                                              y=275)
        Button(width=11, height=4, text='9', relief='flat', bg='white', command=lambda: self.show('9')).place(x=180,
                                                                                                              y=275)
        Button(width=11, height=4, text='0', relief='flat', bg='white', command=lambda: self.show('0')).place(x=90,
                                                                                                              y=350)
        Button(width=11, height=4, text='.', relief='flat', bg='cyan', command=lambda: self.show('.')).place(x=180,
                                                                                                             y=350)
        Button(width=11, height=4, text='-', relief='flat', bg='cyan', command=lambda: self.show('-')).place(x=270,
                                                                                                             y=200)
        Button(width=11, height=4, text='+', relief='flat', bg='cyan', command=lambda: self.show('+')).place(x=270,
                                                                                                             y=275)
        Button(width=11, height=4, text='/', relief='flat', bg='cyan', command=lambda: self.show('/')).place(x=270,
                                                                                                             y=50)
        Button(width=11, height=4, text='*', relief='flat', bg='cyan', command=lambda: self.show('*')).place(x=270,
                                                                                                             y=125)
        Button(width=11, height=4, text='=', relief='flat', bg='cyan', command=self.solve).place(x=270, y=350)
        Button(width=11, height=4, text='C', bg='red', relief='flat', command=self.clear).place(x=5, y=350)


    def show (self,num):
        self.equation+=str(num)
        self.value.set(self.equation)
    def clear(self):
        self.equation=''
        self.value.set(self.equation)
    def solve(self):
        self.result=eval(self.equation)
        self.value.set(self.result)
root=Tk()
obj = Calculator(root)
root.mainloop()






