# initialize a linked list
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.first = None

    def print_values(self):
        node = self.first
        while node != None:
            print(node.value)
            node = node.next

    def insert(self, value, position):
        new_node = Node(value)
        if position == 0:
            new_node.next = self.first
            self.first = new_node
        else:
            current = self.first
            for _ in range(position-1):
                if current == None:
                    raise Exception("Position out of bounds")
                current = current.next
            new_node.next = current.next
            current.next = new_node

