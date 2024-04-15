class Node:
    '''class for nodes'''
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    '''class for stack'''
    def __init__(self):
        self.head = None

    def is_empty(self):
        '''returns true if stack is empty and false otherwise'''
        return not self.head

    def push(self, data):
        '''pushes data to the top of the stack'''
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        '''pops the top element of the stack'''
        if self.is_empty():
            return None
        node = self.head.data
        self.head = self.head.next
        return node

    def peek(self):
        '''returns the top element of the stack'''
        if self.is_empty():
            return None
        return self.head.data

class MyQueue:
    def __init__(self):
        self.queue = Stack()
        
    def push(self, x: int) -> None:
        reverse_new_stack = Stack()
        while not self.queue.is_empty():
            el = self.queue.pop()
            reverse_new_stack.push(el)
        self.queue.push(x)
        while not reverse_new_stack.is_empty():
            el = reverse_new_stack.pop()
            self.queue.push(el)

    def pop(self) -> int:
        return self.queue.pop()
        
    def peek(self) -> int:
        return self.queue.peek()

    def empty(self) -> bool:
        return self.queue.is_empty()
