class Solution:
    def maxArea(self, height: List[int]) -> int:
        #Two Pointer solution
        left = 0 
        right = len(height)-1
        current_water = 0 
        max_water = 0 

        while left < right:
            hght = min (height[left],height[right])
            width = right - left
            current_water = hght * width 
            max_water = max(current_water,max_water)

            if height[left]<height[right]:
                left += 1
            else:
                right -= 1 
        
        return max_water

        # Brute Force
        # max_area = 0
        # n = len(height)

        # for i in range(n):
        #     for j in range(i + 1, n):
        #         width = j - i
        #         h = min(height[i], height[j])
        #         area = width * h

        #         max_area = max(max_area, area)

        # return max_area        