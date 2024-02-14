# prints ciao 20 times
# for i in range(20):
   # print('ciao')

# prints ciao and the index 20 times
# for i in range(20):
   # print('ciao', i)

# prints i love ice cream
# for i in ['vanilla', 'chocolate', 'strawberry']:
   # print('I love', i, 'ice cream!')

# prints ciao and the index 20 times as long as i < 20 and increases i at the end of each cycle
# i = 0
# while i < 20:
   # print('ciao', i)
   # i = i + 1

# n = int(input('choose an integer n > 0: '))
# while n != 1:
   # print(n)
   # if n % 2 == 0:
       # n = n // 2
   # else:
       # n = 3*n + 1

# n = int(input('choose an integer n > 1: '))
# for i in range(2,n):
   # if n % i == 0:
      #  print('composite')
      #  break


n = int(input('choose an integer n > 1: '))
C = [False]*(n)
for i in range(2,n):
   if C[i]:
      continue
   for j in range(i*i,n,1):
      C[j] = True
   print(i)



   