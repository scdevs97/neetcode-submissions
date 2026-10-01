class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        totalProduct = 1
        zero_indexes = []
        for i in range(len(nums)):
            n = nums[i]
            if n == 0:
                zero_indexes.append(i)
            else:
                totalProduct *= n
        if len(zero_indexes) > 1:
            return [0] * len(nums)
        if len(zero_indexes) == 1:
            return [0 if i not in zero_indexes else totalProduct for i in range(len(nums))]
        return [divide(totalProduct,n) for n in nums]

def divide(a: int, b: int) -> int:
    if a == -2^31 and b == -1:
        return 2^31 - 1
    
    sign = -1 if (a < 0) ^ (b < 0) else 1
    a = abs(a)
    b = abs(b)

    quotient = 0
    for i in range(31, -1, -1):
        if (b << i) <= a:
            a -= (b << i)
            quotient |= (1 << i)

    return sign * quotient

