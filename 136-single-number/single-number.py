class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        s = set(nums)
        total = 0
        for num in nums :
            total += num
        return 2*sum(s) - total
        """

        #Now use XOR 
        ans = 0
        for num in nums:
            ans ^= num
        return ans
        
        """
        s = set()
        for num in nums :
            if num in s :
                s.remove(num)
            else:
                s.add(num)
        return s.pop()
        """
        #Using defaultdict

        """
        from collections import defaultdict

        d = defaultdict(int)

        for num in nums:
                d[num] += 1
        for num,count in d.items():
            if count == 1:
                return num
        """
        