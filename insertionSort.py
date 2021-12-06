import time


def insertion_sort(data, drawData, canvas, speed):
    for i in range(len(data)-1):
        key_item = data[i]
        j = i-1
        while j>=0 and data[j] > key_item:
            data[j+1] = data[j]
            j-=1
        data[j+1] = key_item
        colorArray = getColorArray(j, i, len(data))
        drawData(data, canvas, colorArray)
        time.sleep(speed)
    drawData(data, canvas, ['green' for x in range(len(data))])


def getColorArray(j, i, dataLen):
    colorArray = []
    for n in range(dataLen):
        if n > i:
            colorArray.append('red')
        elif n < i:
            colorArray.append('green')

        if n == j or n == i:
            colorArray.append('blue')

    return colorArray