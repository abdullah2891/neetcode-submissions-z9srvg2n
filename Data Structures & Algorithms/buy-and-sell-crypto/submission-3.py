class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0 

        l = 0
        r = 1

        while l < len(prices) and r < len(prices):
            profit = prices[r] - prices[l]    
        
            if profit > 0:
                r += 1 
                ans = max(ans, profit)
            else:
                l = r 
                r += 1




        return ans