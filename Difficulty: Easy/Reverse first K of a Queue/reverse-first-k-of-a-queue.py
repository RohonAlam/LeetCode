class Solution:
    def reverseFirstK(self, q, k):
        #code here 
        if k > len(q) :
            return q
            
        stack = []
        
        for i in range(k) :
            stack.append(q.popleft())
        while stack :
            q.append(stack.pop())
        for i in range(len(q)-k) :
            q.append(q.popleft())
        return q