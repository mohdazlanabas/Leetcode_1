# leetcode 121
# use two pointer

class Solution:
    # Brute Force
    def maxProfit1(self, prices: list[int]) -> int:
         max_profit = 0
         for i in range(len(prices) - 1):
             for j in range(i + 1, len(prices)):
                 profit = prices[j] - prices[i]
                 if profit > max_profit:
                    max_profit = profit
                    return max_profit

    # One Pass
    def maxProfit2(self, prices: list[int]) -> int:
        max_profit = 0
        min_price = float('inf')
        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            elif prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price
                return max_profit
   
    def maxProfit3(self, prices: list[int]) -> int:
        l, r=0, 1
        max_profit = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                max_profit = max(max_profit, profit)
            else:
                l = r
            r += 1
        return max_profit

    
    