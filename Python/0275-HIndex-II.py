class Solution:
    def hIndex(self, citations: 'List[int]') -> 'int':
        # To solve it in O(log N)
        # We probably come up with how to apply binary search
        # to solve the problem
        size = len(citations)
        l, r = 0, size - 1
        
        while (l <= r):
            m = (l + r) // 2
            if citations[m] == size - m:
                return size - m
            elif citations[m] > size - m:
                r = m - 1
            else:
                l = m + 1
        return size - l
