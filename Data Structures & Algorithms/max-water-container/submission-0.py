class Solution:
    def maxArea(self, heights: List[int]) -> int:
        largestArea = 0
        l = 0
        r = len(heights) - 1

        while l < r:
            currArea = (r - l) * min(heights[l], heights[r])
            if currArea > largestArea:
                largestArea = currArea
            
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return largestArea