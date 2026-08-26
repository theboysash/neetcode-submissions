class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #we make an adjacency list
        #We run a depth first search on the value, then dfs its prereqs
        #if we havent seen the node we mark it as seen
        #if we have seen the node we return False unless its finished
        #we dfs to the "Start", set that value to 1, and then poat order
        graph = {c: [] for c in range(numCourses)}
        for course, prereq in prerequisites:
            graph[course].append(prereq)
        #we now have our adjacency list 
        state = {}
        #we want to keep track of a state to know if weve gone past a node
        def dfs(course):
            if course in state:
                return state[course] == 1
            state[course] = 0
            for pre in graph[course]:
                if not dfs(pre):
                    return False
            state[course] = 1
            return True 
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
                