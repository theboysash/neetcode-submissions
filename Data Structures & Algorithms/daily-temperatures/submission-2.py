class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #We compare current to the top of stack
        #If current is greater then to->pop top(while)
        #append current to stack 

        stack = []
        vals = [0] * len(temperatures)
        for i in range(0, len(temperatures)):
            curr = temperatures[i]
            while stack and curr > temperatures[stack[-1]]:
                day = stack.pop()
                vals[day] = i - day
            stack.append(i)
        return vals


       