class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # from collections import Counter
        # stack = []
        # m= len(s1)
        # cnt = Counter(s1)
        # for ch in s2:
        #     stack.append(ch)

        #     if len(stack)>=m and Counter(stack[-m:]) == cnt :
        #         return True
        # return False
        
        from collections import Counter

        n = len(s2)
        m = len(s1)

        left = 0

        if m > n :
            return False
        
        right = 0 
        cnt1 = Counter(s1)
        cnt2 = Counter()

        while right<n:
            cnt2[s2[right]] += 1

            if right - left + 1 > m :
                cnt2[s2[left]] -= 1

                if cnt2[s2[left]] == 0:
                    del cnt2[s2[left]]

                left += 1
            
            if cnt1 == cnt2 :
                return True
            
            right += 1
        
        return False
