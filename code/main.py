import tkinter
window = tkinter.Tk()

# Set the title and size of the window
window.title("PyCalc")
window.geometry("640x480")

# Set the icon of the window (.gif)
if __file__ == 'code/tkintertest.py':
    img = tkinter.PhotoImage(file='./assets/favicon.gif')
elif __file__ == 'tkintertest.py':
    img = tkinter.PhotoImage(file='../assets/favicon.gif')

try:
    window.tk.call('wm', 'iconphoto', window._w, img)
except NameError:
    print("Icon image not found: please ensure that you are executing from either the 'PyCalc' or 'code' directories.")
# Check input and update and things
window.mainloop()
