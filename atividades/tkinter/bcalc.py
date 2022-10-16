from tkinter import *

expression = ''

def keystroke(event):
    if event.char.isnumeric() or event.char in '+*/-':
        press(event.char)    

def press(num, event=None):
    global expression
    if not event:
        expression += str(num)
    else:
        expression += event.char
    equation.set(expression)

def clear():
    global expression
    expression = ''
    equation.set(expression)

def equalpress(event=None):
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
    except:
        equation.set('error')
        expression = ''

def backspace(event=None):
    global expression
    expression = expression[:-1]
    equation.set(expression)

window = Tk()
window.title('Basic Calculator')
window.resizable(False, False)

equation = StringVar()

# Campo de entrada
display = Entry(
    master=window,
    state='readonly',
    justify='right', 
    font=('Arial', 80),
    width=11,
    fg='Black',
    textvariable=equation
)
display.grid(row=0, column=0, columnspan=4)
display.bind('<KeyPress>', keystroke)
display.bind('<Return>', equalpress)
display.bind('<BackSpace>', backspace)
display.focus()

# Criação de buttons
btn_7 = Button(
    master=window,
    text='7',
    font=('arial', 16),
    height=2,
    background='#F7FDA7',
    activebackground='#F7FDA7',
    command=lambda: press(7) #Função anônima (lambda)
)

btn_7.grid(row=1, column=0, sticky=EW)

btn_8 = Button(
    master=window,
    text='8',
    font=('Arial', 16),
    height=2,
    background='#F7FDA7',
    activebackground='#F7FDA7',
    command=lambda: press(8)
)

btn_8.grid(row=1, column=1, sticky=EW)

btn_9 = Button(
    master=window,
    text='9',
    font=('Arial', 16),
    height=2,
    background='#F7FDA7',
    activebackground='#F7FDA7',
    command=lambda: press(9)
)

btn_9.grid(row=1, column=2, sticky=EW)

btn_minus = Button(
    master=window,
    text='-',
    font=('Arial', 16),
    height=2,
    background='#E7A4F1',
    activebackground='#E7A4F1',
    command=lambda: press('-')
)

btn_minus.grid(row=1, column=3, sticky=EW)

btn_4 = Button(
    master=window,
    text='4',
    font=('Arial', 16),
    height=2,
    background='#F7FDA7',
    activebackground='#F7FDA7',
    command=lambda: press(4)
)

btn_4.grid(row=2, column=0, sticky=EW)

btn_5 = Button(
    master=window,
    text='5',
    font=('Arial', 16),
    height=2,
    background='#F7FDA7',
    activebackground='#F7FDA7',
    command=lambda: press(5)
)

btn_5.grid(row=2, column=1, sticky=EW)

btn_6 = Button(
    master=window,
    text='6',
    font=('Arial', 16),
    height=2,
    background='#F7FDA7',
    activebackground='#F7FDA7',
    command=lambda: press(6)
)

btn_6.grid(row=2, column=2, sticky=EW)

btn_plus = Button(
    master=window,
    text='+',
    font=('Arial', 16),
    height=2,
    background='#E7A4F1',
    activebackground='#E7A4F1',
    command=lambda: press('+')
)

btn_plus.grid(row=2, column=3, sticky=EW)

btn_3 = Button(
    master=window,
    text='3',
    font=('Arial', 16),
    height=2,
    background='#F7FDA7',
    activebackground='#F7FDA7',
    command=lambda: press(3)
)

btn_3.grid(row=3, column=0, sticky=EW)

btn_2 = Button(
    master=window,
    text='2',
    font=('Arial', 16),
    height=2,
    background='#F7FDA7',
    activebackground='#F7FDA7',
    command=lambda: press(2)
)

btn_2.grid(row=3, column=1, sticky=EW)

btn_1 = Button(
    master=window,
    text='1',
    font=('Arial', 16),
    height=2,
    background='#F7FDA7',
    activebackground='#F7FDA7',
    command=lambda: press(1)
)

btn_1.grid(row=3, column=2, sticky=EW)

btn_division = Button(
    master=window,
    text='/',
    font=('Arial', 16),
    height=2,
    background='#E7A4F1',
    activebackground='#E7A4F1',
    command=lambda: press('/')
)

btn_division.grid(row=3, column=3, sticky=EW)

btn_clear = Button(
    master=window,
    text='C',
    font=('Arial', 16),
    height=2,
    background='orange',
    activebackground='orange',
    command=clear
)

btn_clear.grid(row=4, column=0, sticky=EW)

btn_0 = Button(
    master=window,
    text='0',
    font=('Arial', 16),
    height=2,
    background='#F7FDA7',
    activebackground='#F7FDA7',
    command=lambda: press(0)
)

btn_0.grid(row=4, column=1, sticky=EW)

btn_equal = Button(
    master=window,
    text='=',
    font=('Arial', 16),
    height=2,
    foreground='white',
    background='dark red',
    activebackground='dark red',
    command=equalpress
)

btn_equal.grid(row=4, column=2, sticky=EW)

btn_mult = Button(
    master=window,
    text='X',
    font=('Arial', 16),
    height=2,
    background='#E7A4F1',
    activebackground='#E7A4F1',
    command=lambda: press('*')
)

btn_mult.grid(row=4, column=3, sticky=EW)

window.mainloop()