class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        n = len(nums)
        res = [-1] * n

        for i in range (2 * n):
            index = i%n
            

            while stack and nums[index] > nums[stack[-1]] :
                res[stack[-1]] = nums[index]
                stack.pop()
            if i < n :
                stack.append(index)
    
        return res




        