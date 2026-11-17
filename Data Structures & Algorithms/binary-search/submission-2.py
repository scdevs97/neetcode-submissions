class Solution:
    def binarySearch(self, nums, target, start, end):
        if end < start:
            return -1
        middle = (start + end) // 2
        if nums[middle] == target:
            return middle
        elif nums[middle] < target:
            return self.binarySearch(nums, target, middle + 1, end)
        else:
            return self.binarySearch(nums, target, start, middle - 1)

    def search(self, nums: List[int], target: int) -> int:
        return self.binarySearch(nums, target, 0, len(nums) - 1)