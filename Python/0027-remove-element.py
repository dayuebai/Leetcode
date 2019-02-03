# Time Complexity: O(N), N: number of elements in the input array
# Space complexity: O(1), in place modification
class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        size = len(nums)
        new_size = 0

        for j in range(size):
            tmp = nums[j]
            if tmp != val:
                nums[new_size] = tmp
                new_size += 1
        return new_size


# Test
solution = Solution()
arr = [0,1,2,2,3,0,4,2]
assert(solution.removeElement(arr, 2) == 5)
