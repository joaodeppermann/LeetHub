class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Edge case
        if amount == 0:
            return 0
        memo = {}
        def dfs(remainder):
            # Check if we have already solved this problem
            if remainder in memo:
                return memo[remainder]
            # Base cases
            # 1. Solution not found in this path
            if remainder < 0:
                return -1
            # 2. Solution found in this path
            if remainder == 0:
                return 0
            
            # Try to use all the coins
            min_coins = +inf
            for coin in coins:
                res = dfs(remainder - coin)
                if res != -1:
                    # This path lead to a solution, check if it's optimal
                    min_coins = min(min_coins, res + 1)
            
            # Cache the result before returning
            memo[remainder] = min_coins
            # Return best solution we have found for this subproblem
            return min_coins
        dfs(amount)
        return memo[amount] if memo[amount] != +inf else -1