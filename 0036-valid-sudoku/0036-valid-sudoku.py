class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {i:set() for i in range(9)}
        cols = {i:set() for i in range(9)}
        squares = {}
        for i in range(3):
            for j in range(3):
                squares[(i, j)] = set()
                
        for r in range(9):
            for c in range(9):
                # verify row condition 
                if board[r][c] != '.' and board[r][c] in rows[r]:
                    return False
                rows[r].add(board[r][c])
                
                # verify col condition 
                if board[r][c] != '.' and board[r][c] in cols[c]:
                    return False
                cols[c].add(board[r][c])
                
                # verify square condition 
                line = r // 3
                column = c // 3
                if board[r][c] != '.' and board[r][c] in squares[(line, column)]:
                    return False
                squares[(line, column)].add(board[r][c])
            
        return True
                