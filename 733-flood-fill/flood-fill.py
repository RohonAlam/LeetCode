from collections import deque
class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        
        if image[sr][sc] == color :
            return image

    
        queue = deque([(sr,sc)])
        cl = image[sr][sc] #Old color

        m = len(image)
        n = len(image[0])

        directions = [
            (1,0),
            (-1,0),
            (0,1),
            (0,-1)
        ]

        #Mark visited before starting loop
        image[sr][sc] = color       


        while queue :
            cr,cc = queue.popleft()

            for dr,dc in directions :
                nr = cr + dr
                nc = cc + dc

                if 0<= nr < m and 0 <= nc < n and image[nr][nc] == cl :
                    image[nr][nc] = color
                    queue.append((nr,nc))
       
        return image
        
        

        