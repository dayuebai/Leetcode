import math
# Based on the hint, we can derive there are at most two majority elements
# the input array can possibly have
# In addition, this question does not assume there must exists a majority element

# Apply Moore voting
# Time: O(N)
# Space: O(1)
class Solution:
    def majorityElement(self, nums: 'List[int]') -> 'List[int]':
        m1, m2, counter1, counter2 = 0, 0, 0, 0
        limit = math.floor(len(nums) / 3)
        result = []
        for num in nums:
            if num == m1:
                counter1 += 1
            elif num == m2:
                counter2 += 1
            elif counter1 == 0:
                m1 = num
                counter1 = 1
            elif counter2 == 0:
                m2 = num
                counter2 = 1
            else:
                counter1 -= 1
                counter2 -= 1
        
        # Since this question does not assume there must exists a majority element,
        # then we need to prove the two potential majority elements we find above
        # are real majority elements.
        counter1, counter2 = 0, 0
        for num in nums:
            if num == m1:
                counter1 += 1
            elif num == m2:
                counter2 += 1
                
        if counter1 > limit:
            result.append(m1)
        if counter2 > limit:
            result.append(m2)
        
        return result
