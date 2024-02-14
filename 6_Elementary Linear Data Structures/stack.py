S = [None]*100                  # "data", fixed-size array where we
                                # store the elements of the stack
N = 0                           # "meta-data"

def push(x):
    # puts element x at the top of the stack, if space permits
    global S,N
    if N < len(S):
        S[N] = x
        N = N + 1
    else:
        print('stack overflow')

def pop():
    global S,N
    if N > 0:
        N = N - 1
        return S[N]
    else:
        print('stack underflow')

def is_empty():
    global S,N
    return N == 0
