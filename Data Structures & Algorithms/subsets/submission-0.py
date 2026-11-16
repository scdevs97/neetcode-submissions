class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        retList = []
        for i in range(2**len(nums)):
            subset = []
            for j, num in enumerate(nums):
                if (i >> j) & 1:
                    subset.append(num)
            retList.append(subset)  
        return retList



