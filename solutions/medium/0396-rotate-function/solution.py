# Rotate Function
# Difficulty : Medium
# Tags       : Array, Math, Dynamic Programming
# Language   : python3
# Runtime    : 134 ms
# Memory     : 30.9 MB
# Link       : https://leetcode.com/problems/rotate-function/

class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        f, n, numSum = 0, len(nums), sum(nums)
        for i, num in enumerate(nums):
            f += i * num
        res = f
        for i in range(1, n):
            f = f + numSum - n * nums[n-i]
            res = max(res, f)
        return res