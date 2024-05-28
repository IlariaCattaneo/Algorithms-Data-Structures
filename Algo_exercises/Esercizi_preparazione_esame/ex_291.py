def re_sort(A):
    # A is already sorted, then random 0s are inserted instead of numbers
    read1 = 0
    write1 = read1
    while read1 < len(A) and A[read1] <= 0:
        if A[read1] < 0:
            A[write1] = A[read1]
            write1 += 1
        read1 += 1
    read2 = len(A)
    write2 = read2
    while read2 > write1 and A[read2] > 0:
        if A[read2] > 0:
            A[write2] = A[read2]
            write2 -= 1
        read2 -= 1
    while write1 <= write2:
        A[write1] = 0
        write1 += 1
    return A