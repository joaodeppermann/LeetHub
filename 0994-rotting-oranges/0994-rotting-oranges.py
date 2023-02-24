class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0 , -1]]
        q = collections.deque()
        freshes_remaining, minutes_passed = 0, 0
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    freshes_remaining += 1
                elif grid[r][c] == 2:
                    q.append((r, c))
            
        while q and freshes_remaining:
            number_oranges_in_this_level = len(q)  # get the number of simultaneous bfs we need to perform
            for _ in range(number_oranges_in_this_level):
                cur_row, cur_col = q.popleft()
                for row_offset, col_offset in directions:
                    new_row, new_col = cur_row + row_offset, cur_col + col_offset
                    if new_row in range(ROWS) and new_col in range(COLS) and grid[new_row][new_col] == 1:
                        freshes_remaining -= 1
                        grid[new_row][new_col] = 2
                        q.append((new_row, new_col))
            minutes_passed += 1
            
        return minutes_passed if freshes_remaining == 0 else -1