# Time complexity: O(N), N: number of elements in the input array
# Space complexity: O(1), in place modification
class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 0
        ref = nums[0]
        new_size = 1
        occurrence = 1
        size = len(nums)

        for i in range(1, size):
            cmp = nums[i]
            if cmp != ref:
                nums[new_size] = cmp
                ref = cmp
                occurrence = 1
                new_size += 1
            elif occurrence < 2:
                nums[new_size] = cmp
                occurrence += 1
                new_size += 1
        return new_size


s = Solution()
arr = [1,1,1,2,2,3]
assert(s.removeDuplicates(arr) == 5)