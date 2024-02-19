def like_or_dislike(A):
    likec = 0
    dislikec = 0
    for i in range(len(A)):
        if len(A) == 1:
            return A[i]
        if A[i] == 'like':
            likec += 1
        elif A[i] == 'dislike':
            dislikec += 1
 
    
    if likec > dislikec:
        return 'like'
    elif dislikec > likec:
        return 'dislike'
    else:
        return 'undecided'

    