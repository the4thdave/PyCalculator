from tkinter import *
from tkinter import ttk

#Commands
def add_one():
    s = screen_text.get()
    s += '1'
    screen_text.set(s)

def add_two():
    s = screen_text.get()
    s += '2'
    screen_text.set(s)

def add_three():
    s = screen_text.get()
    s += '3'
    screen_text.set(s)

def add_four():
    s = screen_text.get()
    s += '4'
    screen_text.set(s)

def add_five():
    s = screen_text.get()
    s += '5'
    screen_text.set(s)

def add_six():
    s = screen_text.get()
    s += '6'
    screen_text.set(s)

def add_seven():
    s = screen_text.get()
    s += '7'
    screen_text.set(s)

def add_eight():
    s = screen_text.get()
    s += '8'
    screen_text.set(s)

def add_nine():
    s = screen_text.get()
    s += '9'
    screen_text.set(s)

def add_zero():
    s = screen_text.get()
    s += '0'
    screen_text.set(s)

def add_decimal():
    s = screen_text.get()
    s += '.'
    screen_text.set(s)

def all_clear():
    screen_text.set("")

def negatize():
    s = screen_text.get()
    num = IntVar()
    if '.' in s:
        num = float(s) * -1
        screen_text.set(num)
    else:
        num = int(s) * -1
        screen_text.set(num)

def percent():
    s = screen_text.get()
    num = IntVar()
    if '.' in s:
        num = float(s) * 0.01
        screen_text.set(num)
    else:
        num = int(s) * 0.01
        screen_text.set(num)

#Calculator Functions
class Calculator:
    calc_value = 0.0

    div_check = False
    multi_check = False
    add_check = False
    sub_check = False

    def isfloat(self, str_val):
        try:
            float(str_val)
            return True
        except ValueError:
            return False

    def function_press(self, value):
        if self.isfloat(screen_text.get()):
            self.div_check = False
            self.multi_check = False
            self.add_check = False
            self.sub_check = False

        self.calc_value = float(screen_text.get())

        if value == "/":
            print("/ Pressed")
            self.div_check = True
        elif value == "*":
            print("* Pressed")
            self.multi_check = True
        elif value == "+":
            print("+ Pressed")
            self.add_check = True
        else:
            print("- Pressed")
            self.sub_check = True

        screen_text.set("")

    def equal_press(self):
        if self.div_check or self.multi_check or self.add_check or self.sub_check:
            if self.div_check:
                answer = self.calc_value / float(screen_text.get())
            elif self.multi_check:
                answer = self.calc_value * float(screen_text.get())
            elif self.add_check:
                answer = self.calc_value + float(screen_text.get())
            else:
                answer = self.calc_value - float(screen_text.get())

            print(self.calc_value, " ", float(screen_text.get()), " ", answer)

            screen_text.set(str(answer))

    def __init__(self, root):
        self.button_add = ttk.Button(frame, text="+", command=lambda: self.function_press('+')).grid(row=5, column=4)
        self.button_sub = ttk.Button(frame, text="-", command=lambda: self.function_press('-')).grid(row=4, column=4)
        self.button_multi = ttk.Button(frame, text="x", command=lambda: self.function_press('*')).grid(row=3, column=4)
        self.button_div = ttk.Button(frame, text="÷", command=lambda: self.function_press('/')).grid(row=2, column=4)
        self.button_equals = ttk.Button(frame, text="=", command=lambda: self.equal_press()).grid(row=6, column=4)
        root.bind("<Return>", lambda event: self.equal_press())

root = Tk()
root.title("Calculator")

#Frame
frame = ttk.Frame(root, padding="20 20 40 40")
frame.grid(row=0, column=0)

#Calculator Screen
screen_text = StringVar()
screen = ttk.Label(frame, textvariable=screen_text, borderwidth=1, relief="solid", width=38, anchor=E)
screen.grid(row=1, column=1, columnspan=4)

#Buttons
ttk.Button(frame, text="AC", command=all_clear).grid(row=2, column=1)
ttk.Button(frame, text="+/-", command=negatize).grid(row=2, column=2)
ttk.Button(frame, text="%", command=percent).grid(row=2, column=3)
ttk.Button(frame, text="7", command=add_seven).grid(row=3, column=1)
ttk.Button(frame, text="8", command=add_eight).grid(row=3, column=2)
ttk.Button(frame, text="9", command=add_nine).grid(row=3, column=3)
ttk.Button(frame, text="4", command=add_four).grid(row=4, column=1)
ttk.Button(frame, text="5", command=add_five).grid(row=4, column=2)
ttk.Button(frame, text="6", command=add_six).grid(row=4, column=3)
ttk.Button(frame, text="1", command=add_one).grid(row=5, column=1)
ttk.Button(frame, text="2", command=add_two).grid(row=5, column=2)
ttk.Button(frame, text="3", command=add_three).grid(row=5, column=3)
ttk.Button(frame, text="0", width=16, command=add_zero).grid(row=6, column=1, columnspan=2)
ttk.Button(frame, text=".", command=add_decimal).grid(row=6, column=3)

#Bindings
root.bind("1", lambda event: add_one())
root.bind("2", lambda event: add_two())
root.bind("3", lambda event: add_three())
root.bind("4", lambda event: add_four())
root.bind("5", lambda event: add_five())
root.bind("6", lambda event: add_six())
root.bind("7", lambda event: add_seven())
root.bind("8", lambda event: add_eight())
root.bind("9", lambda event: add_nine())
root.bind("0", lambda event: add_zero())
root.bind(".", lambda event: add_decimal())
root.bind("<BackSpace>", lambda event: all_clear())

calc = Calculator(root)

root.mainloop()