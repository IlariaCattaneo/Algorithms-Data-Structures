# initialize a doubly linked list
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        
class DoublyLinkedList:
    def __init__(self):
        self.sentinel = Node(None)
        self.sentinel.next = self.sentinel
        self.sentinel.prev = self.sentinel

    def insert_after(self, value, position):
        x = Node(value)
        x.next = position.next
        x.prev = position
        position.next.prev = x
        position.next = x

    def is_empty(self):
        return self.sentinel.next == self.sentinel and self.sentinel.prev == self.sentinel
