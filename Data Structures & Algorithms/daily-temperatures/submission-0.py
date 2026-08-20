class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        for i in range(0, len(temperatures)):
            t = temperatures[i]

            while stack and temperatures[stack[-1]] < t:
                j = stack.pop()
                res[j] = i-j
            stack.append(i)
        return res
       
           