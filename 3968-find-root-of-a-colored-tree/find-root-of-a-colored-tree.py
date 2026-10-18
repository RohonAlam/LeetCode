from collections import deque, defaultdict
class Solution:
    def findColoredRoot(self, edges: list[list[int]], colors: str) -> int:

        tree = defaultdict(list)

        for a ,b  in edges :
            tree[a].append(b)
            tree[b].append(a)
        
        

        def bfs(node,color) :

            queue = deque([node])
            
            queue.append(node)
            visited = {node}

            while queue :
                level_size = len(queue)

                for k in range(level_size) :
                    current  = queue.popleft()
                    if colors[current] != color :
                        return False
                    child = 0
                    for neighbor in tree[current] :
                        if neighbor not in visited:
                            child += 1
                            visited.add(neighbor)
                            queue.append(neighbor)
                    if child > 2 :
                        return False
                color = 'B' if color == 'R' else 'W' if color == 'B' else 'R'

            return True
        
        for i in range(len(edges)+1) :
            if bfs(i,colors[i]) :
                return i
        
        return -1
        
                

        