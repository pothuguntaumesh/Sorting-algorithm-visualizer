from tkinter import *
from tkinter import ttk
import random
from BubbleSort import *
from selectionSort import *
from insertionSort import *
from mergeSort import *
from quickSort import *

# Initialization
root = Tk()
root.title('Sorting algorithms visualizer')
root.maxsize(900, 600)
root.config(background='black')

# functions


def drawData(data, colorArray):
    canvas.delete('all')
    cWidth = 600
    cHeight = 380
    xWidth = cWidth/(len(data)+1)
    offset = 30
    spacing = 10
    normalizedData = [each/max(data) for each in data]
    for i, height in enumerate(normalizedData):
        # top left
        x0 = i*xWidth+offset+spacing
        y0 = cHeight-height*340
        # bottom right
        x1 = (i+1)*xWidth+offset
        y1 = cHeight

        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])
        canvas.create_text(x0+2, y0, anchor=SW, text=str(data[i]))
    root.update_idletasks()


def startAlgorithm():
    algo = algoMenu.get()
    print(algo)
    if algo == 'Bubble sort':
        bubbleSort(data, drawData, speedScale.get())
    elif algo == 'Selection sort':
        selectionSort(data, drawData, speedScale.get())
    elif algo == 'Insertion sort':
        insertionSort(data, drawData, speedScale.get())
    elif algo == 'Merge sort':
        mergeSort(data, drawData, speedScale.get())
    elif algo == 'Quick sort':
        quick_sort(data, 0, len(data)-1, drawData, speedScale.get())
        drawData(data, ['green' for x in range(len(data))])


def generate():

    global data

    minValue = int(minEntry.get())

    minValue = 1

    maxValue = int(maxEntry.get())

    maxValue = 100

    size = int(sizeEntry.get())
    data = []
    for _ in range(size):
        # generate a random number between min Value and maxValue
        value = random.randrange(minValue, maxValue+1)
        data.append(value)
    drawData(data, ['red' for _ in range(len(data))])


# variables
selectedAlgo = StringVar()
data = []


# UI frame
UiFrame = Frame(root, width=600, height=200, background='grey')
UiFrame.grid(row=0, column=0, padx=10, pady=5)

canvas = Canvas(root, width=600, height=380, background='white')
canvas.grid(row=1, column=0, padx=10, pady=5)


# user Interface
# row[0]
Label(UiFrame, text='Algorithm :', bg='grey').grid(
    row=0, column=0, padx=5, pady=5, sticky=W)

algoMenu = ttk.Combobox(UiFrame, textvariable=selectedAlgo, values=[
                        'Bubble sort', 'Selection sort', 'Insertion sort', 'Merge sort', 'Quick sort'])
algoMenu.grid(row=0, column=1, padx=5, pady=5)
algoMenu.current(0)

speedScale = Scale(UiFrame, from_=0.2, to=2.0, orient=HORIZONTAL,
                   length=200, digits=2, resolution=0.2, label='Select speed [s]')
speedScale.grid(row=0, column=2, padx=5, pady=5)
Button(UiFrame, text='   Start   ', command=startAlgorithm,
       bg='red').grid(row=0, column=3, pady=5, padx=5)
# Button(UiFrame, text='generate', command=generate,
#        bg='red').grid(row=0, column=2, padx=5, pady=5)

# row[1]
# Label(UiFrame, text='Size :', bg='grey').grid(
#     row=1, column=0, sticky=W, padx=5, pady=5)
sizeEntry = Scale(UiFrame, from_=3, to=30, orient=HORIZONTAL,
                  length=100, digits=2, resolution=1, label='Select size')
sizeEntry.grid(row=1, column=0, pady=5, padx=5, sticky=W)


# Label(UiFrame, text='Min Value :', bg='grey').grid(
#     row=1, column=2, sticky=W, padx=5, pady=5)
minEntry = Scale(UiFrame, from_=0, to=10, orient=HORIZONTAL,
                 length=100, label='Select min Value', digits=2, resolution=1)
minEntry.grid(row=1, column=1, padx=5, pady=5, sticky=W)

# Label(UiFrame, text='Max Value :', bg='grey').grid(
#     row=1, column=4, sticky=W, padx=5, pady=5)
maxEntry = Scale(UiFrame, from_=10, to=100, length=100,
                 label='Select max value', orient=HORIZONTAL, digits=2, resolution=1)
maxEntry.grid(row=1, column=2, sticky=W, pady=5, padx=5)

Button(UiFrame, bg='white', text='Generate', command=generate).grid(
    row=1, column=3, pady=5, padx=5)
root.mainloop()
