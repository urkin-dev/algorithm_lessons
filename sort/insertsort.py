import time
from base import getListInput
# [1, 3, 4, 8, 2]
# Сравниваем предыдущий элемент со следующим и если этот элемент больше, то ставим его на место этого элемента и проверям 
# элементы слева и так далее, пока элементы слева больше. В конце переставляем наш элемент на место последнего большего элемента
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
