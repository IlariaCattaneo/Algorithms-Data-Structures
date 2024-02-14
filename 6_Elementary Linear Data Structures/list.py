class list_element:
    def __init__(self, v, n):
        self.value = v
        self.next = n

L = None

def insert_after(x, v):
    x.next = list_element(v, x.next)

def insert_before(x, v):
    x = list_element(v, list_element

def find(x):
    # \Theta(n)
    l = L
    while l != None:
        if x == l.value:
            return True
        l = l.next
    return False

def get_element_at(i):
    # \Theta(n)
    l = L
    while l != None:
        if i == 0:
            return l.value
        i = i - 1
        l = l.next
    print('index ouf of bounds')

def is_empty():
    return L == None

def insert_front(x):
    global L
    L = list_element(x,L)
    
def delete_front():
    global L
    if L == None:
        print('list empty')
    else:
        L = L.next
    
def pop_front():
    global L
    if L == None:
        print('list empty')
    else:
        v = L.value
        L = L.next
        return v
    
def print_all():
    global L
    l = L
    while l != None:
        print(l.value)
        l = l.next
