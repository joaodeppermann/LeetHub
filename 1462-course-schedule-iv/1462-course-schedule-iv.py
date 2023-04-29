class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # init graph + auxiliary data structures
        in_degree = [0 for _ in range(numCourses)] # use array instead of hashmap to gain in memory efficiency
        adj_list = [list() for _ in range(numCourses)]
        all_prereq = [set() for _ in range(numCourses)] # if 4 is in the hashset of all_prereq[0], this means that 0 has 4 as a direct or indirect prerequisite

        # fill up graph + auxiliary data structures
        for prereq, course in prerequisites:
            adj_list[prereq].append(course) # from prereq you can go to course
            in_degree[course] += 1
            all_prereq[course].add(prereq)
            
        # start traversal with nodes with in_degree == 0
        nodes_in_degree_zero = []
        for i in range(numCourses):
            if in_degree[i] == 0:
                nodes_in_degree_zero.append(i)        
        
        # traverse topological sort 
        while nodes_in_degree_zero:
            cur_node = nodes_in_degree_zero.pop() # could have used a deque too 
            for neighbor in adj_list[cur_node]:
                all_prereq[neighbor] |= all_prereq[cur_node]
                # In Python, and many other programming languages, | is the bitwise-OR operation. |= is to | as += is to +, i.e. a combination of operation and asignment.
                # So var |= value is short for var = var | value.
                # A common use case is to merge two sets:
                # >>> a = {1,2}; a |= {3,4}; print(a)
                # {1, 2, 3, 4}
                
                # if you don't filter in_degree == 0, you will end up adding the node multiple times to the queue, TLE 
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    nodes_in_degree_zero.append(neighbor)
                        
        # list comprehension to return result 
        return [possible_prereq in all_prereq[course] for possible_prereq, course in queries]