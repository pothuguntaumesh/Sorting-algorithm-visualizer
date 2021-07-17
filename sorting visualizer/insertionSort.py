import time


def insertionSort(arr, drawData, timer):
    for i in range(len(arr)):
        cur = arr[i]
        hole = i

        while hole > 0 and cur < arr[hole-1]:
            arr[hole] = arr[hole-1]
            arr[hole-1] = cur
            color = []
            for x in range(len(arr)):
                if x == i:
                    color.append('blue')
                elif x == hole or x == hole-1:
                    color.append('green')
                else:
                    color.append('red')

            drawData(arr, color)
            time.sleep(timer)
            hole -= 1
    drawData(arr, ['green' for x in range(len(arr))])
# arr = [3, 2, 5, 7, 1, 2, 8, 9, 0]
# insertionSort(arr, None, None)
# print(arr)
