class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char == '{' or char == '[' or char == '(':
                stack.append(char)
            elif char == '}' or char == ']' or char == ')':
                if not stack:
                    return False
                x = stack.pop()
                if x == '{' and char == '}':
                    continue
                elif x == '(' and char == ')':
                    continue
                elif x == '[' and char == ']':
                    continue
                else:
                    return False
        return not stack