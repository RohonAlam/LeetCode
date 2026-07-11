class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # BRUTE FORCE
        # n = len(nums)
        # for n1 in nums:
        #     freq = 0
        #     for n2 in nums:
        #         if n1 == n2 :
        #             freq += 1
        #     if(freq >= n/2):
        #         return n1


        #Using defaultdict
        # n = len(nums)
        # m = defaultdict(int)
        # for num in nums:
        #     m[num] += 1

        # for key, value in m.items():
        #     if value >= n / 2:
        #         return key

        #solving in O(1) space complexity
        #Moore's voting algorithm

        candidate = None
        count = 0

        for num in nums:
            if count == 0:
                candidate = num
            if num == candidate:
                count += 1
            else:
                count -= 1
        return candidate















