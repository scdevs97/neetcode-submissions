class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_map = defaultdict(int)
        for i in nums:
            count_map[i] += 1
        tuple_list = [(count_map[i], i) for i in count_map]
        tuple_list.sort(key=lambda x: -x[0])
        
        return [tuple_list[i][1] for i in range(len(tuple_list)) if i < k]