class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        #Brute Force
        """
        n = len(nums)
        ans = set()

        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    for l in range(k + 1, n):
                        if nums[i] + nums[j] + nums[k] + nums[l] == target:
                            quad = tuple(sorted([
                                nums[i],
                                nums[j],
                                nums[k],
                                nums[l]
                            ]))
                            ans.add(quad)

        return [list(quad) for quad in ans]        
        """

        #Sorting and Two pointer
        nums.sort()

        result = []

        n = len(nums)

        for i in range(n-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            # Smallest possible sum for this i
            if (nums[i]+ nums[i + 1]+ nums[i + 2]+ nums[i + 3]> target):
                break
            # Largest possible sum for this i
            if (nums[i]+ nums[n - 1]+ nums[n - 2]+ nums[n - 3]< target):
                continue

            for j in range (i+1,n-2):
                if j>i+1 and nums[j] == nums[j-1] :
                    continue

                left = j+1
                right = n -1

                while left < right :

                    total = nums[i] + nums[j] + nums[left] + nums[right]

                    if total < target :
                        left += 1

                    elif total > target :
                        right -= 1

                    else :
                        result.append([nums[i],nums[j],nums[left],nums[right]])
                    
                        while left < right and nums[left] == nums[left+1]:
                            left += 1

                        while left < right and nums[right] == nums[right-1]:
                            right -= 1
                        left += 1
                        right -= 1
        return result