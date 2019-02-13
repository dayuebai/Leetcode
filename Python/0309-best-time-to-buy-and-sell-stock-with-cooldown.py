"""
Time: O(N)
Space: O(1)
"""
class Solution:
    def maxProfit(self, prices: 'List[int]') -> 'int':
        if prices == None or len(prices) < 2:
            return 0
        buy1 = float("-inf")
        buy2 = 0
        sell1 = 0
        sell2 = 0
        for p in prices:
            buy2 = buy1
            buy1 = max(sell2-p, buy2)
            sell2 = sell1
            sell1 = max(buy2+p, sell1)
        return sell1
        