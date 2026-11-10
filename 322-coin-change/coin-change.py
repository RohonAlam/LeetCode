class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        """
        Greedy solution doesn't work alwasys.
        """
        """
        coins.sort()

        n = len(coins)
        rem = amount
        count = 0
        for i in range(n-1,-1,-1) :
            print(coins[i])
            if rem == 0 :
                break
            elif rem % coins[i]==0  :
                count += rem//coins[i]
                break
            elif rem < coins[i] :
                continue
            else :
                count += rem// coins[i]
                rem = rem - (count* coins[i])
        return count
        """
        dp = [float('inf')] * (amount+1)

        dp[0] = 0

        for i in range(1,amount+1):
            for  c in coins:
                if i>=c :
                    dp[i] = min(dp[i],1+dp[i-c])
        
        return dp[amount] if dp[amount]!= float('inf') else -1



        