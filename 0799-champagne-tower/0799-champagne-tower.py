class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        # Pattern: each node will have as children the following row index i and i + 1
        tower = [[] for _ in range(query_row + 1)] # val = (volume, how much it overflowed)
        for i in range(query_row + 1):
            for j in range(i + 1):
                # Check how much we get from each parent
                from_left_parent = 0
                from_right_parent = 0
                # Only get from left parent if j > 0
                if j > 0:
                    from_left_parent = tower[i - 1][j - 1][1]/2
                # Only get from right parent if j != i
                if j < i:
                    from_right_parent = tower[i - 1][j][1]/2
                total = from_left_parent + from_right_parent if i != 0 else poured
                overflow = total - 1 if total > 1 else 0
                tower[i].append((min(total, 1), overflow))
        print(tower)
        return tower[query_row][query_glass][0]