class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit, maxP, minP = 0,0, prices[0]
        for i in range(len(prices)):
            minP = min(prices[i], minP)
            profit = prices[i] - minP
            maxP = max(maxP, profit)
        return maxP    