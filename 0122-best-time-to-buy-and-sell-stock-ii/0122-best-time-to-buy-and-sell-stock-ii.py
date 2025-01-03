class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy=0
        sell=1
        profit=0
        while sell<len(prices):
            if prices[sell]>prices[buy]:
                profit+=prices[sell]-prices[buy]                
                buy=sell
            else:
                buy=sell
            sell+=1
        return profit
        