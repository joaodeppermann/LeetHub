class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [+inf]*(amount + 1)
        dp[0] = 0
        for a in range(1, amount + 1):
            for coin in coins:
                # Check if you can use the coin
                if coin <= a:
                    dp[a] = min(dp[a], 1 + dp[a - coin])
        return dp[amount] if dp[amount] != +inf else -1