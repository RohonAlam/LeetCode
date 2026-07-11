class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        #Brute Force
        # nums1[m:] = nums2
        # nums1.sort()

        #Using Extra Array(Two pointer/mergesort)
        # res = []
        # i=j = 0

        # while i <m and j <n :
        #     if nums1[i]<=nums2[j]:
        #         res.append(nums1[i])
        #         i += 1
        #     else:
        #         res.append(nums2[j])
        #         j += 1
        # while i<m:
        #     res.append(nums1[i])
        #     i+=1
        # while j<n:
        #     res.append(nums2[j])
        #     j+=1

        # nums1[:] = res


        #Using Three pointers from back
        i = m-1
        j = n-1
        idx = m+n-1
        
        while(i>=0 and j >=0):
            if(nums1[i]>=nums2[j]):
                nums1[idx] = nums1[i]
                i -= 1
                idx -=1
            else:
                nums1[idx] = nums2[j]
                j -= 1
                idx -= 1
        while(j>=0):
            nums1[idx] = nums2[j]
            j -= 1 
            idx -= 1