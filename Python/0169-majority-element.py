import math
# My solution:
# Time: O(N)
# Space: O(N)
# import math
# from collections import defaultdict

# class Solution:
#     def majorityElement(self, nums: 'List[int]') -> 'int':
#         size = len(nums)
#         limit = math.floor(size/2)
#         ele_counter = defaultdict(int)
        
#         for i in range(size):
#             ele = nums[i]
#             if ele_counter[ele] == limit:
#                 return nums[i]
#             ele_counter[ele] += 1


# Solutions from Grandyang's blog
# Time: O(N)
# Space: O(1), use constant time space
# Method: Moore voting
# Based on assumption: the majority element always appears in the array
# The number of elements in the array must be odd

class Solution:
    def majorityElement(self, nums: 'List[int]') -> 'int':
        res = 0
        counter = 0
        limit = math.floor(len(nums) / 2)
        
        for num in nums:
            if counter == 0:
                res = num
                counter = 1
            elif res == num:
                if counter == limit:
                    return res
                counter += 1
            elif res != num:
                counter -= 1
        return res
    
    
# Another method: bit manipulation
# Implement later
        
            
