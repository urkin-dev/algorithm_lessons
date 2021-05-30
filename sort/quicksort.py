import time
from base import getListInput
import random


def quickSort(list):
    if (len(list) > 1):
        base = list[0]  # Take first elemtn of the list as base value

        base = random.choice(list)

        less = [i for i in list if i < base]
        greater = [i for i in list if i > base]
        equal = [i for i in list if i == base]

        return self.quickSort(less) + equal + self.quickSort(greater)
    else:
        return list


def quickSortTime(count):
    list = getListInput(count)
    start = time.time()
    list = quickSort(list)
    end = time.time()

    return end - start
