class MyStack:

    def __init__(self):
        self.data = []
        self.value_count = 0

    def push(self, x: int) -> None:
        self.data.append(x)
        self.value_count+=1
        
    def pop(self) -> int:
        self.value_count-=1
        return self.data.pop()

    def top(self) -> int:
        return self.data[-1]

    def empty(self) -> bool:
        return self.value_count == 0
