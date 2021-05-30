input = open('input.txt', 'r')

arr = input.read().split()
arr = [int(i) for i in arr]  # To numbers
input.close()

n = arr[0]
del arr[0]
count = 0


def mergeSort(arr):
    if len(arr) > 1:
        middle = len(arr) // 2
        left = arr[:middle]
        right = arr[middle:]

        mergeSort(left)
        mergeSort(right)

        i = j = k = 0  # i - index of the left arr, j - index of the right arr, k - index of the arr
        global count

        while (i < len(left) and j < len(right)):
            if (left[i] <= right[j]):
                # arr is the left part from "up call of function"
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                count += (len(left) - i)
                j += 1

            k += 1

        # For all remaining values
        while (i < len(left)):
            arr[k] = left[i]
            i += 1
            k += 1

        while (j < len(right)):
            arr[k] = right[j]
            j += 1
            k += 1


mergeSort(arr)

filename = "output.txt"
file = open(filename, "w")
file.write(str(count))
file.close()
