class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        totalProduct = 1
        zero_indexes = []
        for i in range(len(nums)):
            n = nums[i]
            if n == 0:
                zero_indexes.append(i)
            else:
                totalProduct *= n
        if len(zero_indexes) > 1:
            return [0] * len(nums)
        if len(zero_indexes) == 1:
            return [0 if i not in zero_indexes else totalProduct for i in range(len(nums))]
        return [totalProduct // n for n in nums]