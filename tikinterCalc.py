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
