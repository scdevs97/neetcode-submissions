class Solution:
    def hoursToClearPiles(self, piles: List[int], k: int):
        return sum([(p + k - 1) // k for p in piles])

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        minK = 1
        maxK = max(piles)
        
        while minK < maxK:
            m = (minK + maxK) // 2
            if self.hoursToClearPiles(piles, m) > h:
                minK = m + 1
            else:
                maxK = m
        
        return minK

        