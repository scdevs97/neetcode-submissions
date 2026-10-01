class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixes = []
        suffixes = []

        prefix = 1
        for i in range(len(nums)):
            prefixes.append(prefix)
            prefix *= nums[i]

        suffix = 1
        for j in range(len(nums)-1, -1, -1):
            suffixes.append(suffix)
            suffix *= nums[j]
        
        res = [prefixes[k] * suffixes[len(nums) - 1 - k] for k in range(len(nums))]

        return res
