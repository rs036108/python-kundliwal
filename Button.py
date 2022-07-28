from tkinter import *
from tkinter import filedialog,simpledialog
root=Tk()
root.title("Rahul Kundliwal")

def pop_menu(event):
    menu.tk_popup(event.x_root,event.y_root)

menu=Menu(tearoff=0,bg="black", fg="white")
menu.add_command(label="Cut")
menu.add_command(label="Paste")
menu.add_command(label="Cut")
menu.add_command(label="Cut")





text=Text(width=300,height=300,wrap=WORD)
text.pack()
text.bind("<Button-3>",pop_menu)
root.geometry("1280x700")
root.mainloop()

