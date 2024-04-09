# initialize a doubly linked list
class DListElement:
    def __init__(self, value):
        self.value = value
        self.next = self
        self.prev = self

sentinel = DListElement(None)

def list_insert_after_sentinel(value, l):
    # insert value after element l
    new_element = DListElement(value)
    new_element.prev = l
    new_element.next = l.next
    new_element.prev.next = new_element
    new_element.next.prev = new_element

def list_insert_before_sentinel(value, l):
    # insert value after element l
    new_element = DListElement(value)
    new_element.next = l
    new_element.prev = l.prev
    new_element.prev.next = new_element
    new_element.next.prev = new_element

def list_insert_attheend(value):
    global sentinel
    list_insert_after_sentinel(value, sentinel)

def list_print_forward():
    global sentinel
    l = sentinel.next
    while l != sentinel:
        print(l.value)
        l = l.next

def list_print_backwards():
    global sentinel
    l = sentinel.prev
    while l != sentinel:
        print(l.value)
        l = l.prev
