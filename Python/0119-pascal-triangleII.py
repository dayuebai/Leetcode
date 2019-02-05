# Time: O(n^2)
# Space: O(k), k = rowIndex
class Solution:
    def getRow(self, rowIndex: 'int') -> 'List[int]':
        if rowIndex < 2:
            return [1] * (rowIndex + 1)

        tmp = [1] * (rowIndex + 1)
        for i in range(2, rowIndex + 1):
            for j in range(i-1, 0, -1):
                tmp[j] += tmp[j-1]
        return tmp
