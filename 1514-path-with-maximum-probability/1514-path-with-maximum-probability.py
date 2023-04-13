class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        adj_list = {i:[] for i in range(n)}
        
        for i, edge in enumerate(edges):
            adj_list[edge[0]].append((edge[1], succProb[i]))
            adj_list[edge[1]].append((edge[0], succProb[i]))
            
        dist = [+inf]*n
        dist[start] = -1
        
        visited = [False]*n
        
        minHeap = []
        heapq.heapify(minHeap)
        heapq.heappush(minHeap, (-1, start))
        
        while minHeap:
            curDist, curNode = heapq.heappop(minHeap)
            visited[curNode] = True
            if curNode == end:
                return curDist*-1    
            for nextNode, nextCost in adj_list[curNode]:
                if visited[nextNode]:
                    continue            
                nextDist = nextCost*curDist
                if nextDist < dist[nextNode]:
                    dist[nextNode] = nextDist
                    heapq.heappush(minHeap, (nextDist, nextNode))
            
        return 0