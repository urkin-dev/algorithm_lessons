import time
from base import getListInput

def insertSort(list):
    for i in range(1, len(list)):
        item_to_insert = list[i]
        j = i - 1
        while j >= 0 and list[j] > item_to_insert:
            list[j + 1] = list[j]
            j -= 1
        list[j + 1] = item_to_insert

    return list


def insertSortTime(count):
    list = getListInput(count)
    start = time.time()
    insertSort(list)
    end = time.time()

    return end - start
