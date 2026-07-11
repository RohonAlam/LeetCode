class Solution:
    def myPow(self, x: float, n: int) -> float:
        #Binary Exponentiation 
        if n<0:
            x = 1/x 
            n = -n
        ans = 1
        while n:
            if n & 1 :
                ans *= x
            
            x *= x
            n >>= 1
        
        return ans 

        #Brute force

        # power = abs(n)
        # ans = 1.0

        # for _ in range(power):
        #     ans *= x

        # if n < 0:
        #     return 1 / ans

        # return ans        






















