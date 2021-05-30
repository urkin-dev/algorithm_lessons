import random

class Solution(object):
    def sortArray(self, nums):
        arr = nums
        
        for i in range(len(arr)):
            arr[i] = int(arr[i])
        
        arr = self.quickSort(arr)
        
        return arr
    
    def quickSort(self, list):
        if (len(list) > 1):
            base = random.choice(list)
            
            less = [i for i in list if i < base]
            greater = [i for i in list if i > base]
            equal = [i for i in list if i == base]
            
            return self.quickSort(less) + equal + self.quickSort(greater)
        else: 
            return list