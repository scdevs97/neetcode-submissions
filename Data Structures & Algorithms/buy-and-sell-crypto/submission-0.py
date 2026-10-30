class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0

        currMaxProfit = 0
        currBuyPrice = prices[0]

        for i in range(1, len(prices)):
            p = prices[i]
            if p < currBuyPrice:
                currBuyPrice = p
            elif p - currBuyPrice > currMaxProfit:
                currMaxProfit = p - currBuyPrice 
            
        return currMaxProfit
