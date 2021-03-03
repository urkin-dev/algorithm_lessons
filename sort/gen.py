import sys
import random

if (len(sys.argv) > 1):
    count = sys.argv[1]
else:
    print('You should enter the number of values')
    sys.exit()

# Range of generate values
leftRange = 1
rightRange = 10000

inputFile = open('inputs/input_' + count + '.txt', 'w')

inputFile.write(count + '\n')

for i in range(int(count)):
    value = str(random.randint(leftRange, rightRange)) + ' '
    inputFile.write(value)

inputFile.close()
