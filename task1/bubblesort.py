import time
from base import getListInput

def bubbleSort(list):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(list) - 1):
            if list[i] > list[i + 1]:
                list[i], list[i + 1] = list[i + 1], list[i]
                swapped = True


def bubbleSortTime(count):
    list = getListInput(count)
    start = time.time()
    bubbleSort(list)
    end = time.time()

    return end - start
