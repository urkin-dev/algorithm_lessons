import sys
import time
from base import getListInput

if (len(sys.argv) > 1):
    count = sys.argv[1]
else:
    print('You should enter the number of values in input file')
    sys.exit()

list = set(getListInput(count)) #Remove repeat values
list = sorted(list)

ELEMENT = 54 #Element you need to find

def binarySearch(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        middle = (low + high)
        guessed = list[middle]

        if (guessed == item):
            return middle

        if (guessed > item):
            high = middle - 1
        else:
            low = middle + 1

    return 'not found'


start = time.time()
result = binarySearch(list, element)
end = time.time()

print('Index of element {} in unique array is: {}'.format(ELEMENT, result))
print(end - start)
