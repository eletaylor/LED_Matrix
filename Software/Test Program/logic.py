def getIndex(i, j):
    global index
    global newIndex
    global quadrant
    if j <= 7:
        if i % 2 == 0:
            index = 8*i + j  # Don't need +1
        else:
            index = 8*i + (8-(j+1))
    else:
        if i % 2 == 0:
            index = 8*(15+i) + j
        else:
            index = 8*(16+i) + (16-(j+1))
    print(index)
    getQuadrant(index)
    NewIndex(i, j)
    lightBulb(newIndex, quadrant)


def getQuadrant(index):
    global quadrant
    if index in range(0, 64):
        quadrant = 3
    elif index in range(64, 128):
        quadrant = 1
    elif index in range(128, 192):
        quadrant = 4
    elif index in range(192, 256):
        quadrant = 2
    print(quadrant)


def NewIndex(i, j):
    global newIndex
    if j <= 7:
        if i <= 7:
            if i % 2 == 0:
                newIndex = 8*i + (7-j)  # Don't need +1
            else:
                newIndex = 8*i + (8-(j+1))
        else:
            if i % 2 == 0:
                newIndex = 8*(i-8) + (7-j)  # Don't need +1
            else:
                newIndex = 8*(i-8) + (8-(j+1))
    else:
        if i <= 7:
            if i % 2 == 0:
                newIndex = 8*i + (7-(j-8))  # Don't need +1
            else:
                newIndex = 8*i + (8-((j-8)+1))
        else:
            if i % 2 == 0:
                newIndex = 8*(i-8) + (7-(j-8))  # Don't need +1
            else:
                newIndex = 8*(i-8) + (8-((j-8)+1))
    print(newIndex)
# The zeroes are 7, 71, 135, 199
# Create function to decide which color to use


def lightBulb(newIndex, quadrant):
    global userColor
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

userColor = None
index = None
newIndex = None
quadrant = None
getIndex(8, 0)