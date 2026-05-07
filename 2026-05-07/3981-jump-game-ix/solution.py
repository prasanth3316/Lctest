# Jump Game IX
# Difficulty : Medium
# Tags       : Array, Dynamic Programming
# Runtime    : 348 ms
# Memory     : 40 MB
# Link       : https://leetcode.com/problems/jump-game-ix/

class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        pre=[0 for i in nums]
        rev=[0 for i in nums]
        res=[0 for i in nums]
        pre[0]=nums[0]
        for i in range(1,len(nums)):
            pre[i]=max(nums[i],pre[i-1])
        rev[len(nums)-1]=nums[-1]
        for i in range(len(nums)-2,-1,-1):
            rev[i]=min(nums[i],rev[i+1])
        print(pre)
        print(rev)
        res[-1]=pre[-1]
        for i in range(len(nums)-2,-1,-1):
            res[i]=pre[i]
            if pre[i]>rev[i+1]:
                res[i]=res[i+1]
        return res