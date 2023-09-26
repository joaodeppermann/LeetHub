class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Dijkstra / Heap
        # Create graph
        graph = {i:[] for i in range(1, n + 1)} # Key = node, val = [(weight, neighbor)]
        
        # Fill up the graph 
        for source, target, weight in times:
            graph[source].append((weight, target))
            
        # Hash set to keep track of the nodes we have already visited
        visited = set()
        distances = [+inf]*(n+1)
        distances[k] = 0
        priority_queue = [(0, k)]
        while priority_queue:
            cur_dist, cur_node = heapq.heappop(priority_queue)
            # Skip nodes we have already visited
            if cur_node in visited:
                continue
            visited.add(cur_node)
            # Visit the neighbors
            for weight, neighbor in graph[cur_node]:
                new_dist = cur_dist + weight
                if new_dist < distances[neighbor]:
                    heapq.heappush(priority_queue, (new_dist, neighbor))
                    distances[neighbor] = new_dist
        
        return max(distances[1:]) if max(distances[1:]) != +inf else -1