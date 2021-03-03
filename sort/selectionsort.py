import time
from base import getListInput

def selectionSort(list):
    # Значение i соответствует кол-ву отсортированных значений
    for i in range(len(list)):
        min_index = i

        for j in range(i + 1, len(list)):
            if list[j] < list[min_index]:
                min_index = j

        list[i], list[min_index] = list[min_index], list[i]


def selectionSortTime(count):
    list = getListInput(count)
    start = time.time()
    selectionSort(list)
    end = time.time()

    return end - start
