class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]* len(temperatures)
        stack = []
        for i in range(0, len(temperatures)):
            curr = temperatures[i]
            while stack and curr > temperatures[stack[-1]]:
                day = stack.pop()
                res[day] = i - day
            stack.append(i)
        return res
    
        