import sys

input = open('./input.txt', 'r')
list = input.readlines()[0]
list = list.split(' ')
input.close()

#Init
q, v, p, n, k = int(list[0]), int(list[1]), int(list[2]), int(list[3]), int(list[4])
a = [p]

if (q == 0 or v == 0):
    sys.exit()

for i in range(1, n):
    a.append((a[i-1] * q) % v)

A = sorted(a)
print(A[k-1])
