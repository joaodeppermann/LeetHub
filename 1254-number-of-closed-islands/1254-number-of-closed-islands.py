class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        DIRECITONS = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        visited = set()
        
        def bfs(row, col):
            queue = collections.deque()
            queue.append((row, col))
            while queue:
                cur_row, cur_col = queue.popleft()
                for row_offset, col_offset in DIRECITONS:
                    new_row = cur_row + row_offset
                    new_col = cur_col + col_offset
                    if (new_row in range(ROWS) and
                        new_col in range(COLS) and
                        grid[new_row][new_col] == 0 and 
                        (new_row, new_col) not in visited):
                        visited.add((new_row, new_col))
                        queue.append((new_row, new_col))
        
        # Mark islands connected to the border
        for row in range(ROWS):
            for col in range(COLS):
                if (row != 0 and row != ROWS - 1 and
                    col != 0 and col != COLS - 1):
                    continue
                if grid[row][col] == 0 and (row, col) not in visited:
                    visited.add((row, col))
                    bfs(row, col)
        
        res = 0
        # Count number of islands if you hit a cell that is not connected to the border
        for row in range(ROWS):
            for col in range(COLS):
                if (row == 0 or row == ROWS - 1 or
                    col == 0 or col == COLS - 1):
                    continue
                if grid[row][col] == 0 and (row, col) not in visited:
                    visited.add((row, col))
                    bfs(row, col)
                    res += 1
                        
        return res