from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import board
import neopixel
import os
import time

'''Use GPIO pins 10, 12, 18, 21 for each quadrant
   of lights respectively'''
pixel_pin1 = board.D10
pixel_pin2 = board.D12
pixel_pin3 = board.D18
pixel_pin4 = board.D21

# Set the number of pixels for each quadrant
num_pixels = 64

'''Set the RGB values in order GRB. It does
   the opposite for some weird reason'''
ORDER = neopixel.GRB

'''Initalize 4 pixel quadrants to the pin, number of pixels,
   brightness, and pixel order'''
pixels1 = neopixel.NeoPixel(
    pixel_pin1, num_pixels, brightness=0.1, pixel_order=ORDER)
pixels2 = neopixel.NeoPixel(
    pixel_pin2, num_pixels, brightness=0.1, pixel_order=ORDER)
pixels3 = neopixel.NeoPixel(
    pixel_pin3, num_pixels, brightness=0.1, pixel_order=ORDER)
pixels4 = neopixel.NeoPixel(
    pixel_pin4, num_pixels, brightness=0.1, pixel_order=ORDER)


'''Create the button grid for the application, configure the grid,
   and when a user clicks on a button, call the color function'''
def createGrid():
    global blankColor
    for i in range(rows):
        for j in range(columns):
            btns[i][j] = Button(tk, bg=blankColor)
            btns[i][j]['command'] = lambda btn=btns[i][j]: color(btn)
            btns[i][j].grid(row=i + 1, column=j)
            Grid.rowconfigure(tk, index=i + 1, weight=1)


# Create and format the color buttons on the side of the screen
def createColorButtons():
    for i in range(len(colors)):
        if colors[i] == "White" or colors[i] == "Yellow":
            colorButtons[i] = Button(tk, text=colors[i], fg='black', bg=colors[i].lower())
        else:
            colorButtons[i] = Button(tk, text=colors[i], fg='white', bg=colors[i].lower())

        colorButtons[i]['command'] = lambda btn=colorButtons[i]: changeColor(btn)
        colorButtons[i].grid(row=i + 7, column=35)


# Create the clear and erase buttons just under the color buttons
def createClearAndErase():
    global clearButton
    clearButton = Button(tk, text="Clear", fg="white", bg="gray")
    clearButton.grid(row=15, column=35)
    clearButton['command'] = lambda btn=clearButton: clear(btn)

    global eraseButton
    eraseButton = Button(tk, text="Erase", fg="white", bg="gray")
    eraseButton.grid(row=16, column=35)
    eraseButton['command'] = lambda btn=eraseButton: eraser(btn)
    
    global funButton
    funButton = Button(tk, text="Party Mode", fg="white", bg="blue")
    funButton.grid(row=8, column=40)
    funButton['command'] = lambda btn=funButton: fun(btn)


'''Create the menu tab at the top of the screen with the
   cascading buttons'''
def createMenuTab():
    global menuStrip
    global file

    menuStrip = Menu(tk)
    file = Menu(menuStrip, tearoff=0)

    menuStrip.add_cascade(label="File", menu=file)
    file.add_command(label="Open Design", command=lambda: open_file())
    file.add_command(label="Save Design", command=lambda: save_file())
    menuStrip.add_command(label="Exit", command=lambda: on_closing())


# Create a directory for the text files if it does not exist already
def createFolder():
    if not (os.path.exists(path)):
        os.makedirs(path)


'''Clear the board if the user answers "yes", or say the grid is 
already clear'''
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


# Reset the userColor, LEDs, and booleans
def reset():
    global userColor
    global erase
    global boardClear
    userColor = blankColor
    erase = False
    boardClear = True
    
    pixels1.fill((0, 0, 0))
    pixels2.fill((0, 0, 0))
    pixels3.fill((0, 0, 0))
    pixels4.fill((0, 0, 0))


# Set the erase boolean to true if the grid is not empty
def eraser(btn):
    global erase
    global boardClear
    if boardClear is False:
        messagebox.showinfo("Erase Activated", "Erase activated.")
        erase = True
    else:
        messagebox.showinfo("Grid Empty", "Grid empty. Nothing to erase.")


'''Get the info from the button that was clicked.
   Check to see if the user has selected a color,
   has clicked erase, or is changing the color of a
   pixel'''
