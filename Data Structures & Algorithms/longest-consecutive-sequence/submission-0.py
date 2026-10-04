class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        nums.sort()
        currLength = 1
        longestLength = 1
        prevNum = nums[0]
        
        for i in range(1, len(nums)):
            n = nums[i]
            if n == prevNum + 1:
                currLength += 1
            elif n == prevNum:
                continue
            else:
                if currLength > longestLength:
                    longestLength = currLength
                currLength = 1
            prevNum = n
        
        if currLength > longestLength:
            longestLength = currLength

        return longestLength
