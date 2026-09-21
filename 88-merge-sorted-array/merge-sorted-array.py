class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p = m-1
        q = n-1
        ptr = m+n-1

        while q >= 0:
            if p >= 0 and nums1[p] > nums2[q]:
                nums1[ptr] = nums1[p]
                p -= 1
            else:
                nums1[ptr] = nums2[q]
                q -= 1

            ptr -= 1

        