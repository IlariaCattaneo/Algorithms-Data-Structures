class List:
    def __init__(self, value):
        self.value = value
        self.next = None

def print_list(l):
    while l != None:
        print(l.value)
        l = l.next

# Invert the Order of a Single-Link List
def reverse_list(l):
    new_list = None
    while l != None:
        next_l = l.next
        l.next = new_list
        new_list = l
        l = next_l
    return new_list
        
# Concatenating Two Single-Link Lists
def concatenate_lists(l1, l2):
    if l1 == None:
        return l2
    new_list = l1
    while new_list.next != None:
        new_list = new_list.next
    new_list.next = l2
    return l1



class DoubleList:
    def __init__(self, value):
        self.value = value
        self.next = self
        self.prev = self

def list_append (l, v):
    n = List()
    n.prev = l.prev
    n.next = l
    n.prev.next = n
    n.next.prev = n

def print_list(sentinel):
    l = sentinel.next
    while l != sentinel:
        print(l.value)
        l = l.next

# Invert the Order of a Doubly-Linked List
def reverse_double_list(l):
    pass

# Concatenating Two Doubly-Linked Lists
def concatenate_double_lists(l1, l2):
    pass