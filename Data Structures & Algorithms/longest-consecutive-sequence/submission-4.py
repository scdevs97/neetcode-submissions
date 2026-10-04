class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        longestLength = 0

        for n in nums:
            if n not in numsSet:
                continue

            numsSet.remove(n)
            currLength = 1

            currNum = n - 1
            while currNum in numsSet:
                numsSet.remove(currNum)
                currLength += 1
                currNum -= 1

            currNum = n + 1
            while currNum in numsSet:
                numsSet.remove(currNum)
                currLength += 1
                currNum += 1

            if currLength > longestLength:
                longestLength = currLength
        
        return longestLength
            
