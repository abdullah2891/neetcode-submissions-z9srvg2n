class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0

        left = 0
        right = left + 1

        while left < len(prices) and right < len(prices):
            profit = prices[right] - prices[left]

            if profit > 0:
                while profit > 0 and right < len(prices):
                    # print(prices[left], prices[right], profit)
                    profit = prices[right] - prices[left]
                    ans = max(ans, profit)

                    right += 1 
                left = right - 1 

            else:
                left = right 
                right = left +  1
                # print('---', left, right)
                

            # print("+++++", left, right, profit)
        

        return ans