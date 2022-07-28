from tkinter import *
from tkinter import messagebox

root=Tk()
root.resizable(False,False)
root.geometry('925x500+300+100')
frame=Frame(root,height=350,width=350,bg='white')
frame.place(x=480,y=70)

def on_enter(e):
    user.delete(0,'end')


def on_leave(e) :
    name=user.get()
    if name=='':
        user.insert(0,'Username')

def sign_in():
    username=user.get()
    password=code.get()

    if username=='admin' and password=='1234':
        screen = Toplevel(root)
        screen.title("App")
        screen.geometry("925x500+300+200")
        screen.config(bg='white')
        Label(screen,text='sign up sucessfully',font=('Times',20,'bold'),bg='white').pack(expand=True)
        screen.mainloop()
    elif username!='admin' and password!='1234':
        messagebox.showerror("Invaldi username and password")
    elif username!='admin':
        messagebox.showerror("Invalid username")
    elif password!='1234':
        messagebox.showerror("Invalid password")
la=Label(frame, text='Sign in',bg='white',font=('Times',20,'bold'))
la.place(x=100,y=5)
user=Entry(frame,width=25,fg='black',border=0,bg='white',font=('Times',11))
user.place(x=30,y=80)
user.insert(0,'Username')
user.bind('<FocusIn>',on_enter)
user.bind('<FocusOut>',on_leave)
Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)


def on_enter(f):
    code.delete(0,'end')
def on_leave(f):
    passw =code.get()
    if code=='':
        code.insert(0,'Password')


code=Entry(frame,width=25,fg='black',border=0,bg='white',font=('Times',11))
code.place(x=30,y=150)
code.insert(0,'Password')
code.bind('<FocusIn>',on_enter)
code.bind('<FocusOut>',on_leave)
Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)



Button(frame,width=35, pady=7,text='Sign in',bg="red",border=0,fg='White',command=sign_in).place(x=45,y=215)
lable=Label(frame,text="Don't Have an acount ?",fg='black',bg='white')
lable.place(x=75,y=270)
sign_up=Button(frame,width=6,text="Sign up",cursor='hand2',border=0,bg='white',fg='blue')
sign_up.place(x=215,y=270)

root.mainloop()


