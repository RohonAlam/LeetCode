class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        #Floyd Cycle Detection
        
        slow = nums[0]
        fast = nums[0]

        # Phase 1: Find intersection inside the cycle
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        # Phase 2: Find cycle entrance
        slow = nums[0]

        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow
        
        # Brute Force
        """
        n = len(nums)

        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] == nums[j]:
                    return nums[i]
        """

        #Sorting
        """
        nums.sort()

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return nums[i]
        """ 
        #Frequency Array
        """
        count = [0] * len(nums)

        for num in nums:
            count[num] += 1

            if count[num] > 1:
                return num       
        """

        # Hash Set
        """
        seen = set()

        for num in nums:
            if num in seen:
                return num
            else:
                seen.add(num)
        """
        # Binary Search on the value range
        """
        left = 1
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            count = 0

            for num in nums:
                if num <= mid:
                    count += 1

            if count > mid:
                right = mid
            else:
                left = mid + 1

        return left    
        """