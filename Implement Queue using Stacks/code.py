class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

class Stack:
    def __init__(self):
        self.top = None  

    def is_empty(self):
        return self.top is None

    def push(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node

    def pop(self):
        if self.is_empty():
            raise ValueError("Stack is empty")
        data = self.top.data
        self.top = self.top.next
        return data

    def peek(self):
        if self.is_empty():
            raise ValueError("Stack is empty")
        return self.top.data

class MyQueue:
    def __init__(self):
        self.in_stack = Stack()
        self.out_stack = Stack()

    def push(self, x: int) -> None:
        self.in_stack.push(x)

    def pop(self) -> int:
        self._move_to_out_stack()
        return self.out_stack.pop()

    def peek(self) -> int:
        self._move_to_out_stack()
        return self.out_stack.peek()

    def empty(self) -> bool:
        return self.in_stack.is_empty() and self.out_stack.is_empty()

    def _move_to_out_stack(self):
        if self.out_stack.is_empty():
            while not self.in_stack.is_empty():
                self.out_stack.push(self.in_stack.pop()) 
