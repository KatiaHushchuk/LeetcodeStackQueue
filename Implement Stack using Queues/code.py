class Node:
    '''class for nodes'''
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    '''class for queue'''
    def __init__(self):
        self.head = None

    def is_empty(self):
        '''returns true if stack is empty and false otherwise'''
        return not self.head

    def push(self, data):
        '''pushes data to the end of the queue'''
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        node = self.head
        while node.next:
            node = node.next
        node.next = new_node

    def pop(self):
        '''pops data from the front of the queue'''
        if self.is_empty():
            return None
        node = self.head.data
        self.head = self.head.next
        return node

    def peek(self):
        '''returns the data at the front of the queue'''
        if self.is_empty():
            return None
        return self.head.data

    def size(self):
        '''returns the size of the queue'''
        len_queue = 0
        current = self.head
        while current:
            len_queue += 1
            current = current.next
        return len_queue

class MyStack:
    def __init__(self):
        self.stack = Queue()

    def push(self, x: int) -> None:
        reverse_new_queue = Queue()
        while not self.stack.is_empty():
            el = self.stack.pop()
            reverse_new_queue.push(el)
        self.stack.push(x)
        while not reverse_new_queue.is_empty():
            el = reverse_new_queue.pop()
            self.stack.push(el)

    def pop(self) -> int:
        return self.stack.pop()
        
    def top(self) -> int:
        return self.stack.peek()

    def empty(self) -> bool:
        return self.stack.is_empty()
        
