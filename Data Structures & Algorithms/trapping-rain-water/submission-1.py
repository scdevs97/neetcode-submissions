class Solution:
    def trap(self, height: List[int]) -> int:
        totalVol = 0
        q = deque([(height[0], 1)])

        for h in height:
            count = 1
            if h >= q[0][0]:
                while q:
                    totalVol += (q[0][0] - q[-1][0]) * q[-1][1] 
                    q.pop()
            else:
                while h > q[-1][0]:
                    totalVol += (h - q[-1][0]) * q[-1][1]
                    count += q[-1][1]
                    q.pop()

            q.append((h, count))
        
        return totalVol



            