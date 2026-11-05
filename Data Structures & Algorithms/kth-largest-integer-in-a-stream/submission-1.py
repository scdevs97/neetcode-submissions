import heapq

class KthLargest:
    stream = []
    k = 0

    def __init__(self, k: int, nums: List[int]):
        heapq.heapify(nums)
        self.stream = nums
        self.k = k    

    def add(self, val: int) -> int:
        heapq.heappush(self.stream, val)
        return heapq.nlargest(self.k, self.stream)[-1]
