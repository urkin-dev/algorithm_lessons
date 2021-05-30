import sys
import random

input = open('./input.txt', 'r')
list = input.readlines()[0]
list = list.split(' ')
input.close()

# Init
q, v, p, n, k = int(list[0]), int(list[1]), int(
    list[2]), int(list[3]), int(list[4])
a = [p]


def quickSort(list):
    if (len(list) > 1):
        base = random.choice(list)

        less = [i for i in list if i < base]
        greater = [i for i in list if i > base]
        equal = [i for i in list if i == base]

        return quickSort(less) + equal + quickSort(greater)
    else:
        return list


if (q == 0 or v == 0):
    sys.exit()

for i in range(1, n):
    a.append((a[i-1] * q) % v)

sortedA = quickSort(a)
print(sortedA[k-1])
