# Time: O(N)
# Space: O(1)
#
# Apply greedy algorithm
# Only care about the max index we can reach
# Set a variable: max_i to keep tracking the max index we can reach
# Iterate through the array to update the variable
# break if (a) max_i is smaller than current index
# which means it cannot even reach current position
# or (b) max_i is larger than the last postion index.
# If at the end max_i is larger than size -1
# then we can reach the last index.
#
# Note that in this question we don't have reach the last position exactly.
# We can even go beyond the last position index.
class Solution:
    def canJump(self, nums: 'List[int]') -> 'bool':
        size = len(nums)
        max_i = 0
        
        for i in range(size):
            if max_i < i or max_i >= size - 1:
                break
            max_i = max(max_i, i + nums[i])
        return max_i >= size - 1
