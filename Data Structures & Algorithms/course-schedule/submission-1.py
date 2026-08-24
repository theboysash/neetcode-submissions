class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {c: [] for c in range(numCourses)}
        for course, prereq in prerequisites:
            graph[course].append(prereq)
        state= {} #stores 0 for visiting 1 for visitied

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
        