import time


def merge_sort(data, drawData, canvas, speed):
    merge_sort_alg(data, 0, len(data) - 1, drawData, canvas, speed)


def merge_sort_alg(data, left, right, drawData, canvas, speed):
    if left < right:
        middle = (left + right) // 2
        merge_sort_alg(data, left, middle, drawData, canvas, speed)
        merge_sort_alg(data, middle + 1, right, drawData, canvas, speed)
        merge(data, left, middle, right, drawData, canvas, speed)


def merge(data, left, middle, right, drawData, canvas, speed):
    drawData(data, canvas, getColorArray(len(data), left, middle, right))
    time.sleep(speed)

    leftPart = data[left:middle + 1]
    rightPart = data[middle + 1: right + 1]

    leftIdx = rightIdx = 0

    for dataIdx in range(left, right + 1):
        if leftIdx < len(leftPart) and rightIdx < len(rightPart):
            if leftPart[leftIdx] <= rightPart[rightIdx]:
                data[dataIdx] = leftPart[leftIdx]
                leftIdx += 1
            else:
                data[dataIdx] = rightPart[rightIdx]
                rightIdx += 1

        elif leftIdx < len(leftPart):
            data[dataIdx] = leftPart[leftIdx]
            leftIdx += 1
        else:
            data[dataIdx] = rightPart[rightIdx]
            rightIdx += 1

    drawData(data, canvas, ["green" if x >= left and x <= right else "white" for x in range(len(data))])
    time.sleep(speed)


def getColorArray(leght, left, middle, right):
    colorArray = []

    for i in range(leght):
        if i >= left and i <= right:
            if i >= left and i <= middle:
                colorArray.append("yellow")
            else:
                colorArray.append("pink")
        else:
            colorArray.append("white")

    return colorArray