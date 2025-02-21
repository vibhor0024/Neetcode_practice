class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if len(prices) == 0 or len(prices) == 1:
            return 0

        
        profit = 0
        maxprofit = 0
        l=0
        r=1

        while r < len(prices):
            if prices[r] > prices[l]:
                profit = prices[r] - prices[l]
                maxprofit = max(maxprofit,profit)
            else:
                l = r
            r += 1
        
        return maxprofit

        