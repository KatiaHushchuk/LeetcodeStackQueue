class Node:
    def __init__(self, value, freq = 1, next= None):
        self.data = value
        self.frequency = freq
        self.next = next

class FreqStack:

    def __init__(self):
        self.head = None

    def push(self, val: int) -> None:
        if self.head:
            freq = 0
            curr = self.head
            while curr:
                if curr.data == val:
                    freq = curr.frequency
                    break
                curr = curr.next
            first = Node(val, freq + 1, self.head)
            self.head = first
        else:
            self.head = Node(val)

    def pop(self) -> int:
        if not self.head.next:
            val = self.head.data
            self.head = None
            return val
        max_freq = 0
        curr = self.head
        while curr:
            if max_freq < curr.frequency:
                max_freq = curr.frequency
            curr = curr.next
        curr = self.head
        if max_freq == curr.frequency:
            self.head = self.head.next
            return curr.data
        while curr.next:
            if curr.next.frequency == max_freq:
                el = curr.next.data
                curr.next = curr.next.next
                return el
            curr = curr.next
        el = self.head.data
        self.head = self.head.next
        return el
