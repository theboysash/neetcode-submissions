class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph ={i:[] for i in range(numCourses)}
        for course, pre in prerequisites:
            graph[course].append(pre)
        state = {}

        def dfs(course):
            if course in state:
                return state[course] == 1
            state[course] = 0 
            for pre in graph[course]:
                if not dfs(pre):
                    return False
            state[course] = 1
            return True
        return all (dfs(c) for c in range(numCourses))
        