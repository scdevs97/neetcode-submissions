class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
            
        res1 = 1 
        res2 = 2

        for i in range(n-2):
            if res1 < res2:
                res1 += res2
            else:
                res2 += res1
        
        return max(res1, res2)