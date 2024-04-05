S = [None]*100
top_of_stack = 0

def push(x):
    global S, top_of_stack
    assert top_of_stack < len(S), "Stack overflow"
    S[top_of_stack] = x
    top_of_stack += 1

def pop():
    global S, top_of_stack
    assert top_of_stack > 0, "Stack underflow"
    top_of_stack -= 1
    return S[top_of_stack]

def is_empty():
    global top_of_stack
    return top_of_stack == 0
    
