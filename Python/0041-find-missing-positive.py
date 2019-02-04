# Time: O(N), swap operation can make sure at least one element will be put at a correct position.
# Constant extra space
class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)

        for i in range(size):
            while nums[i] > 0 and nums[i] <= size and nums[i] != nums[nums[i] - 1]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

        for i in range(size):
            if nums[i] != i + 1:
                return i + 1
        return size + 1