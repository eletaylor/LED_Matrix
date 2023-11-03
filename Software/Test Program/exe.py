from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import board
import neopixel
import os

#data_pin is for the data pin to be wired to. 
#Must use GPIO10 for sudoless control of leds (physical pin 19)
data_pin = board.D10

#num_lights holds the number of LED's to be programmed
num_lights = 64

pixel1 = neopixel.NeoPixel(
    data_pin, num_lights, brightness = 0.2,
    auto_write = True, pixel_order = neopixel.RGB
    )



def createGrid():
    global blankColor
    for i in range(rows):
        for j in range(columns):
            btns[i][j] = Button(tk, bg=blankColor)
            btns[i][j]['command'] = lambda btn=btns[i][j]: color(btn)
            btns[i][j].grid(row=i + 1, column=j)
            Grid.rowconfigure(tk, index=i + 1, weight=1)


def createColorButtons():
    for i in range(len(colors)):
        if colors[i] == "White" or colors[i] == "Yellow":
            colorButtons[i] = Button(tk, text=colors[i], fg='black', bg=colors[i].lower())
        else:
            colorButtons[i] = Button(tk, text=colors[i], fg='white', bg=colors[i].lower())

        colorButtons[i]['command'] = lambda btn=colorButtons[i]: changeColor(btn)
        colorButtons[i].grid(row=i + 7, column=35)


def createClearAndErase():
    global clearButton
    clearButton = Button(tk, text="Clear", fg="white", bg="gray")
    clearButton.grid(row=15, column=35)
    clearButton['command'] = lambda btn=clearButton: clear(btn)

    global eraseButton
    eraseButton = Button(tk, text="Erase", fg="white", bg="gray")
    eraseButton.grid(row=16, column=35)
    eraseButton['command'] = lambda btn=eraseButton: eraser(btn)


def createMenuTab():
    global menuStrip
    global file

    menuStrip = Menu(tk)
    file = Menu(menuStrip, tearoff=0)

    menuStrip.add_cascade(label="File", menu=file)
    file.add_command(label="Open Design", command=lambda: open_file())
    file.add_command(label="Save Design", command=lambda: save_file())
    menuStrip.add_command(label="Exit", command=lambda: on_closing())


def createFolders():
    if not (os.path.exists(path)):
        os.makedirs(path)


def clear(btn):
    global boardClear
    global blankColor
    if boardClear is False:
        if messagebox.askyesno("Confirm Clear", "Are you sure you want to clear?"):
            reset()
            for i in range(rows):
                for j in range(columns):
                    btns[i][j]['bg'] = blankColor
    else:
        messagebox.showinfo("Grid Empty", "Grid empty. Nothing to clear.")


def reset():
    global userColor
    global erase
    global boardClear
    userColor = blankColor
    erase = False
    boardClear = True


def eraser(btn):
    global erase
    global boardClear
    if boardClear is False:
        messagebox.showinfo("Erase Activated", "Erase activated.")
        erase = True
    else:
        messagebox.showinfo("Grid Empty", "Grid empty. Nothing to erase.")


def color(btn):
    global boardClear
    if userColor == blankColor and erase is False:
        messagebox.showinfo("No Color Selected", "No color selected. Please choose a color on the right-hand side "
                            + "of the screen.")
    elif erase:
        btn['bg'] = blankColor
        boardClear = False
    else:
        btn['bg'] = userColor
        boardClear = False


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


def open_file():
    global erase
    global boardClear
    global userColor
    global blankColor
    counter = 0
    erase = False
    boardClear = False
    userColor = blankColor
    
    openFile = filedialog.askopenfile(initialdir=path, title="Open Design")
    colorArray = openFile.readlines()
    colorArray = [x.strip() for x in colorArray]
    for i in range(rows):
        for j in range(columns):
            btns[i][j]['bg'] = colorArray[counter]
            counter += 1


def save_file():
    global erase
    global boardClear
    global userColor
    global blankColor
    erase = False
    boardClear = False
    userColor = blankColor
    
    saveFile = filedialog.asksaveasfile(defaultextension=".txt", initialdir=path, title="Save Design")
    for i in range(rows):
        for j in range(columns):
            saveFile.write(btns[i][j]['bg'] + "\n")


def getIndex(i, j):
    if j <= 7:
        if i % 2 == 0:
            index = 8 * i + j
        else:
            index = 8 * i + (8 - (j + 1))
    else:
        if i % 2 == 0:
            index = 8 * (15 + i) + j
        else:
            index = 8 * (16 + i) + (16 - (j + 1))


rows = 16
columns = 16
btns = [[None for i in range(rows)] for j in range(columns)]
colors = ["White", "Red", "Green", "Blue", "Magenta", "Cyan", "Yellow"]
colorButtons = [None for i in range(len(colors))]
clearButton = None
eraseButton = None
menuStrip = None
file = None
blankColor = "black"
userColor = blankColor
erase = False
boardClear = True
path = os.getcwd() + "/Pixel Box Images"

tk = Tk()
tk.title("Pixel Board")

createGrid()
createColorButtons()
createClearAndErase()
createMenuTab()
createFolders()

tk.config(menu=menuStrip)
tk.attributes('-fullscreen', True)

tk.protocol("WM_DELETE_WINDOW", on_closing)
tk.mainloop()
