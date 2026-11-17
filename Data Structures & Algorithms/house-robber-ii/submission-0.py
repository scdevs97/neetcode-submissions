class Solution:
    def rob(self, nums: List[int]) -> int:
        # if rob first house, cannot rob last house.
        # assume rob first house, check total money that can be earned from 3rd to 2nd last house.
        # compare against money that can be earned from not robbing first house, which will be the 2nd to last house
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        if len(nums) == 3:
            return max(nums[0], nums[1], nums[2])

        #assume rob first house
        firstHouseMoney = nums[0]

        one = nums[2]
        two = 0

        for i in range(3, len(nums) - 1):
            two = max(one, two + nums[i])
            tmp = two
            two = one
            one = tmp
        
        maxMoneyIncFirstHouse = one + firstHouseMoney

        #assume don't rob first house
        one = nums[1]
        two = 0

        for i in range(2, len(nums)):
            two = max(one, two + nums[i])
            tmp = two
            two = one
            one = tmp
        
        maxMoneyExcFirstHouse = one

        #compare
        return max(maxMoneyIncFirstHouse, maxMoneyExcFirstHouse)