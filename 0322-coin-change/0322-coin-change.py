class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        dp = [+inf]*(amount+1)
        dp[0] = 0
        for a in range(amount + 1):
            for coin in coins:
                if a - coin >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - coin])
        return dp[-1] if dp[-1] != +inf else -1