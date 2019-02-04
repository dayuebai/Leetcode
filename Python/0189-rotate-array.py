# Time complexity: O(N)
# Space complexity: O(1)
class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if nums == []:
            return nums

        size = len(nums)
        pivot = (k - 1) % size + 1
        nums[:pivot], nums[pivot:] = nums[-pivot:], nums[:(size-pivot)]