class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        res = []
        # add original index to the list to not lose this information
        for i in range(len(tasks)):
            tasks[i].append(i)
        # transform initial array into a min heap to always access the best (enqueue time, processing time, index)
        heapq.heapify(tasks)
        # get the first task to be the smallest enqueue time and smallest processing time 
        first_task = heapq.heappop(tasks)
        # next_tasks min heap contains (processing time, original index)
        # only valid tasks (enqueue time <= timestamp) are added to the min heap
        # edge case: when there are still tasks to process but none of the next tasks have enqueue time < timestamp 
        next_tasks = [(first_task[1], first_task[2])]
        # timestamp start with first task enqueue time
        timestamp = first_task[0]
        while next_tasks:
            # process the task with smallest processing time 
            cur_task = heapq.heappop(next_tasks)
            # get the list of possible next_tasks to process
            timestamp += cur_task[0]
            while tasks and (tasks[0][0] <= timestamp or not next_tasks):
                possible_next_task = heapq.heappop(tasks)
                # handle edge case, need to set timestamp to next enqueue time 
                if possible_next_task[0] > timestamp:
                    timestamp = possible_next_task[0]
                # add valid next task to the min heap; only (processing time, original index)
                heapq.heappush(next_tasks, (possible_next_task[1], possible_next_task[2]))
            res.append(cur_task[1])
        return res