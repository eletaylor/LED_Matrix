from tkinter import *
from tkinter import messagebox


def createGrid():
    for i in range(rows):
        for j in range(columns):
            btns[i][j] = Button(tk, bg="gray")
            btns[i][j]['command'] = lambda btn=btns[i][j]: color(btn)
            btns[i][j].grid(row=i, column=j)


def createColorButtons():
    for i in range(len(colors)):
        if colors[i] == "White" or colors[i] == "Yellow":
            colorButtons[i] = Button(tk, text=colors[i], fg='black', bg=colors[i].lower())
        else:
            colorButtons[i] = Button(tk, text=colors[i], fg='white', bg=colors[i].lower())

        colorButtons[i]['command'] = lambda btn=colorButtons[i]: changeColor(btn)
        colorButtons[i].grid(row=i + 5, column=20)


def createClearandErase():
    global clearButton
    clearButton = Button(tk, text="Clear", fg="white", bg="gray")
    clearButton.grid(row=13, column=20)
    clearButton['command'] = lambda btn=clearButton: clear(btn)

    global eraseButton
    eraseButton = Button(tk, text="Erase", fg="white", bg="gray")
    eraseButton.grid(row=14, column=20)
    eraseButton['command'] = lambda btn=eraseButton: eraser(btn)


def clear(btn):
    if messagebox.askyesno("Confirm Clear", "Are you sure you want to clear?"):
        reset()
        for i in range(rows):
            for j in range(columns):
                btns[i][j]['bg'] = "gray"


def reset():
    global userColor
    global erase
    userColor = blankColor
    erase = False


def eraser(btn):
    global erase
    erase = True
    messagebox.showinfo("Erase Activated", "Erase activated.")


def color(btn):
    if userColor == blankColor and erase is False:
        messagebox.showinfo("No Color Selected", "No color selected. Please choose a color on the right-hand side "
                            + "of the screen.")
    elif erase:
        btn['bg'] = blankColor
    else:
        btn['bg'] = userColor


def changeColor(btn):
    global userColor
    userColor = btn['bg']

    global erase
    if erase:
        erase = False
        messagebox.showinfo("Color Changed", "Erase deactivated. The active color is " + userColor)
    else:
        messagebox.showinfo("Color Changed", "The active color is " + userColor)


def on_closing():
    if messagebox.askokcancel("Quit", "Are you sure you want to quit?"):
        reset()
        tk.destroy()


rows = 16
columns = 16
btns = [[None for i in range(rows)] for j in range(columns)]
colors = ["White", "Red", "Green", "Blue", "Black", "Cyan", "Yellow"]
colorButtons = [None for i in range(len(colors))]
clearButton = None
eraseButton = None
blankColor = "gray"
userColor = blankColor
erase = False

tk = Tk()
tk.title("Pixel Board")
tk.attributes('-fullscreen', True)

createGrid()
createColorButtons()
createClearandErase()

tk.protocol("WM_DELETE_WINDOW", on_closing)
tk.mainloop()
