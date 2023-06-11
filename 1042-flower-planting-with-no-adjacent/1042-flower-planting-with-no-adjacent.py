class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        # create a graph
        graph = {i:[] for i in range(1, n + 1)}
        
        # add edges
        for path in paths:
            graph[path[0]].append(path[1])
            graph[path[1]].append(path[0])
        
        # here is our solution vector where res[i] represents color of garden i+1
        res = [0]*n
                
        # For each garden
        for i in range(1, n + 1):
            # vector that checks which colors are already taken among the neighbors
            colors_used = [0]*4
            # fill up colors_used array
            for neighbor in graph[i]:
                # check if neighbor is already painted or not 
                color_neighbor = res[neighbor - 1]
                if color_neighbor:
                    colors_used[color_neighbor - 1] = 1
            # paint current house with the first color that is available
            for j in range(4):
                if colors_used[j] == 0:
                    res[i - 1] = j + 1
        return res