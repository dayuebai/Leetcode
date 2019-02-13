"""
two pointer solution
improved based on one dp array solution
can be further improved using stack
TODO: implement stack solution

Current solution
Time: O(N)
Space: O(1)
"""
class Solution:
    def trap(self, height: 'List[int]') -> 'int':
        l = 0
        r = len(height) - 1
        result = 0
        
        while l < r:
            min_height = min(height[l], height[r])
            if height[l] == min_height:
                l += 1
                while l < r and min_height > height[l]:
                    result += min_height - height[l]
                    l += 1
            else:
                r -= 1
                while l < r and min_height > height[r]:
                    result += min_height - height[r]
                    r -= 1
        return result