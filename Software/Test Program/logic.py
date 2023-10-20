def getIndex(i, j):
    if j <= 7:
        if i % 2 == 0:
            index = 8*i + j+1  # Don't need +1
        else:
            index = 8*i + (8-j)
    else:
        if i % 2 == 0:
            index = 8*(15+i) + j+1
        else:
            index = 8*(16+i) + (16-j)
    print(index)


getIndex(1, 0)
