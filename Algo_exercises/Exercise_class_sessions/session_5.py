def closest_pair(A, B, n):
    assert len(A) == len(B)
    sorted(A)
    sorted(B)
    min = abs(A[0] + B[0] - n)
    min_pair = (A[0], B[0])
    for element in A:
        for element2 in B:
            if abs(element + element2 - n) < min:
                min = abs(element + element2 - n)
                min_pair = (element, element2)
    return min_pair

def largest_subarray_sum(A):
    previous = 0
    max = 0
    for number in A:
        if previous + number > previous:
            previous += number
        else:
            previous = number
        if previous > max:
            max = previous
    return max

def merge_intervals(intervals):
    sorted(intervals)
    if len(intervals) == 0:
        return []
    merged = []
    for i in range(len(intervals)-1):
        if intervals[i][1] >= intervals[i+1][0]:
            merged.append([intervals[i][0], intervals[i+1][1]])
        else:
            merged.append(intervals[i])
    return merged
# MANCA IL CASO IN CUI UN INTERVALLO È COMPLETAMENTE INNESTATO IN UN ALTRO
# RIGUARDARE ANCHE COME È SCRITTO IL CODICE PERCHÉ NON È CORRETTO

def two_sum(A, t):
    # A is sorted, B is sorted
    B = []
    for element in A:
        B.append(element)
    i = 0
    j = len(B) - 1
    while i < len(A) and j >= 0:
        if A[i] + B[j] < t:
            i += 1
        elif A[i] + B[j] > t:
            j -= 1
        else:
            return True
    return False