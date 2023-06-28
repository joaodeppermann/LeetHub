# Explanation of BFS Space Complexity: Min(M, N).
# Think about an example where dif(M, N) is big like 3x1000 grid. And the worst case is when we start from the middle of the grid.
# Imagine how the processed points form a shape in the grid. It will be like a diamond and at some point, it will reach the longer edge of the grid. The possible shape at time t would be:
# ......QXXXQ.........
# ....QXXXXXQ........
# ......QXXXQ.........
# So in this specific example (Q: points in the queue, .: not processed, X: processed) the number of the items in the queue is proportional with 3 because the smallest side limits the expanding.
# So the actual value will be Min(M, N)*a+b but since a and b are constants and independent than M and N, Space complexity becomes Min(M, N).

# Please comment if anything looks weird, needs clarification or simply wrong.




# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         ROWS, COLS = len(grid), len(grid[0])
#         DIRECTIONS = [[1, 0], [0, -1], [0, 1], [-1, 0]]
        
#         res = 0
#         visited = [[False for _ in range(COLS)] for _ in range(ROWS)]
        
#         def bfs(row, col):
#             queue = collections.deque()
#             queue.append((row, col))
            
#             while queue:
#                 cur_row, cur_col = queue.popleft()
#                 for row_offset, col_offset in DIRECTIONS:
#                     new_row, new_col = cur_row + row_offset, cur_col + col_offset
#                     if (new_row in range(ROWS) and 
#                         new_col in range(COLS) and 
#                         grid[new_row][new_col] == "1" and not
#                         visited[new_row][new_col]):
#                         visited[new_row][new_col] = True
#                         queue.append((new_row, new_col))
        
#         for row in range(ROWS):
#             for col in range(COLS):
#                 if grid[row][col] == "1" and not visited[row][col]:
#                     visited[row][col] = True
#                     res += 1
#                     bfs(row, col)
                    
#         return res
                    
                    
#  By not keeping track of what's already in the queue (and waiting to be processed) with a visited set, you will end up adding a lot of duplicates to the queue since adjacent cells are shared among surrounding cells. So your code would add an adjacent cell to the queue even though it's already there because it was adjacent to an earlier cell. As the grid grows large, you add more and more duplicates to the queue unnecessarily which causes the code to re-process the same cells multiple times and slow down. So you have to apply this optimization. I believe it's a standard thing to do for BFS in graphs. You can get a quantifiable answer if you run the code on your local IDE and compare the max/average queue size between both versions.
        
                
# class Solution:
#     # global variable to store the number of components
#     # accessible and modifiable within union() and find() functions
#     count = 0
    
#     def numIslands(self, grid: List[List[str]]) -> int:
#         ROWS, COLS = len(grid), len(grid[0])
#         DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
#         rank = {}
#         parent = {}
        
        
#         def union(u, v):
#             root_u, root_v = find(u), find(v)
#             if root_u == root_v:
#                 return # already connected
#             if rank[root_v] > rank[root_u]: # union by rank
#                 rank[root_v] += rank[root_u]
#                 parent[root_u] = root_v
#             else:
#                 rank[root_u] += rank[root_v]
#                 parent[root_v] = root_u
#             self.count -= 1
            
#         def find(u):
#             while parent[u] != u:
#                 parent[u] = parent[parent[u]] # path compression
#                 u = parent[u]
#             return u
        
#         for row in range(ROWS):
#             for col in range(COLS):
#                 # create component
#                 if grid[row][col] == "1":
#                     node_id = (row, col)
#                     rank[node_id] = 1
#                     parent[node_id] = node_id
#                     self.count += 1
                    
#         for row in range(ROWS):
#             for col in range(COLS):
#                 # merge components with its neighbors
#                 if grid[row][col] == "1":
#                     for row_offset, col_offset in DIRECTIONS:
#                         new_row, new_col = row + row_offset, col + col_offset
#                         if new_row in range(ROWS) and new_col in range(COLS) and grid[new_row][new_col] == "1":
#                             union((row, col), (new_row, new_col))
        
#         return self.count

        
        
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        DIRECTIONS = [(0, 1), (-1, 0), (0, -1), (1, 0)]
        visited = set()
        queue = collections.deque()
        res = 0 
        for row in range(0, ROWS):
            for col in range(0, COLS):
                if grid[row][col] == "1" and (row, col) not in visited:
                    res += 1
                    queue.append((row, col))
                    visited.add((row, col))
                    # explore all the neighbors
                    while queue:
                        cur_row, cur_col = queue.popleft()
                        for delta_row, delta_col in DIRECTIONS:
                            new_row = cur_row + delta_row
                            new_col = cur_col + delta_col
                            if (new_col in range(0, COLS) and
                                new_row in range(0, ROWS) and
                                (new_row, new_col) not in visited and
                                grid[new_row][new_col] == "1"):
                                visited.add((new_row, new_col))
                                queue.append((new_row, new_col))
        return res
                            
        
        
        
        
        
        
        
        
        
        
        
        
        
