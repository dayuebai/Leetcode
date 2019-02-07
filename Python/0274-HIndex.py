# H-index wiki page: https://en.wikipedia.org/wiki/H-index
# Formula: max_i min(f(i), i)
# Time complexity: O(NlogN) depended on which sort algorithm you use. The best case could be O(N)
# Space complexity: O(1)
class Solution:
    def hIndex(self, citations: 'List[int]') -> 'int':
#         citations.sort(reverse = True)
#         size = len(citations)
#         result = 0
        
#         for i in range(size):
#             if citations[i] >= i + 1:
#                 result = i + 1
#         return result
    
    # better solution:
        
        citations.sort(reverse = True)
        size = len(citations)
        
        for i in range(size):
            if citations[i] <= i:
                return i
            
        return size