def color(btn):
    global boardClear
    global userColor
    
    row = btn.grid_info()['row'] - 1
    column = btn.grid_info()['column']
    
    if userColor == blankColor and erase is False:
        messagebox.showinfo("No Color Selected", "No color selected. Please choose a color on the right-hand side "
                            + "of the screen.")
    elif erase:
        btn['bg'] = blankColor
        boardClear = False
        getIndex(row, column, blankColor)
    else:
        btn['bg'] = userColor
        boardClear = False
        getIndex(row, column, userColor)


'''When a user clicks a color button, change userColor variable
   and check if the user is trying to erase or not'''
def changeColor(btn):
    global userColor
    userColor = btn['bg']

    global erase
    if erase:
        erase = False
        messagebox.showinfo("Color Changed", "Erase deactivated. The active color is " + userColor)
    else:
        messagebox.showinfo("Color Changed", "The active color is " + userColor)


'''This method handles the "Party Mode" feature.
   It runs through a pre-set cycle 3 times.'''
def fun(btn):
    for i in range(3):
        fillColor((255, 0, 0))
        fillColor((0, 255, 0))
        fillColor((0, 0, 255))
        fillColor((255, 0, 255))
        fillColor((0, 100, 100))
        fillColor((255, 255, 0))
        
        pixels1.fill((255, 0, 0))
        pixels2.fill((0, 255, 0))
        pixels3.fill((0, 255, 0))
        pixels4.fill((0, 0, 255))
        time.sleep(1)
        
        for i in range(64):
            pixels1[i] = (255, 255, 0)
            pixels4[i] = (255, 255, 0)
            pixels2[i] = (255, 255, 255)
            pixels3[i] = (255, 255, 255)
        
        pixels1.fill((255, 0, 0))
        pixels2.fill((0, 0, 255))
        pixels3.fill((0, 0, 255))
        pixels4.fill((255, 255, 0))
        time.sleep(1)
        
    fillColor((0, 0, 0))
        


# This method fills all the quadrants with a particular color
def fillColor(color):
    pixels1.fill(color)
    pixels2.fill(color)
    pixels3.fill(color)
    pixels4.fill(color)
    time.sleep(1)
        
        
'''If the user closes the program, reset the board and exit the 
   application'''
def on_closing():
    if messagebox.askokcancel("Quit", "Are you sure you want to quit?"):
        reset()
        tk.destroy()


'''Open a design by reading in the selected text file from the file
   dialog and changing the color of the LEDs'''
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
    colorArray = [x.strip() for x in colorArray] # Get rid of "\n"
    for i in range(rows):
        for j in range(columns):
            btns[i][j]['bg'] = colorArray[counter]
            getIndex(i, j, colorArray[counter])
            counter += 1


'''Save a design by writing the button background colors to a .txt 
   file. Reset the booleans and userColor.'''
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


# Get the index of the LED (0-255). Don't ask about the math. It sucked.
def getIndex(i, j, userColor):
    global index
    global newIndex
    global quadrant
    if j <= 7:
        if i % 2 == 0:
            index = 8*i + j  # Don't need +1
        else:
            index = 8*i + (7-j)
    else:
        if i % 2 == 0:
            index = 8*(15+i) + j
        else:
            index = 8*(16+i) + (15-j)
    getQuadrant(index, i, j, userColor)


# Get the quadrant of the LED
def getQuadrant(index, i, j, userColor):
    global quadrant
    if index in range(0, 64):
        quadrant = 4
    elif index in range(64, 128):
        quadrant = 3
    elif index in range(128, 192):
        quadrant = 2
    elif index in range(192, 256):
        quadrant = 1
    NewIndex(i, j, userColor)

'''Change the index found earlier to a value between 0 and 63.
   The hours I toiled to get the math right...'''
def NewIndex(i, j, userColor):
    global newIndex
    global quadrant
    
    if j <= 7:
        # Quadrant 1
        if i <= 7:
            
            # Row is even (read numbers left to right on board)
            if i % 2 == 0:
                newIndex = 8*i + j
                
            # Row is odd (read numbers right to left on board)
            else:
                newIndex = 8*i + (7-j)
                
        # Quadrant 2
        else:
            if i % 2 == 0:
                newIndex = 8*(i-8) + j
            else:
                newIndex = 8*(i-8) + (7-j)
    else:
        
        # Quadrant 3
        if i <= 7:
            if i % 2 == 0:
                newIndex = 8*i + (j-8)  # Don't need +1
            else:
                newIndex = 8*i + (15-j)
                
        # Quadrant 4
        else:
            if i % 2 == 0:
                newIndex = 8*(i-8) + (j-8)  # Don't need +1
            else:
                newIndex = 8*(i-8) + (15-j)
    lightBulb(newIndex, quadrant, userColor)


