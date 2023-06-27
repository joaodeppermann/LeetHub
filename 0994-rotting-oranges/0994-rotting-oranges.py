from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        visited = set() # hash set containing explored coordinates
        freshes = 0 # number of fresh oranges
        res = 0 # minutes it took to rotten all the oranges
        ROWS, COLS = len(grid), len(grid[0])
        DIRECTIONS = [(0,1), (-1,0), (0,-1), (1,0)]
        # edge case where we are given an empty grid 
        if ROWS == 0 or COLS == 0:
            return -1
        queue = deque()
        # traverse the grid once and add to the BFS queue the intial rotten oranges
        for row in range(0, ROWS):
            for col in range(0, COLS):
                # add intial rotten orange to the queue 
                if grid[row][col] == 2:
                    queue.append((row, col))
                elif grid[row][col] == 1:
                    freshes += 1
                
        if freshes == 0:
            return 0
        
        # BFS through the grid starting by the queue mentioned previously 
        while queue:
            oranges_in_this_level = len(queue)
            while oranges_in_this_level != 0:
                cur_row, cur_col = queue.popleft()
                # visit 4 directions
                for delta_row, delta_col in DIRECTIONS:
                    new_row, new_col = cur_row + delta_row, cur_col + delta_col
                    # try to explore neighbour 
                    if (new_row in range(0, ROWS) and 
                        new_col in range(0, COLS) and 
                        (new_row, new_col) not in visited and
                        grid[new_row][new_col] == 1):
                        freshes -= 1
                        queue.append((new_row, new_col))
                        visited.add((new_row, new_col))
                oranges_in_this_level -= 1
            res += 1
            
        return res - 1 if freshes == 0 else -1