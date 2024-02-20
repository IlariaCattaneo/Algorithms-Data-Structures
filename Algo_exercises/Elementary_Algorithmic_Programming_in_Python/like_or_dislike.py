def like_or_dislike(A):
    likec = 0
    for i in range(len(A)):
        if A[i] == "like":
            likec += 1

    if len(A) == 0:
        print('undecided')
    elif likec / len(A) > 0.5:
        print('like')
    elif likec / len(A) < 0.5:
        print('dislike')
    elif likec / len(A) == 0.5:
        print('undecided')

# ex 1
like_or_dislike(['like'])

# ex 2
like_or_dislike(['dislike','like','dislike'])

# ex 3
like_or_dislike(['like','dislike'])

# ex 4
like_or_dislike([])