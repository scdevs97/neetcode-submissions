class Solution:
    def rob(self, nums: List[int]) -> int:
        #maxMoney(n) = max money that can be robbed from houses 0 to n
        #maxMoney(n) = max(maxMoney(n-2) + money[n], maxMoney(n-1))
        #maxMoney(0) = money[0]
        #maxMoney(1) = max(money[0], money[1])
        one = nums[0]
        two = 0

        for i in range(1, len(nums)):
            two = max(two + nums[i], one)
            tmp = two
            two = one
            one = tmp

        return one