import time
from base import getListInput

def quickSort(list):
    if (len(list) > 1):
        base = list[0] # Take first elemtn of the list as base value

        less = [i for i in list[1:] if i < base]
        greater = [i for i in list[1:] if i > base]

        return quickSort(less) + [base] + quickSort(greater)
    else:
        return list


def quickSortTime(count):
    list = getListInput(count)
    start = time.time()
    list = quickSort(list)
    end = time.time()

    return end - start