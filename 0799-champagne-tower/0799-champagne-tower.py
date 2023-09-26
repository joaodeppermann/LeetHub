class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        # Edge case: First row
        
        2
        1
        1
        # Pattern: each node will have as children the following row index i and i + 1
        tower = [[0]*k for k in range(1, query_row + 7)]
        tower[0][0] = poured
        for i in range(query_row + 1):
            for j in range(i + 1):
                extra = tower[i][j] - 1
                if extra > 0:
                    tower[i + 1][j] += extra / 2
                    tower[i + 1][j + 1] += extra / 2
        return min(1, tower[query_row][query_glass])