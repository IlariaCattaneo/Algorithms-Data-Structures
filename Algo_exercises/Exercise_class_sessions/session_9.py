class Node:
    def __init__(self,k):
        self.key = k
        self.parent = None
        self.left = None
        self.right = None

def bst_insert(t, k):
    if t == None:
        return Node(k)
    x = t
    while True:
        if k <= x.key:
            if x.left == None:
                x.left = Node(k)
                x.left.parent = x
                return t
            x = x.left
        else:
            if x.right == None:
                x.right = Node(k)
                x.right.parent = x
                return t
            x = x.right

import random
t = None
for _ in range(20):
    t = bst_insert(t, random.randint(1,100))

class Canvas:
    def __init__(self,width):
        self.line_width = width
        self.canvas = []

    def put_char(self,x,y,c):
        if x < self.line_width:
            pos = y*self.line_width + x
            l = len(self.canvas)
            if pos < l:
                self.canvas[pos] = c
            else:
                self.canvas[l:] = [' ']*(pos - l)
                self.canvas.append(c)

    def print_out(self):
        i = 0
        sp = 0
        for c in self.canvas:
            if c != ' ':
                print(' '*sp, end='')
                print(c, end='')
                sp = 0
            else:
                sp += 1
            i = i + 1
            if i % self.line_width == 0:
                print('\n', end='')
                sp = 0
        if i % self.line_width != 0:
            print('\n', end='')

def print_binary_tree_r(t,x,y,canvas):
    max_y = y
    if t.left != None:
        x, max_y, lx, rx = print_binary_tree_r(t.left,x,y+2,canvas)
        x = x + 1
        for i in range(rx,x):
            canvas.put_char(i, y+1, '/')

    middle_l = x
    for c in str(t.key):
        canvas.put_char(x, y, c)
        x = x + 1
    middle_r = x

    if t.right != None:
        canvas.put_char(x, y+1, '\\')
        x = x + 1
        x0, max_y2, lx, rx = print_binary_tree_r(t.right,x,y+2,canvas)
        if max_y2 > max_y:
            max_y = max_y2
        for i in range(x,lx):
            canvas.put_char(i, y+1, '\\')
        x = x0

    return (x,max_y,middle_l,middle_r)

def print_tree_w(t,width):
    canvas = Canvas(width)
    print_binary_tree_r(t,0,0,canvas)
    canvas.print_out()

def print_tree(t):
    print_tree_w(t,20000)


# The height of a binary search tree
def bst_height(T):
    max = 0
    while T != None:
        if T.left != None and bst_height(T.left) > max:
            max = bst_height(T.left)
        if T.right != None and bst_height(T.right) > max:
            max = bst_height(T.right)
        return max + 1

# Count in range
def bst_count_in_range(T,a,b):
    print( T.key, a, b)
    assert a <= b
    count = 0
    # print(f'key: {T.key}')
    if T.left != None:
        print( 'left call')
        count += bst_count_in_range(T.left,a,b)
    if T.right != None:
        print( 'right call')
        count += bst_count_in_range(T.right,a,b)
    # print( f'count: {count}')
    if T.key >= a and T.key <= b:
        # print(f'key: {T.key}')
        print( f'element in range: {T.key}')
        return count + 1
    else:
        print( f'element not in range: {T.key}')
        return count

def bst_count_in_range_optimised(T,a,b):
    if T == None:
        return 0
    c = 0
    if a < T.key:
        c = c + bst_count_in_range(T.left,a,b)
    if b > T.key:
        c = c + bst_count_in_range(T.right,a,b)
    if a <= T.key and b >= T.key:
        c = c + 1
    return c

def bst_expected_height(n,M):
    A = [i for i in range(n)]
    sum = 0
    for _ in range(M):
        random.shuffle(A)
        T = None
        for a in A:
            T = bst_insert(T,a)
        sum += bst_height(T)
    return sum/M

