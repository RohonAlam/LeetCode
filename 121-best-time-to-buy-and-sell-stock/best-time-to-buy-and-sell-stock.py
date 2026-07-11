class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        max_profit = 0 
        profit = 0 
        best_buy = prices[0]
        best_sell = prices[0]

        for i in range(0,len(prices)):
            if prices[i] <= best_buy :
                best_buy = prices[i]
            else:
                profit = prices[i]-best_buy
                if  profit > max_profit:
                    max_profit = profit
        return max_profit
        """
        #Prefix Minimum
        
        min_price = prices[0]
        max_profit = 0

        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)

        return max_profit

        # Brute Force
"""
        n = len(prices)
        ans = 0 
        for i in range(n):
            for j in range(i+1,n):
                if prices[j]>prices[i]:
                    ans = max(ans,prices[j]-prices[i])
        return ans
"""
            

        