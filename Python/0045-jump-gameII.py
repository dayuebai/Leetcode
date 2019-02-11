# Time:  O(n)
# Space: O(1)
class Solution:
    # Greedy algorithm solution
    def jump(self, nums: 'List[int]') -> 'int':
        result = 0
        curMaxJump = 0
        maxJump = 0
        size = len(nums)
        
        if size < 2:
            return 0
        for i in range(size-1):
            maxJump = max(maxJump, i + nums[i])
            if i == curMaxJump:
                result += 1
                curMaxJump = maxJump
        return result

    
    # bfs solution
    # different from greedy algorithm solution
    # bfs loop through the range within current max
    # if it find max > length - 1
    # then it can terminate the loop earlier