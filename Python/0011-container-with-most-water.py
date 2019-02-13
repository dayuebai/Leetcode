"""
Time: O(N)
Space: O(1)
Similar to question 42: Trapping rain water.
Use two pointer to keep track.
Tips: make assumption to find out which pointer we should move so that max_result can be possibly increased.
"""
class Solution:
    def maxArea(self, height: 'List[int]') -> 'int':
        size = len(height)
        left = 0
        right = size - 1
        result = 0
        
        while left < right:
            min_height = min(height[left], height[right])
            result = max(result, min_height * (right - left))
            while left < right and height[left]==min_height:
                left += 1
            while left < right and height[right]==min_height:
                right -= 1
        return result