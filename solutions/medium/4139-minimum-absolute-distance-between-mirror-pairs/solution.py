# Minimum Absolute Distance Between Mirror Pairs
# Difficulty : Medium
# Tags       : Array, Hash Table, Math
# Language   : python3
# Runtime    : 203 ms
# Memory     : 42 MB
# Link       : https://leetcode.com/problems/minimum-absolute-distance-between-mirror-pairs/

class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        lastOcc = {}
        lastOcc[int(str(nums[0])[::-1])] = 0

        INF = 10**18
        res = INF

        for j in range(1, len(nums)):
            if nums[j] in lastOcc:
                res = min(res, j - lastOcc[nums[j]])
            lastOcc[int(str(nums[j])[::-1])] = j

        return -1 if res == INF else res
        