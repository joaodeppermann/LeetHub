class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        l = 0
        minQueue = collections.deque()
        maxQueue = collections.deque()
        best = -1
        
        for r in range(len(nums)):
            # append val to the minQueue
            while minQueue and minQueue[-1][1] > nums[r]:
                minQueue.pop()
            minQueue.append((r, nums[r]))
            
            # append val to the maxQueue
            while maxQueue and maxQueue[-1][1] < nums[r]:
                maxQueue.pop()
            maxQueue.append((r, nums[r]))   
            
            while maxQueue[0][1] - minQueue[0][1] > limit:
                if l == maxQueue[0][0]:
                    maxQueue.popleft()
                if l == minQueue[0][0]:
                    minQueue.popleft()
                l += 1
            
            best = max(best, r - l + 1)
        
        return best
                
                
                
                
                
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        