class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # prices[i] == the price of ith day
        # maximize your profit
        profit=0
        min_buy=float("inf")
        
        for p in prices:
            if p<min_buy:
                min_buy=p
            if p - min_buy > profit:
                profit = p-min_buy

        return profit
