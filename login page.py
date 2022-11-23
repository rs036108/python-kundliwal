import tkinter
from tkinter import*
from tkinter import messagebox
import time


class Window(tkinter.Toplevel):
    def __init__(self):
        super().__init__()


        self.geometry('760x420+330+190')
        #self.overrideredirect(1)
        self.attributes("-toolwindow", 1)
        self.title("Login Page")
        self.config(bg='white')
        Label(self, text='Rahul Photography ',font=('Megatron',20),bg='white').place(x=275, y=1)
        from tkinter import messagebox
        def sign_in(*args):

            self.username = self.user.get()
            self.password = self.code.get()

            self.ico = PhotoImage(file='./Icon/Places-mail-message-icon.png')
            self.iconphoto(False, self.ico)
            if self.username == 'rahul' and self.password == '1234':
                messagebox.showinfo("Login Page",'Login Successfully')

            elif self.username != 'rahul' and self.password != '1234':
                messagebox.showerror("Login Page",'Invaldi username and password')
            elif self. username != 'rahul':
                messagebox.showerror("Login page",'Invalid username')
            elif self.password != '1234':
                messagebox.showerror("Login Page",'Invalid password')

        def on_enter(event):
            self.user.delete(0, 'end')

        def on_leave(event):
            self.name = self.user.get()
            if self.name == '':
                self.user.insert(0, 'Username')

        self.user=Entry(self, font=('Times',14),border=0,width=32)
        self.f=Frame(self,width=295,height=2,bg='black')
        self.f.place(x=300,y=173)
        self.user.place(x=300,y=150)
        self.user.insert(0,"Username")
        self.user.bind('<FocusIn>', on_enter)
        self.user.bind('<FocusOut>', on_leave)


        def on_enter(event):
            self.code.delete(0, 'end')

        def on_leave(event):
            self.name = self.code.get()
            if self.name == '':
                self.code.insert(0, 'Password')


        self.code = Entry(self, font=('Times', 14), border=0,width=32)
        self.f = Frame(self, width=295, height=2, bg='black')
        self.f.place(x=300, y=223)
        self.code.place(x=300, y=200)
        self.code.insert(0, "Password")
        self.code.bind('<FocusIn>', on_enter)
        self.code.bind('<FocusOut>', on_leave)
        Button(self,text= 'Sing In',width=30,bg='#3498DB',fg='white',command=sign_in).place(x=350,y=290)

        Checkbutton(self).place(x=300,y=238)
        Label(self,text='Remember me',bg='white').place(x=328,y=239)
        Label(self, text="Don't have an account?", bg='white').place(x=350, y=330)

        Button(self, text='Sing Up', bg='white', fg='#3498DB',border=0,relief='flat').place(x=480, y=330)

        self.img2 = PhotoImage(file='./Login/01.png')
        Label(self, image=self.img2,border=0).place(x=0, y=0)





class App(Tk):
    def __init__(self):
        super().__init__()
        self.geometry('760x420+330+190')
        self.overrideredirect(1)
        self.config(bg='#272727')
        self.img2 = PhotoImage(file='./Login/side.png')
        Label(self, image=self.img2,border=0).place(x=0, y=0)
        self.name=Label(self,text="Welcome Rahul Studio",font=('Game Of Squids',21,'bold'),bg='#272727')
        self.name.place(x=280,y=70)

        Label(self, text='Loading.....',bg='#272727',font=('Times',14)).place(x=300,y=380)
        imga = PhotoImage(file="./New folder/dot.png")
        imgb = PhotoImage(file="./New folder/ddot.png")

        for i in range(4):
            self.config(bg='#272727')
            l1 = Label(self, image=imga, border=0, relief=SUNKEN, bg='#272727').place(x=380, y=220)
            l2 = Label(self, image=imgb, border=0, relief=SUNKEN, bg='#272727').place(x=400, y=220)
            l3 = Label(self, image=imgb, border=0, relief=SUNKEN, bg='#272727').place(x=420, y=220)
            l4 = Label(self, image=imgb, border=0, relief=SUNKEN, bg='#272727').place(x=440, y=220)
            self.update_idletasks()
            time.sleep(0.3)
            self.config(bg='#272727')
            l1 = Label(self, image=imgb, border=0, relief=SUNKEN, bg='#272727').place(x=380, y=220)
            l2 = Label(self, image=imga, border=0, relief=SUNKEN, bg='#272727').place(x=400, y=220)
            l3 = Label(self, image=imgb, border=0, relief=SUNKEN, bg='#272727').place(x=420, y=220)
            l4 = Label(self, image=imgb, border=0, relief=SUNKEN, bg='#272727').place(x=440, y=220)
            self.update_idletasks()
            time.sleep(0.3)
            self.config(bg='#272727')
            l1 = Label(self, image=imgb, border=0, relief=SUNKEN, bg='#272727').place(x=380, y=220)
            l2 = Label(self, image=imgb, border=0, relief=SUNKEN, bg='#272727').place(x=400, y=220)
            l3 = Label(self, image=imga, border=0, relief=SUNKEN, bg='#272727').place(x=420, y=220)
            l4 = Label(self, image=imgb, border=0, relief=SUNKEN, bg='#272727').place(x=440, y=220)
            self.update_idletasks()
            time.sleep(0.3)
            self.config(bg='#272727')
            l1 = Label(self, image=imgb, border=0, relief=SUNKEN, bg='#272727').place(x=380, y=220)
            l2 = Label(self, image=imgb, border=0, relief=SUNKEN, bg='#272727').place(x=400, y=220)
            l3 = Label(self, image=imgb, border=0, relief=SUNKEN, bg='#272727').place(x=420, y=220)
            l4 = Label(self, image=imga, border=0, relief=SUNKEN, bg='#272727').place(x=440, y=220)
            self.update_idletasks()
            time.sleep(0.3)

        window=Window()
        window.grab_set()




x=App()

x.mainloop()
