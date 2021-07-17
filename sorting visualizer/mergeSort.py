import time


def mergeSort(arr, drawData, timer):
    _mergeSort(arr, 0, len(arr)-1, drawData, timer)


def _mergeSort(arr, left, right, drawData, timer):
    if left < right:
        middle = (left+right)//2
        # sort the left part
        _mergeSort(arr, left, middle, drawData, timer)
        # sort the right part
        _mergeSort(arr, middle+1, right, drawData, timer)
        # merge left and right parts
        merge(arr, left, middle, right, drawData, timer)


def merge(arr, left, middle, right, drawData, timer):
    drawData(arr, getColor(len(arr), left, middle, right))
    time.sleep(timer)
    leftArr = arr[left:middle+1]
    rightArr = arr[middle+1:right+1]
    leftIndex, rightIndex = 0, 0
    for idx in range(left, right+1):
        if leftIndex < len(leftArr) and rightIndex < len(rightArr):
            if leftArr[leftIndex] <= rightArr[rightIndex]:
                arr[idx] = leftArr[leftIndex]
                leftIndex += 1
            else:
                arr[idx] = rightArr[rightIndex]
                rightIndex += 1
        elif leftIndex < len(leftArr):
            arr[idx] = leftArr[leftIndex]
            leftIndex += 1
        else:
            arr[idx] = rightArr[rightIndex]
            rightIndex += 1
    drawData(arr, ['green' if x >= left and x <=
                   right else 'white' for x in range(len(arr))])


def getColor(length, left, middle, right):
    colorArr = []
    for i in range(length):
        if i >= left and i <= right:
            if i <= middle:
                colorArr.append('yellow')
            else:
                colorArr.append('pink')
        else:
            colorArr.append('white')
    return colorArr
