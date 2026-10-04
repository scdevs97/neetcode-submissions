class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        numToIndexMap = defaultdict(int)
        for i in range(len(nums)):
            numToIndexMap[nums[i]] = i
        
        ret_set = set()
        for i in range(len(nums) -2):
            for j in range(i+1, len(nums) - 1):
                missingVal = -nums[i] - nums[j]
                if missingVal in numToIndexMap and numToIndexMap[missingVal] > j:
                    ret_set.add((nums[i], nums[j], missingVal))
        
        return [[x,y,z] for x,y,z in ret_set ]
                    
        