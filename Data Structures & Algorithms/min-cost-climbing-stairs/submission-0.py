class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        a = b = 0
        for i in range(2, len(cost)+1):
            temp = a
            a = min(a + cost[i-1], b + cost[i-2])
            b = temp
        return a

    # minCost[0] = 0
    # minCost[1] = 0
    # minCost[n] = min(minCost[n-1] + cost[n-1], minCost[n-2] + cost[n-2])     