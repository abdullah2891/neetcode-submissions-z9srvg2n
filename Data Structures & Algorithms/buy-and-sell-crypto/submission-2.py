class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0 

        l = 0
        r = 1

        while l < len(prices) and r < len(prices):
            profit = prices[r] - prices[l]    
            # print(fit)
            while profit > 0 and r < len(prices):
                # print(profit,r, l)
                profit = prices[r] - prices[l]
                ans = max(ans, profit)
                r += 1 

            if profit <= 0:
                l += 1 
                r = l + 1

        return ans