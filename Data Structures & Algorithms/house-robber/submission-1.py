class Solution:
    def rob(self, nums: List[int]) -> int:
        #maxMoney(n) = max money that can be robbed from houses 0 to n
        #maxMoney(n) = max(maxMoney(n-2) + money[n], maxMoney(n-1))
        #maxMoney(0) = money[0]
        #maxMoney(1) = max(money[0], money[1])
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]

        maxMoney = [0] * len(nums)
        maxMoney[0] = nums[0]
        maxMoney[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            maxMoney[i] = max(maxMoney[i-2] + nums[i], maxMoney[i-1])
        return maxMoney[len(nums) - 1]