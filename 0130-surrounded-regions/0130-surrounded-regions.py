class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS, COLS = len(board), len(board[0])
        DIRECTIONS = [(0,1),(1,0),(-1,0),(0,-1)]
        
        def bfs(row, col):
            queue = deque()
            queue.append((row, col))
            while queue:
                cur_row, cur_col = queue.popleft()
                for row_offset, col_offset in DIRECTIONS:
                    new_row = cur_row + row_offset
                    new_col = cur_col + col_offset
                    if (new_row in range(ROWS) and
                        new_col in range(COLS) and
                        board[new_row][new_col] == "O"):
                        queue.append((new_row, new_col))
                        board[new_row][new_col] = "%"
            
        # Convert border island chars to "%"
        for row in range(ROWS):
            for col in range(COLS):
                if ((row == 0 or row == ROWS - 1 or
                    col == 0 or col == COLS - 1) and
                    board[row][col] == "O"):
                    board[row][col] = "%"
                    bfs(row, col)
                    
        # Convert remanining "O" (surrounded islands) to "X" and "%" back to "O"
        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == "%":
                    board[row][col] = "O"
                elif board[row][col] == "O":
                    board[row][col] = "X"

