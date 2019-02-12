class Solution:
    def maxProfit(self, k: 'int', prices: 'List[int]') -> 'int':
        if prices == None or len(prices) < 2:
            return 0
        
        local = [0] * (k + 1)
        glob = [0] * (k + 1)
        size = len(prices)

        for i in range(size - 1):
            diff = prices[i + 1] - prices[i]
            for j in range(k, 0, -1):
                local[j] = max(glob[j-1]+(diff if diff>0 else 0), local[j]+diff)
                glob[j] = max(local[j],glob[j])
        return glob[k]