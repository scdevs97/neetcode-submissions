class KthLargest:
    stream = []
    k = 0

    def __init__(self, k: int, nums: List[int]):
        self.stream = nums
        self.k = k    

    def add(self, val: int) -> int:
        self.stream.append(val)
        sortedStream = sorted(self.stream)
        return sortedStream[-self.k]
