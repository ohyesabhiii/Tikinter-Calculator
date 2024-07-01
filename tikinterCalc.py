from tkinter import *

# Create the main window
window = Tk()
window.title("Simple Calculator")
window.geometry("260x290")
window.configure(bg='#282c34')

# Entry widget for displaying numbers and results
e = Entry(window, width=15, borderwidth=5, font=('Arial', 20), justify='right', bg='#1c1f24', fg='white')
e.grid(row=0, column=0, columnspan=4)

# Function to handle button click for numbers and operators
def click(char):
    current_text = e.get()
    e.delete(0, END)
    e.insert(END, current_text + str(char))

# Function to clear the entry widget
def clear():
    e.delete(0, END)

# Function to perform calculations
def calculate():
    try:
        current_text = e.get()
        result = eval(current_text)
        e.delete(0, END)
        e.insert(0, str(result))
    except Exception as ex:
        e.delete(0, END)
        e.insert(0, "Error")

# Button styling
button_font = ('Arial', 14)
button_width = 5
button_height = 2

# Number buttons
numbers = [
    (1, 3, 0), (2, 3, 1), (3, 3, 2),
    (4, 2, 0), (5, 2, 1), (6, 2, 2),
    (7, 1, 0), (8, 1, 1), (9, 1, 2),
    (0, 4, 1)
]
for num, r, c in numbers:
    Button(window, text=str(num), font=button_font, width=button_width, height=button_height, command=lambda n=num: click(n), bg='#61afef', fg='black').grid(row=r, column=c)

# Operator buttons
operators = [
    ('+', 4, 3), ('-', 3, 3), ('*', 2, 3), ('/', 1, 3),
    ('.', 4, 0)
]
for op, r, c in operators:
    Button(window, text=str(op), font=button_font, width=button_width, height=button_height, command=lambda o=op: click(o), bg='#00008B', fg='white').grid(row=r, column=c)

# Equal and clear buttons
Button(window, text="=", font=button_font, width=button_width, height=button_height, command=calculate, bg='#00008B', fg='white').grid(row=4, column=2)
Button(window, text="C", font=button_font, width=button_width, height=button_height, command=clear, bg='#00008B', fg='white').grid(row=4, column=0)

mainloop()

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
