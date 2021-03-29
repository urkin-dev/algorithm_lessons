import time
from base import getListInput

def mergeSort(list):
    if len(list) > 1:
        middle = len(list) // 2 # Middle index fo the list
        left = list[:middle]
        right = list[middle:]

        mergeSort(left)
        mergeSort(right)

        i = j = k = 0 # i - index of the left list, j - index of the right list, k - index of the list

        while (i < len(left) and j < len(right)):
            if (left[i] < right[i]):
                list[k] = left[i]
                i += 1
            else:
                list[k] = right[i]
                j += 1
            
            k += 1

        while (i < len(left)):
            list[k] = left[i]
            i += 1
            k += 1

        while (j < len(right)):
            list[k] = right[j]
            j += 1
            k += 1

def mergeSortTime(count):
    list = getListInput(count)
    start = time.time()
    mergeSort(list)
    end = time.time()

    return end - start