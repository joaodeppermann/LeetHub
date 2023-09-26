class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        # Edge case: First row
        
        2
        1
        1
        # Pattern: each node will have as children the following row index i and i + 1
        prev_row = [poured]
        for row in range(1, query_row + 1):
            # Create child row
            cur_row = [0]*(row + 1)
            # Traverse parent row
            for j in range(row):
                extra = prev_row[j] - 1
                if extra > 0:
                    cur_row[j] += extra / 2
                    cur_row[j + 1] += extra / 2
            prev_row = cur_row
        return min(1, prev_row[query_glass])