import tkinter as tk
import math

# Create root window
root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("500x500")
root.resizable(False, False)

# Expression variable
expression = ""
input_text = tk.StringVar()

# Input field
input_frame = tk.Frame(root, bd=10, relief=tk.RIDGE)
input_frame.pack(side=tk.TOP, fill=tk.X)

input_field = tk.Entry(input_frame, font=('arial', 18, 'bold'),
                       textvariable=input_text, width=40, bd=5, justify=tk.RIGHT)
input_field.pack(ipady=15)

# Scrollable frame for buttons
canvas = tk.Canvas(root, height=500)
scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
scrollable_frame = tk.Frame(canvas)

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# Functions
def btn_click(item):
    global expression
    expression += str(item)
    input_text.set(expression)

def btn_clear():
    global expression
    expression = ""
    input_text.set("")

def btn_backspace():
    global expression
    expression = expression[:-1]
    input_text.set(expression)


def btn_equal():
    global expression
    try:
        result = str(eval(expression))
        input_text.set(result)
        expression = result
    except:
        input_text.set("Error")
        expression = ""

def btn_scientific(func):
    global expression
    try:
        value = eval(expression)
        if func == "sin":
            result = math.sin(math.radians(value))
        elif func == "cos":
            result = math.cos(math.radians(value))
        elif func == "tan":
            result = math.tan(math.radians(value))
        elif func == "sqrt":
            result = math.sqrt(value)
        elif func == "log":
            result = math.log10(value)
        elif func == "ln":
            result = math.log(value)
        elif func == "exp":
            result = math.exp(value)
        elif func == "pow":
            result = math.pow(value, 2)
        input_text.set(str(result))
        expression = str(result)
    except:
        input_text.set("Error")
        expression = ""

# Button Layout
buttons = [
    ['C', '⌫', 'exp', 'pi', 'e'],
    ['(', ')', 'log', 'ln', 'pow'],
    ['7', '8', '9', '/', 'sin'],
    ['4', '5', '6', '*', 'cos'],
    ['1', '2', '3', '-', 'tan'],
    ['0', '.', '=', '+', 'sqrt']
]


# Generate Buttons
for row_idx, row in enumerate(buttons):
    for col_idx, item in enumerate(row):
        if item == "=":
            btn = tk.Button(scrollable_frame, text=item, fg="white", bg="green", font=('arial', 14, 'bold'),
                            width=7, height=2, command=btn_equal)
        elif item == "C":
            btn = tk.Button(scrollable_frame, text=item, fg="white", bg="red", font=('arial', 14, 'bold'),
                            width=7, height=2, command=btn_clear)
        elif item in ["sin", "cos", "tan", "sqrt", "log", "ln", "exp", "pow"]:
            btn = tk.Button(scrollable_frame, text=item, fg="white", bg="orange", font=('arial', 14, 'bold'),
                            width=7, height=2, command=lambda f=item: btn_scientific(f))
        elif item == "pi":
            btn = tk.Button(scrollable_frame, text=item, fg="white", bg="blue", font=('arial', 14, 'bold'),
                            width=7, height=2, command=lambda: btn_click(str(math.pi)))
        elif item == "e":
            btn = tk.Button(scrollable_frame, text=item, fg="white", bg="blue", font=('arial', 14, 'bold'),
                            width=7, height=2, command=lambda: btn_click(str(math.e)))
        elif item == "⌫":
              btn = tk.Button(scrollable_frame, text=item, fg="white", bg="black", font=('arial', 14, 'bold'),
                    width=7, height=2, command=btn_backspace)
        else:
            btn = tk.Button(scrollable_frame, text=item, font=('arial', 14, 'bold'),
                            width=7, height=2, command=lambda x=item: btn_click(x))
        btn.grid(row=row_idx, column=col_idx, padx=1, pady=1)

root.mainloop()
