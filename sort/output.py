from bubblesort import bubbleSortTime
from selectionsort import selectionSortTime
from insertsort import insertSortTime
from quicksort import quickSortTime

from prettytable import PrettyTable

import csv

x = PrettyTable()
x.field_names = ['N', 'BubbleSort', 'SelectionSort', 'InsertSort', 'QuickSort']

print('Loading...')

x.add_row([10, bubbleSortTime(10), selectionSortTime(10), insertSortTime(10), quickSortTime(10)])
x.add_row([100, bubbleSortTime(100), selectionSortTime(100), insertSortTime(100), quickSortTime(100)])
x.add_row([1000, bubbleSortTime(1000), selectionSortTime(1000), insertSortTime(1000), quickSortTime(1000)])
x.add_row([10000, bubbleSortTime(10000), selectionSortTime(10000), insertSortTime(10000), quickSortTime(10000)])
x.add_row([100000, '', '', '', quickSortTime(100000)])
x.add_row([1000000, '', '', '', quickSortTime(1000000)])
x.add_row([10000000, '', '', '', quickSortTime(10000000)])

with open('output.txt', 'w') as w, open('output.csv', 'w', newline='') as c:
    w.write(str(x))
    x.
    c.write(x.get_csv_string())

    print('Sorting is over. You can see results in output.txt and output.csv files')