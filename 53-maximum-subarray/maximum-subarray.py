class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        # Kadane's Algo
        n = len(nums)
        max_sum = float(-inf)
        current_sum = 0
        for i in range(n):
            current_sum = max(current_sum,0)
            current_sum += nums[i]
            
            max_sum = max(current_sum,max_sum)
        return max_sum



        #Better Brute Force
"""
        n = len(nums)
        max_sum = float(-inf)
        for i in range(n):
            current_sum = 0

            for j in range(i,n):
                current_sum += nums[j]
                max_sum = max(current_sum,max_sum)
        return max_sum
 """       
        #brute force

"""
        n = len(nums)
        max_sum = float(-inf)
        for i in range(n):
            for j in range(i,n):
                current_sum = 0 
                for k in range(i,j+1):
                    current_sum += nums[k]
                max_sum = max(current_sum,max_sum)
        
        return max_sum
"""


"""
        current_sum = nums[0]
        max_sum = nums[0]

        for i in range(1,len(nums)):
            current_sum = max(nums[i],current_sum+nums[i])
            max_sum = max(current_sum , max_sum)
        return max_sum
"""   