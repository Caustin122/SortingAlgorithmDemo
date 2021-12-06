import time


def partition(data, head, tail, drawData, canvas, speed):
    border = head
    pivot = data[tail]

    drawData(data, canvas, getColorArray(len(data), head, tail, border, border))
    time.sleep(speed)

    for j in range(head, tail):
        if data[j] < pivot:
            drawData(data, canvas, getColorArray(len(data), head, tail, border, j, True))
            time.sleep(speed)

            data[border], data[j] = data[j], data[border]
            border += 1

        drawData(data, canvas,  getColorArray(len(data), head, tail, border, j))
        time.sleep(speed)

    # swap pivot with border value
    drawData(data, canvas,  getColorArray(len(data), head, tail, border, tail, True))
    time.sleep(speed)

    data[border], data[tail] = data[tail], data[border]

    return border


def quick_sort(data, head, tail, drawData, canvas, speed):
    if head < tail:
        partitionIdx = partition(data, head, tail, drawData, canvas, speed)

        # LEFT PARTITION
        quick_sort(data, head, partitionIdx - 1, drawData, canvas, speed)

        # RIGHT PARTITION
        quick_sort(data, partitionIdx + 1, tail, drawData, canvas, speed)


def getColorArray(dataLen, head, tail, border, currIdx, isSwaping=False):
    colorArray = []
    for i in range(dataLen):
        # base coloring
        if i >= head and i <= tail:
            colorArray.append('gray')
        else:
            colorArray.append('white')

        if i == tail:
            colorArray[i] = 'blue'
        elif i == border:
            colorArray[i] = 'red'
        elif i == currIdx:
            colorArray[i] = 'yellow'

        if isSwaping:
            if i == border or i == currIdx:
                colorArray[i] = 'green'

    return colorArray