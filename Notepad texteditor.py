from tkinter import *
from tkinter import filedialog,simpledialog
global cur_open_file
cur_open_file="no_file"
def cmds(event=""):

    result=filedialog.askopenfile(initialdir="/",title="select File", filetypes=(("text file",".txt"),("all file","*")))
    if (result != None):
        text.delete(1.0,END)
        for line in result:
         text.insert(END,line)
        global cur_open_file
        cur_open_file=result.name
        result.close()
        print(cur_open_file)
    p()
def p():
    print(cur_open_file)
def save(event=""):
    if cur_open_file =="no_file":
        saveas()
    else :
        f=open(cur_open_file,"w+")
        f.write(text.get(1.0,END))
        f.close()
def saveas(event=""):
    f=filedialog.asksaveasfile(mode="w", title="Save as", defaultextension=".txt")
    if f is None:
        return
    savev= text.get(1.0,END)
    cur_open_file = f.name
    f.write(savev)
    f.close()

def copy () :
    text.clipboard_clear()
    text.clipboard_append(text.selection_get())

def cut ():
    copy()
    text.delete("sel.first", "sel.last")

def paste():
    text.insert(INSERT,text.clipboard_get())

def pop_menu(event):
    p_menu.tk_popup(event.x_root,event.y_root)

root=Tk()
root.title("Rahul Kundliwal")
text=Text(width=300,height=300,wrap=WORD,undo=True)
text.pack()

main_menu=Menu(root)
root.config(menu=main_menu)
File_menu=Menu(main_menu,tearoff=0)
main_menu.add_cascade(label="File", menu=File_menu)

root.bind('<Control-o>' , cmds)
File_menu.add_command(label="Open",command=cmds)
root.bind('<Control-s>',save)
File_menu.add_command(label="Save",command=save)
root.bind('<Control-Alt-s>',saveas)
File_menu.add_command(label="Save as..",command=saveas)
File_menu.add_command(label="Page Setup..",command=save)
File_menu.add_command(label="Print",command=save)
File_menu.add_command(label="Exit",command=root.quit)
Edit_menu=Menu(main_menu, tearoff=0)
main_menu.add_cascade(label="Edit", menu=Edit_menu)
Edit_menu.add_command(label="Undo", command=text.edit_undo)
Edit_menu.add_command(label="Redo", command=text.edit_redo)
root.bind('<Control-x>')
Edit_menu.add_command(label="Cut", command=cut)
root.bind('<Contro-c>')
Edit_menu.add_command(label="Copy", command=copy)
root.bind('<Control-v>')
Edit_menu.add_command(label="Paste", command=paste)
root.bind('<Control-d>')
p_menu=Menu(tearoff=0,bg="black",fg="cyan")
p_menu.add_command(label="Copy",command=copy)
p_menu.add_command(label="Paste",command=paste)
p_menu.add_command(label="Cut",command=cut)
p_menu.add_command(label="Undo",command=text.edit_undo)


root.geometry("1280x700")
root.bind("<Button-3>",pop_menu)
root.mainloop()
