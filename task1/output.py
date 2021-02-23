from bubblesort import bubbleSortTime
from selectionsort import selectionSortTime
from insertsort import insertSortTime

from prettytable import PrettyTable

x = PrettyTable()
x.field_names = ['N', 'BubbleSort', 'SelectionSort', 'InsertSort']

print('Loading...')

x.add_row([10, bubbleSortTime(10), selectionSortTime(10), insertSortTime(10)])
x.add_row([100, bubbleSortTime(100), selectionSortTime(100), insertSortTime(100)])
x.add_row([1000, bubbleSortTime(1000), selectionSortTime(1000), insertSortTime(1000)])
x.add_row([10000, bubbleSortTime(10000), selectionSortTime(10000), insertSortTime(10000)])

print(x)