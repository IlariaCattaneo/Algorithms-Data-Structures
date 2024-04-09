# initialize a linked list
class ListElement:
    def __init__(self, value):
        self.value = value
        self.next = None

first = None

def list_push(value):
    global first
    # insert value at the beginning of the list
    new_node = ListElement(value)
    new_node.next = first
    first = new_node

def print_values():
    global first
    l = first
    while l != None:
        print(l.value)
        l = l.next

def list_pop():
    global first
    # extract the first element from the list
    assert first != None, "Empty list"
    result = first.value
    first = first.next
    return result



