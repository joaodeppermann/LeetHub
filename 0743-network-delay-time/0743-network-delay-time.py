class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_list = {i:list() for i in range(1, n + 1)} # each graph with a list of its neighbors (weight_to_neighbor, neighbor)
        for source, target, weight in times:
            adj_list[source].append((weight, target))
        visited = set()
        min_heap = [(0, k)] # current_min_weight, current node 
        heapq.heapify(min_heap)
        res = 0
        
        while min_heap:
            cur_weight, cur_node = heapq.heappop(min_heap)
            if cur_node in visited:
                continue # this is not the best path
            visited.add(cur_node)
            res = max(res, cur_weight)
            # explore all the neighbors of the current node, adding possible weights to min_heap
            for neighbor_weight, neighbor_node in adj_list[cur_node]:
                new_weight = cur_weight + neighbor_weight
                heapq.heappush(min_heap, (new_weight, neighbor_node))
                
        return res if len(visited) == n else -1
                
                