# Light the correct LED in the correct quadrant with the correct color
def lightBulb(newIndex, quadrant, userColor):
    if quadrant == 1:
        if userColor == "black":
            pixels1[newIndex] = (0, 0, 0)
        elif userColor == "white":
            pixels1[newIndex] = (255, 255, 255)
        elif userColor == "red":
            pixels1[newIndex] = (255, 0, 0)
        elif userColor == "green":
            pixels1[newIndex] = (0, 255, 0)
        elif userColor == "blue":
            pixels1[newIndex] = (0, 0, 255)
        elif userColor == "magenta":
            pixels1[newIndex] = (255, 0, 255)
        elif userColor == "cyan":
            pixels1[newIndex] = (0, 100, 100)
        elif userColor == "yellow":
            pixels1[newIndex] = (255, 255, 0)
    elif quadrant == 2:
        if userColor == "black":
            pixels2[newIndex] = (0, 0, 0)
        elif userColor == "white":
            pixels2[newIndex] = (255, 255, 255)
        elif userColor == "red":
            pixels2[newIndex] = (255, 0, 0)
        elif userColor == "green":
            pixels2[newIndex] = (0, 255, 0)
        elif userColor == "blue":
            pixels2[newIndex] = (0, 0, 255)
        elif userColor == "magenta":
            pixels2[newIndex] = (255, 0, 255)
        elif userColor == "cyan":
            pixels2[newIndex] = (0, 100, 100)
        elif userColor == "yellow":
            pixels2[newIndex] = (255, 255, 0)
    elif quadrant == 3:
        if userColor == "black":
            pixels3[newIndex] = (0, 0, 0)
        elif userColor == "white":
            pixels3[newIndex] = (255, 255, 255)
        elif userColor == "red":
            pixels3[newIndex] = (255, 0, 0)
        elif userColor == "green":
            pixels3[newIndex] = (0, 255, 0)
        elif userColor == "blue":
            pixels3[newIndex] = (0, 0, 255)
        elif userColor == "magenta":
            pixels3[newIndex] = (255, 0, 255)
        elif userColor == "cyan":
            pixels3[newIndex] = (0, 100, 100)
        elif userColor == "yellow":
            pixels3[newIndex] = (255, 255, 0)
    else:
        if userColor == "black":
            pixels4[newIndex] = (0, 0, 0)
        elif userColor == "white":
            pixels4[newIndex] = (255, 255, 255)
        elif userColor == "red":
            pixels4[newIndex] = (255, 0, 0)
        elif userColor == "green":
            pixels4[newIndex] = (0, 255, 0)
        elif userColor == "blue":
            pixels4[newIndex] = (0, 0, 255)
        elif userColor == "magenta":
            pixels4[newIndex] = (255, 0, 255)
        elif userColor == "cyan":
            pixels4[newIndex] = (0, 100, 100)
        elif userColor == "yellow":
            pixels4[newIndex] = (255, 255, 0)
                
                
# Set the rows and columns of the button grid
rows = 16
columns = 16

# Create an array of available colors
colors = ["White", "Red", "Green", "Blue", "Magenta", "Cyan", "Yellow"]

# Initalize the button grid and color buttons
btns = [[None for i in range(rows)] for j in range(columns)]
colorButtons = [None for i in range(len(colors))]

'''Initalize the clear and erase buttons, the menu bar, file dialog,
   index variables, quadrant variable, blankColor, userColor, and
   drawing booleans'''
funButton = None
clearButton = None
eraseButton = None
menuStrip = None
file = None
index = None
newIndex = None
quadrant = None
blankColor = "black"
userColor = blankColor
erase = False
boardClear = True
funBool = False

# Store the path of the directory for the .txt files
path = os.getcwd() + "/Pixel Box Images"

# Start the tkinter application and give it a title
tk = Tk()
tk.title("Pixel Board")

'''Create the button grid, color buttons, clear and erase buttons,
   menu tab, and (if necessary) the folder for the .txt files'''
createGrid()
createColorButtons()
createClearAndErase()
createMenuTab()
createFolder()

'''Add the menu strip to the application window and make the
   application full screen'''
tk.config(menu=menuStrip)
tk.attributes('-fullscreen', True)

# When the user closes the application, call on_closing
tk.protocol("WM_DELETE_WINDOW", on_closing)

# This starts the application and keeps it running
tk.mainloop()
