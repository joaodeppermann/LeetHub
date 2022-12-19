class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        curPath = []
        def dfs(i, newTarget):
            # base cases
            if newTarget == 0:
                res.append(curPath[:])
                return 
            if newTarget < 0 or i == len(candidates):
                return 
            
            # pick the numebr 
            curPath.append(candidates[i])
            dfs(i, newTarget - candidates[i])
            
            # stop picking the number
            curPath.pop()
            dfs(i + 1, newTarget)
            
        dfs(0, target)
        return res
        
    