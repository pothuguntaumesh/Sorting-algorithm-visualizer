import time


def selectionSort(arr, drawData, timer):
    print('hello')
    for i in range(len(arr)-1):
        _min = i
        for j in range(i, len(arr)):
            if arr[j] < arr[_min]:
                _min = j
        drawData(arr, ['green' if x == i or x ==
                       _min else 'red' for x in range(len(arr))])
        time.sleep(timer)

        arr[_min], arr[i] = arr[i], arr[_min]
    drawData(arr, ['green' for _ in range(len(arr))])
