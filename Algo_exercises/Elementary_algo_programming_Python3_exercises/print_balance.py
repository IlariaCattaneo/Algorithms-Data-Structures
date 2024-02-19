def print_balance(b):
    if b > 0:
        print('gain:', b)
    elif b < 0:
        print('loss:', -b)
    else:
        print('zero')