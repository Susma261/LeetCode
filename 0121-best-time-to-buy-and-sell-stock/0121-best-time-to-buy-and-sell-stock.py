class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy=0
        sell=1
        maxi=0
        while sell<len(prices):
            if prices[sell]>prices[buy]:
                profit=prices[sell]-prices[buy]
                if profit > maxi:
                    maxi=profit
            else:
                buy=sell
            sell+=1
        return maxi

        