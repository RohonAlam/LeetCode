from functools import lru_cache
class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:    
        

        n = len(nums)

        @lru_cache(None)  #I can use lru_cache(None) only when i am returing some valuesi in recursive calls

        def dp(i,sum) :
            if i == n :
                return 1 if sum == target else 0
                        
            return dp(i+1,sum + nums[i] ) + dp(i+1,sum - nums[i] )
            
        return dp(0,0)

        
        # Method 2 : Must use memoization or TLE will occur

        """



        n = len(nums)

        @lru_cache(None)
        def dp(i, curr_sum):
            if i == n:
                return 1 if curr_sum == target else 0

            add = dp(i + 1, curr_sum + nums[i])
            subtract = dp(i + 1, curr_sum - nums[i])

            return add + subtract

        return dp(0, 0)
        """




        