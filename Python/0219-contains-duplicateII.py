# Time: O(N)
# Space: O(N)
class Solution:
    def containsNearbyDuplicate(self, nums: 'List[int]', k: 'int') -> 'bool':
        ele_map = {}
        size = len(nums)
        
        for i in range(size):
            ele = nums[i]
            if ele not in ele_map:
                ele_map[ele] = i
            else:
                if abs(i - ele_map[ele]) <= k:
                    return True
                else:
                    ele_map[ele] = i
        return False
