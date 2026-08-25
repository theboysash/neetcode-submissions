class MinStack:

    def __init__(self):
        self.stack  = []
       
       

    def push(self, val: int) -> None:
        self.stack.append(val)
        return
       

    def pop(self) -> None:
        del self.stack[len(self.stack)-1]
        return
           
        
        

    def top(self) -> int:
        x = self.stack[len(self.stack) - 1]
        return x

        
       
    
    def getMin(self) -> int:
        return min(self.stack)
        
        

