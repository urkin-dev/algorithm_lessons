# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         arr = []
#         self.possibleSubs(arr, [], 0, nums)

#         return arr

#     def possibleSubs(self, arr, path, idx, nums):
#         arr.append(path)

#         if len(path) == len(nums): return
#         for i in range(idx, len(nums)):
#             self.possibleSubs(arr, path + [nums[i]], i + 1, nums)

# Quicker solution
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = [[]]
        
        for n in nums:
            output += [current + [n] for current in output]
        return output