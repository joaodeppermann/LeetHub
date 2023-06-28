class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        frequencies = Counter(tasks).values()
        max_heap = [-freq for freq in frequencies]
        heapq.heapify(max_heap)
        
        timestamp = 0
        prob_tasks = collections.deque()
        while prob_tasks or max_heap:
            if max_heap:
                cur_task = heapq.heappop(max_heap)
                cur_task += 1
                if cur_task < 0:
                    prob_tasks.append((cur_task, timestamp + n + 1))
            # check if there is a freq coming back to the game
            if prob_tasks and prob_tasks[0][1] == timestamp + 1:
                heapq.heappush(max_heap, prob_tasks.popleft()[0])        
            timestamp += 1
        return timestamp
        
# If len(frequencies) = k
# TC = O(k*log(k))
# SC = O(k)