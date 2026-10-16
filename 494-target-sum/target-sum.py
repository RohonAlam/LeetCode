from functools import lru_cache
class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:

        #Method 1 : TLE
        """

        n = len(nums)

        count = 0
        sum = 0 

        def dp(i,sum) :
            nonlocal count
            if i == n :
                if sum == target :
                    count += 1
                return
            
            dp(i+1,sum + nums[i] )
            dp(i+1,sum - nums[i] )
            
        
        dp(0,0)
        
        return count 

        """
        # Method 2 : Must use memoization or TLE will occur



        n = len(nums)

        @lru_cache(None)
        def dp(i, curr_sum):
            if i == n:
                return 1 if curr_sum == target else 0

            add = dp(i + 1, curr_sum + nums[i])
            subtract = dp(i + 1, curr_sum - nums[i])

            return add + subtract

        return dp(0, 0)




        