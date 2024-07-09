from tkinter import *
import math

# Create the main window
window = Tk()
window.title("Scientific Calculator")
window.geometry("450x450")
window.configure(bg='#282c34')

# Entry widget for displaying numbers and results
e = Entry(window, width=17, borderwidth=5, font=('Arial', 24), justify='right', bg='#1c1f24', fg='white')
e.grid(row=0, column=0, columnspan=5, pady=20)

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

# Function to handle scientific operations
def scientific_operation(operation):
    try:
        current_text = e.get()
        if operation == 'sqrt':
            result = math.sqrt(float(current_text))
        elif operation == 'log':
            result = math.log10(float(current_text))
        elif operation == 'ln':
            result = math.log(float(current_text))
        elif operation == 'sin':
            result = math.sin(math.radians(float(current_text)))
        elif operation == 'cos':
            result = math.cos(math.radians(float(current_text)))
        elif operation == 'tan':
            result = math.tan(math.radians(float(current_text)))
        elif operation == 'exp':
            result = math.exp(float(current_text))
        e.delete(0, END)
        e.insert(0, str(result))
    except Exception as ex:
        e.delete(0, END)
        e.insert(0, "Error")

# Button styling
button_font = ('Arial', 14)
button_width = 5
button_height = 2
button_bg = '#3b3f44'
button_fg = 'white'

# Number buttons
numbers = [
    (1, 3, 0), (2, 3, 1), (3, 3, 2),
    (4, 2, 0), (5, 2, 1), (6, 2, 2),
    (7, 1, 0), (8, 1, 1), (9, 1, 2),
    (0, 4, 1)
]
for num, r, c in numbers:
    Button(window, text=str(num), font=button_font, width=button_width, height=button_height, command=lambda n=num: click(n), bg=button_bg, fg=button_fg).grid(row=r, column=c, padx=5, pady=5)

# Operator buttons
operators = [
    ('+', 4, 3), ('-', 3, 3), ('*', 2, 3), ('/', 1, 3),
    ('.', 4, 2), ('(', 5, 0), (')', 5, 1), ('^', 5, 2)
]
for op, r, c in operators:
    Button(window, text=str(op), font=button_font, width=button_width, height=button_height, command=lambda o=op: click(o), bg=button_bg, fg=button_fg).grid(row=r, column=c, padx=5, pady=5)

# Scientific buttons
scientific_operations = [
    ('sqrt', 1, 4), ('log', 2, 4), ('ln', 3, 4),
    ('sin', 4, 4), ('cos', 5, 4), ('tan', 5, 3),
    ('exp', 4, 0)
]
for op, r, c in scientific_operations:
    Button(window, text=str(op), font=button_font, width=button_width, height=button_height, command=lambda o=op: scientific_operation(o), bg=button_bg, fg=button_fg).grid(row=r, column=c, padx=5, pady=5)

# Equal and clear buttons
Button(window, text="=", font=button_font, width=button_width, height=button_height, command=calculate, bg='#d35400', fg='white').grid(row=4, column=5, padx=5, pady=5)
Button(window, text="C", font=button_font, width=button_width, height=button_height, command=clear, bg='#c0392b', fg='white').grid(row=5, column=5, padx=5, pady=5)

mainloop()
