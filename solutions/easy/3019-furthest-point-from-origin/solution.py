# Furthest Point From Origin
# Difficulty : Easy
# Tags       : String, Counting
# Language   : python3
# Runtime    : 0 ms
# Memory     : 19.3 MB
# Link       : https://leetcode.com/problems/furthest-point-from-origin/

class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        l=0
        r=0
        o=0
        for i in moves:
            if i=='L':
                l+=1
            elif i=='R':
                r+=1
            else:
                o+=1
        count=abs(r-l)+o
        return count
        