class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        arr = [[]]

        for i in range(len(nums)):
            for j in range(len(arr)):
                t = arr[j].copy()
                t.append(nums[i])
                arr.append(t)

        return arr