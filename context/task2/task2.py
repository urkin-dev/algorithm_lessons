input = open('./input.txt', 'r')

list = input.readlines()[1].split(' ')
list = [int(i) for i in list] #To numbers

result = 0

input.close()

for i in range(len(list)):
    for j in range(i, len(list)):
        if (list[i] > list[j]):
            result += 1

print(result)
