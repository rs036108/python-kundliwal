from tkinter import *
from PIL import Image,ImageTk
import pyscreenrec

root=Tk()
root.title("Screen Recoder")
root.geometry("400x600")
root.config(bg="#fff")
root.resizable(False,False)
def start_rec():
    file=Filename.get()
    rec.start_recording(str(file+".mp4"),5)

def pause_rec():
    rec.pause_recording()

def play_rec():
    rec.resume_recording()

def stop_rec():
    rec.stop_recording()

rec=pyscreenrec.ScreenRecorder()
img=PhotoImage(file="./Icon/Back.png")
x=Label(root, image=img,bg='#fff')
x.pack()


icon=PhotoImage(file="./Icon/Untitled-4.png")
Label(root,image=icon,bg='#fff').place(x=70,y=90)

Filename=StringVar()
entry=Entry(root,textvariable=Filename,width=18,font="arial 15")
entry.place(x=100,y=330)
Filename.set("recording125")
start=Button(root,text='Start',font=('Times',22,'bold'),bd=0,command=start_rec)
start.place(x=130,y=225)
img2=PhotoImage(file="./Icon/Play.png")
play=Button(root,image=img2,bd=0,bg='#fff',command=play_rec)
play.place(x=50,y=450)

img3=PhotoImage(file="./Icon/Puse.png")
pause=Button(root,image=img3,bd=0,bg='#fff',command=pause_rec)
pause.place(x=150,y=450)

img4=PhotoImage(file="./Icon/Stop.png")
stop=Button(root,image=img4,bd=0,bg='#fff',command=stop_rec)
stop.place(x=250,y=450)

#img1=PhotoImage(file="./Icon/")


root.mainloop()