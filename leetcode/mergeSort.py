class Solution:
    def sortArray(self, nums):
        arr = nums
        for i in range(len(arr)):
            arr[i] = int(arr[i])

        def mergeSort(arr):
            if len(arr) > 1:

                mid = len(arr)//2
                left = arr[:mid]
                right = arr[mid:]

                mergeSort(left)
                mergeSort(right)

                i = j = k = 0  # i - index of the left list, j - index of the right list, k - index of the list

                while i < len(left) and j < len(right):
                    if left[i] < right[j]:
                        # List is the left part from "up call of function"
                        arr[k] = left[i]
                        i += 1
                    else:
                        arr[k] = right[j]
                        j += 1
                    k += 1

                # For all remaining values
                while i < len(left):
                    arr[k] = left[i]
                    i += 1
                    k += 1

                while j < len(right):
                    arr[k] = right[j]
                    j += 1
                    k += 1

        mergeSort(arr)

        return arr
