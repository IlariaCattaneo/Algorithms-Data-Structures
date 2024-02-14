def Algo_Y(A, r, c):
  for i in range(0,r*c):
    for j in range(i+1,r*c):
      if A[i] == A[j]:
        a = (i - 1)//c #integer division
        b = (j - 1)//c #integer division
        if a == b or a == b-1:
          if i - a*c == j - b*c or i - a*c == j - b*c + 1 or i - a*c == j - b*c - 1:
            return True
  return False
    
# Explain what  Algo-Y  does
# The algorithm checks if there are two elements in the same row or column that are equal.
# If there are, it returns True, otherwise it returns False.
# The worst case time complexity is O(n^2) because there are two nested for loops.
# The best case time complexity is O(1) because the algorithm will return False if there are no 
# equal elements in the same row or column.

def better_Algo_Y(A, r, c):
    i = 0
    j = i + 1
    while i < r*c and j < r*c:
        if A[i] == A[j]:
            a = (i - 1)//c
            b = (j - 1)//c
            if a == b or a == b-1:
                if i - a*c == j - b*c or i - a*c == j - b*c + 1 or i - a*c == j - b*c - 1:
                    return True
        i += 1
        j += 1
    return False