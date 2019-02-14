"""
Time: O(N)
Space: O(1)
"""
class Solution:
    def increasingTriplet(self, nums: 'List[int]') -> 'bool':
        if nums == None or len(nums) < 3:
            return False
        
        m1, m2 = math.inf, math.inf
        
        for num in nums:
            if m1 >= num:
                m1 = num
            elif m2 >= num:
                m2 = num
            else:
                return True
        return False