class MinStack:
    def __init__(self):
        self.min = None
        self.stack = [] 

    def push(self, val: int) -> None:
        if self.min == None or self.min > val: self.min = val
        self.stack.insert(0, val)

    def pop(self) -> None:
        self.stack.pop(0) 
        mins = sorted([x for x in self.stack])
        self.min = mins[0] if len(mins) > 0 else None

    def top(self) -> int:
        return self.stack[0]
        
    def getMin(self) -> int:
        return self.min   
