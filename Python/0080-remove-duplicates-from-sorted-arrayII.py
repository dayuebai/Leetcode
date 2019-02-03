# Given a sorted array nums, remove the duplicates in-place such that duplicates appeared at most twice and return the new length.
#
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.


# Time complexity: O(N), N: number of elements in the input array
# Space complexity: O(1), in place modification
class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        if size <= 2:
            return size

        new_size = 2
        for i in range(2, size):
            tmp = nums[i]
            if tmp != nums[new_size - 2]:
                nums[new_size] = tmp
                new_size += 1
        return new_size

s = Solution()
arr = [1,1,1,2,2,3]
assert(s.removeDuplicates(arr) == 5)
print(arr)
