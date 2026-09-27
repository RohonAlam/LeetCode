from collections import deque
class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
    
        visited = {(sr,sc)}
        queue = deque([(sr,sc)])
        cl = image[sr][sc]
        m = len(image)
        n = len(image[0])

        while queue :
            cr,cc = queue.popleft()
            image[cr][cc] = color 

            if cr+1 < m and image[cr+1][cc] == cl and (cr+1,cc) not in visited :
                queue.append((cr+1,cc))
                visited.add((cr+1,cc))        
            if cc+1 < n and image[cr][cc+1] == cl and (cr,cc+1) not in visited :
                queue.append((cr,cc+1))
                visited.add((cr,cc+1))
            if cr-1 >=0 and image[cr-1][cc] == cl and (cr-1,cc) not in visited :
                queue.append((cr-1,cc))
                visited.add((cr-1,cc))
            if cc-1 >= 0 and image[cr][cc-1] == cl and (cr,cc-1) not in visited :
                queue.append((cr,cc-1))
                visited.add((cr,cc-1))
        
        return image
        
        

        