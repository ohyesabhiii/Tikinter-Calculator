from tkinter import *
import tkinter.messagebox
window = Tk()
'''inp = Label(window, text = "hello world")
inp.pack()
window.mainloop()
window.title("simple")
'''

window.geometry("350x425")
'''
window.config(bg="yellow")
frame1=Frame(window, width="300", height="300", cursor="dot")
frame2=Frame(window, width="300", height="300", cursor= "dotbox")
button1=Button(frame1, text="Button1", bg="blue")
button2=Button(frame2, text="Button2", bg="green")
button3=Button(frame1, text="Button3", bg="green")
button1.pack()
button2.pack()
button3.pack()
frame1.pack(side=TOP)
frame2.pack(side=BOTTOM)
'''
'''
window.geometry("500x500")

label1 = Label(window, text="mail")
label1.grid(row  =0, column = 1)
label2 = Label(window, text="password")
label2.grid(row  =1, column = 1)
e1 = Entry(window, width=40, borderwidth=5)
e1.grid(row=0, column=2)
e2 = Entry(window, width=40, borderwidth=5)
e2.grid(row=1, column=2)
'''
'''
label1 = Label(window, text="label 1", bg="red", fg="white")
label1.pack(side= TOP, fill= X, expand = False)
label2 = Label(window, text="label 2", bg="blue", fg="white")
label2.pack(side= LEFT, fill= Y, expand = False)
label3 = Label(window, text="label 3", bg="green", fg="white")
label3.pack(side= RIGHT, fill= Y, expand = False)

'''
'''
def log_entry():
    print("logged in")
button= Button(window , text= "login", command= log_entry, width= 12, bg= "red", fg= "white", font=("bold", 12), activebackground="black", activeforeground="white")
button.pack()
'''
'''
menu=Menu(window)
file=Menu(menu, tearoff=0)
file.add_command(label="new")
file.add_cascade(label="open")
file.add_command(label="save")
file.add_command(label="save as")
file.add_separator()
file.add_command(label="exit", command=window.quit)
menu.add_cascade(label="file", menu=file)
window.config(menu=menu)
'''
'''
question= tkinter.messagebox.askyesno("weather", "will it rain?")
if question== True:
    tkinter.messagebox.showinfo("info", "take an umbrella")
else:
    tkinter.messagebox.showinfo("info", "okay")
'''
'''
c= Canvas(window, width=500, height= 500)
c.pack()
c.create_line(0,0,500,500, width=5, fill="green", dash=(3,3))
c.create_line(0,500,500,0, width=5, fill="blue", dash=(3,3))
c.create_rectangle(150,125,450,375)
mainloop()
'''
e= Entry(window, width=56, borderwidth=5)
e.place(x=0, y=0)
def click(num):
    result=e.get()
    e.delete(0,END)
    e.insert(0,str(result)+str(num))
b= Button(window, text="1", width=12, command= lambda:click(1))
b.place(x=10,y=60)
b= Button(window, text="2", width=12, command= lambda:click(2))
b.place(x=80,y=60)
b= Button(window, text="3", width=12, command= lambda:click(3))
b.place(x=170,y=60)
b= Button(window, text="4", width=12, command= lambda:click(4))
b.place(x=10,y=120)
b= Button(window, text="5", width=12, command= lambda:click(5))
b.place(x=80,y=120)
b= Button(window, text="6", width=12, command= lambda:click(6))
b.place(x=170,y=120)
b= Button(window, text="7", width=12, command= lambda:click(7))
b.place(x=10,y=180)
b= Button(window, text="8", width=12, command= lambda:click(8))
b.place(x=80,y=180)
b= Button(window, text="9", width=12, command= lambda:click(9))
b.place(x=170,y=180)
b= Button(window, text="0", width=12, command= lambda:click(0))
b.place(x=10,y=240)
def add():
    n1=e.get()
    global math
    math="addition"
    global i
    i=int(n1)
    e.delete(0,END)

b= Button(window, text="+", width=12, command= add)
b.place(x=80,y=240)
def sub():
    n1=e.get()
    global math
    math = "subtraction"
    global i
    i=int(n1)
    e.delete(0,END)
b= Button(window, text="-", width=12, command= sub)
b.place(x=170,y=240)
def mul():
    n1=e.get()
    global math
    math = "multiplication"
    global i
    i=int(n1)
    e.delete(0,END)
b= Button(window, text="*", width=12, command= mul)
b.place(x=10,y=300)
def div():
    n1=e.get()
    global math
    math = "division"
    global i
    i=int(n1)
    e.delete(0,END)
b= Button(window, text="/", width=12, command= div)
b.place(x=80,y=300)
def equal():
    n2=e.get()
    e.delete(0,END)
    if math=="addition":
        e.insert(0,i+int(n2))
    elif math=="subtraction":
        e.insert(0,i-int(n2))
    elif math=="multiplication":
        e.insert(0,i*int(n2))
    elif math=="division":
        e.insert(0,i/int(n2) )



b= Button(window, text="=", width=12, command= equal)
b.place(x=170,y=300)
def clear():
    e.delete(0, END)
b= Button(window, text="clear", width=12, command= clear)
b.place(x=10,y=360)


mainloop()