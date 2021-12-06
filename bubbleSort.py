import time

def bubble_sort(data, drawData, canvas, timeTick):
    print(data)
    n = len(data)
    for i in range(n-1):
        for j in range(n-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                drawData(data, canvas, ['green' if x == j or x == j+1 else 'red' for x in range(len(data))] )
                time.sleep(timeTick)
    drawData(data, canvas, ['green' for x in range(len(data))])