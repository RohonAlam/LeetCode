class Solution:
    def findPages(self, arr, k):
        # code here
        n = len(arr)
        
        if k > n :
            return -1
        
        low = max(arr)
        high = sum(arr)
        
        while low <= high:
            
            mid = low + (high- low)//2
            
            if self.can_allocate(arr,k, mid):
                high = mid -1
            else :
                low = mid+1
        return low
            
        
    
    def can_allocate(self,arr,k,max_pages):
        
        stud = 1
        curr_page = 0
        
        for pages in arr:
            if curr_page + pages <= max_pages:
                curr_page += pages
            else :
                stud += 1
                curr_page = pages
        
        return stud <= k