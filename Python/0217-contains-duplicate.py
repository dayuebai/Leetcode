# Time: O(N)
# Space: O(N)

# Using hash table can improve time complexity.
# Another approach is to first sort the array
# and then check if there are two equal neighboring elements
# The time and space complexity of this method depends on
# which sort algorithm we use.
class Solution:
    def containsDuplicate(self, nums: 'List[int]') -> 'bool':
        # Use hash table
        ele_set = set()
        size = len(nums)
        
        for i in range(size):
            ele = nums[i]
            if ele not in ele_set:
                ele_set.add(ele)
            else:
                return True
        return False
