class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        """
        # Dutch National Flag Algorithm
        left = 0 
        right = len(nums)-1
        idx = 0
        while idx<=right:
            if nums[idx] == 0:
                nums[left],nums[idx] = nums[idx],nums[left]
                left += 1
                idx += 1
                
            elif nums[idx] == 2:
                nums[right],nums[idx] = nums[idx],nums[right]
                right -= 1
            else :
                idx += 1
        
        # Brute Force
        # nums.sort()


        # Counting Frequencies
        # count = [0, 0, 0]

        # for num in nums:
        #     count[num] += 1

        # index = 0

        # for num in range(3):
        #     for _ in range(count[num]):
        #         nums[index] = num
        #         index += 1        

        

                  