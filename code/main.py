import tkinter as tk
import os

os.system('xset r off')

# Create window
root = tk.Tk()

# Set the title and size of the window
root.title("PyCalc")

# Set the icon of the window (.gif)
if __file__ == 'code/main.py':
    img = tk.PhotoImage(file='./assets/favicon.gif')
elif __file__ == 'main.py':
    img = tk.PhotoImage(file='../assets/favicon.gif')

try:
    root.tk.call('wm', 'iconphoto', root._w, img)
except NameError:
    print("Icon image not found: please ensure that you are executing from either the 'PyCalc' or 'code' directories.")

def enter(event=None):
    try:
        eq = ent.get()

        ent.delete(0, tk.END)
        ent.insert(0, '{0:g}'.format(float(eval(eq))))
    except SyntaxError:
        print("Either something wrong or nothing to evaluate.")

def backspace(event=None):
    text = ent.get()[:-1]
    ent.delete(0, tk.END)
    ent.insert(0, text)

def clear():
    ent.delete(0, tk.END)

def onButtonClick(btn_id):
    global ent
    ent.insert(tk.END, str(btn_id))

# Widgets
ent = tk.Entry(root)
ent.grid(columnspan=4)

buttonSymbols = []
buttons = []
for num in range(10):
    btn = tk.Button(root, text=num, font='monospace', command=lambda num=num: onButtonClick(num))
    buttons.append(btn)
    buttonSymbols.append(num)

for symbol in ['.', '=', '/', '*', '-', '+']:
    btn = tk.Button(root, text=symbol, font='monospace', command=lambda symbol=symbol: onButtonClick(symbol))
    buttons.append(btn)
    buttonSymbols.append(symbol)

buttons[11] = tk.Button(root, text='=', font='monospace', command=enter)

# Draw buttons, 0-9 are the corresponding numbers, 10 and up are symbols
buttons[9].grid(row=1, column=2)
buttons[8].grid(row=1, column=1)
buttons[7].grid(row=1, column=0)
buttons[6].grid(row=2, column=2)
buttons[5].grid(row=2, column=1)
buttons[4].grid(row=2, column=0)
buttons[3].grid(row=3, column=2)
buttons[2].grid(row=3, column=1)
buttons[1].grid(row=3, column=0)
buttons[0].grid(row=4, column=0)

buttons[10].grid(row=4, column=1) # .
buttons[11].grid(row=4, column=2) # =
buttons[12].grid(row=1, column=3) # /
buttons[13].grid(row=2, column=3) # *
buttons[14].grid(row=3, column=3) # -
buttons[15].grid(row=4, column=3) # +

root.bind('<Return>', enter)
root.bind('<BackSpace>', backspace)

# Check input and update and things
root.mainloop()

os.system('xset r on')
