class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
    
        memo = {}
        def dfs(curSum):
            # Check cache
            if curSum in memo:
                return memo[curSum]
        
            # Base cases
            if curSum > amount:
                return -1
            if curSum == amount:
                return 0
        
            # Analyse all the paths and get minimum cost
            min_cost = +inf
            for coin in coins:
                res = dfs(curSum + coin)
                if res != -1:
                    min_cost = min(min_cost, res + 1)
            
            # Cache the return value of the dfs function
            memo[curSum] = min_cost
            return memo[curSum] if min_cost != +inf else -1
        return dfs(0)