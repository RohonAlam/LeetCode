class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:

        #Brute Force
        """
        ans = set()
        n = len(nums)

        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if nums[i] + nums[j] + nums[k] == 0:
                        triplet = tuple(sorted([
                            nums[i],
                            nums[j],
                            nums[k]
                        ]))
                        ans.add(triplet)

        return [list(triplet) for triplet in ans]
"""              

        nums.sort()
        n = len(nums)
        result = []
        for i in range(n-2):
            if nums[i]>0: # all remaining numbers are also positive.
                break
            if i>0 and nums[i] == nums[i-1]:
                continue

            left = i + 1
            right = n-1

            while left < right :
                total = nums[i] + nums[left] + nums[right]

                if total < 0 :
                    left += 1
                
                elif total > 0 :
                    right -= 1
                
                else :
                    result.append([nums[i],nums[left],nums[right]])
                    while left< right and nums[left] == nums[left+1]:
                        left += 1
                    while left <right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
        return result
        