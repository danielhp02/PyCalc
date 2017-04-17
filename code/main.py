import tkinter as tk
from time import sleep

# Create window
window = tk.Tk()

# Set the title and size of the window
window.title("PyCalc")
# window.geometry("640x480")

# Set the icon of the window (.gif)
if __file__ == 'code/main.py':
    img = tk.PhotoImage(file='./assets/favicon.gif')
elif __file__ == 'main.py':
    img = tk.PhotoImage(file='../assets/favicon.gif')

try:
    window.tk.call('wm', 'iconphoto', window._w, img)
except NameError:
    print("Icon image not found: please ensure that you are executing from either the 'PyCalc' or 'code' directories.")

def enter():
    eq = ent.get()
    ent.delete(0, tk.END)

    ent.insert(0, '{0:g}'.format(float(eval(eq))))

def onButtonClick(btn_id):
    global ent
    ent.insert(tk.END, str(btn_id))

# Widgets
ent = tk.Entry(window)
ent.grid(columnspan=4)

buttons = []
for num in range(10):
    btn = tk.Button(window, text=num, font='monospace', command=lambda num=num: onButtonClick(num))
    buttons.append(btn)

for symbol in ['.', '=', '/', '*', '-', '+']:
    btn = tk.Button(window, text=symbol, font='monospace', command=lambda symbol=symbol: onButtonClick(symbol))
    buttons.append(btn)

buttons[11] = tk.Button(window, text='=', font='monospace', command=enter)

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

# Check input and update and things
window.mainloop()
