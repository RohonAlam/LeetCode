class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #BRUTE FORCE
        # n = len(nums)
        # for n1 in nums:
        #     freq = 0
        #     for n2 in nums:
        #         if n1 == n2 :
        #             freq += 1
        #     if(freq >= n/2):
        #         return n1

        n = len(nums)
        m = defaultdict(int)
        for num in nums:
            m[num] += 1

        for key,value in m.items():
            if value >= n/2:
                return key


            