import unittest


# Time complexity: O(N), N: number of elements in the input array
# Space complexity: O(1): in place modification
class Solution:

    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ref = None
        new_size = 0
        size = len(nums)
        for j in range(size):
            cmp = nums[j]
            if cmp != ref:
                nums[new_size] = cmp
                ref = cmp
                new_size += 1
        return new_size


# Test
solution = Solution()
test_arr = [1,1,2,3,3,4,4,5]
solution.removeDuplicates(test_arr)


class TestSolution(unittest.TestCase):
    def test_equal(self):
        self.assertEqual(solution.removeDuplicates([]), 0)
        self.assertEqual(solution.removeDuplicates([1,2]), 2)
        self.assertEqual(solution.removeDuplicates([1,1,2,2,2]), 2)
        self.assertEqual(solution.removeDuplicates([1,2,3,3,3]), 3)

    def test_element(self):
        self.assertEqual(test_arr[4], 5)


if __name__ == "__main__":
    unittest.main()
