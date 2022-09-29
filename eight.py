# fisrt
# N = int(input("Enter N: "))
# array=[[int(input()) for i in range(N)] for k in range(N)]
# sum = 0
# count = 0
# for i in range(N):
#     for k in range(N):
#         if k>=i:
#             sum+= array[i][k]
#             count+=1
# print("Sum: ", sum)
# print("Count: ", count)


# 2)

# N = int(input("Enter N: "))
# M = int(input("Enter M: "))
# array=[[int(input()) for i in range(N)] for k in range(M)]
# min = float('inf')
# max = float('-inf')
# tempimin=0
# tempkmin=0
# tempimax=0
# tempkmax=0
# for i in range(0,N):
#     for k in range(0,N):
#         if min>array[i][k]:
#             min = array[i][k]
#             tempimin = i
#             tempkmin = i
#         if max<array[i][k]:
#             max = array[i][k]
#             tempimax =i
#             tempimin =i
# temp = array[0][0]
# array[0][0] = min
# array[tempimin][tempkmin] = temp
# temp = array[N-1][M-1]
# array[N-1][M-1] = max
# array[tempimax][tempkmax] = temp
# print(array)

# Second

# 1)

# N = int(input("Enter N: "))
# array=[[int(input()) for i in range(N)] for k in range(N)]
# arr=[]
# arr2 = []
# temp = False
# for i in range(N):
#     arr.append(0)
#     arr2.append(0)
# for i in range(0,N):
#     for k in range(0,N):
#         arr[i]+=array[i][k]
# for i in range(0,N):
#     for k in range(0,N):
#         arr2[i]+=array[i][i]
# for i in range(0,N):
#     for k in range(0,N):
#         if arr[i]!=arr[k] or arr2[i]!=arr2[k] or arr[i] !=arr2[k]:
#             print("Not magic")
#             temp = True
#             break
# if temp==False:
#     print("This is magic")

# 2)

# N = int(input("Enter N: "))
# array=[[int(input()) for i in range(N)] for k in range(N)]
# temp = 0
# for i in range(0,N):
#     temp = array[0][i]
#     array[0][i] = array[N-1][i]
#     array[N-1][i] = temp
# for i in range(0,N):
#     for k in range(0,N):
#         print(array[i][k] , end=" ")
#     print("")

# Third
# 1)
# N = int(input("Enter N: "))
# array=[[int(input()) for i in range(N)] for k in range(N)]
# def transpose(mat, tr, N):
#     for i in range(N):
#         for j in range(N):
#             tr[i][j] = mat[j][i]
#
#
# def isSymmetric(mat, N):
#     tr = [[0 for j in range(len(mat[0]))] for i in range(len(mat))]
#     transpose(mat, tr, N)
#     for i in range(N):
#         for j in range(N):
#             if (mat[i][j] != tr[i][j]):
#                 return False
#     return True
#
#
# if (isSymmetric(array, 3)):
#     print("Yes")
# else:
#     print("No")

# 2)

# N = int(input("Enter N: "))
# M = int(input("Enter M: "))
# array=[[int(input()) for i in range(N)] for k in range(M)]
# max = float('-inf')
# tempimax=0
# tempkmax=0
# for i in range(0,M):
#     for k in range(0,N):
#         if max<array[i][k]:
#             max = array[i][k]
#             tempimax =i
#             tempimin =i
# temp = array[0][0]
# array[0][0]=max
# array[tempimax][tempkmax] = temp
# for i in range(0,M):
#     for k in range(0,N):
#         print(array[i][k] , end=" ")
#     print("")

# Fourth

# N = int(input("Enter N: "))
# M = int(input("Enter M: "))
# array=[[int(input()) for i in range(N)] for k in range(M)]
# summin = float('inf')
# tempsum=0
# max=0
# min=0
# summax = float('-inf')
# for i in range(0,M):
#     for k in range(0,N):
#         tempsum += array[i][k]
#     if summin>tempsum:
#         summin = tempsum
#         min = i
#     if summax<tempsum:
#         summax = tempsum
#         max = i
#     tempsum = 0
# print("sum of min row: " , summin)
# for i in range(0,N):
#     print(array[min][i])
# print("sum of max row: " , summax)
# for i in range(0,N):
#     print(array[max][i])

# 2)
# N = int(input("Enter N: "))
# array=[[int(input()) for i in range(N)] for k in range(N)]
# for i in range(0,N-1):
#     for k in range(0,N):
#         if array[i][k]>0:
#             array[i][k]=1
#         elif array[i][k]<0:
#             array[i][k]=0
# for i in range(0,N):
#     for k in range(0,N):
#         print(array[i][k] , end=" ")
#     print("")

# fifth
# 1)

# N = int(input("Enter N: "))
# M = int(input("Enter M: "))
# array=[[int(input()) for i in range(N)] for k in range(M)]
# for i in range(0,M):
#     array[i].sort()
# array.sort()
# for i in range(0,M):
#     for k in range(0,N):
#         print(array[i][k] , end=" ")
#     print("")

# 2)

# N = int(input("Enter N: "))
# M = int(input("Enter M: "))
# array=[[int(input()) for i in range(N)] for k in range(M)]
# min = float('inf')
# temp = 0
# for i in range(0,M):
#     for k in range(0,N):
#         if min> array[i][k]:
#             min = array[i][k]
#             temp = k
#     if array[i][temp]%2 ==0:
#         array[i][temp]=0
#     else:
#         array[i][temp] =1
# for i in range(0,M):
#     for k in range(0,N):
#         print(array[i][k] , end=" ")
#     print("")

# sixth
# 1)
# N = int(input("Enter N: "))
# M = int(input("Enter M: "))
# array=[[int(input()) for i in range(N)] for k in range(M)]
# max = float('-inf')
# min = float('inf')
# temp = 0
# for i in range(0,M):
#     for k in range(0,N):
#         if max< array[i][k]:
#             max = array[i][k]
#             temp = k
#     print("The biggest number in row:" ,temp," is: " , max)
#     max = 0
# for i in range(0,M):
#     for k in range(0,N):
#         if min>array[i][i]:
#             min = array[i][i]
#     print("The biggest number in column:" ,i," is: " , min)
#     min = float('inf')

# 2)
# import random
#
# n = int(input("Enter n: "))
# b = [[random.randrange(10) for i in range(n)] for j in range(n)]
#
# for i in b:
#     for j in i:
#         print(j, end=" ")
#     print()
# print()
#
# for i in b:
#     print(i)
# print()
#
# a = sum(b, [])
# max1 = max(a[::n + 1])
# max2 = max(a[n - 1::n - 1][:n])
# if max1 > max2:
#     i1 = j1 = a[::n + 1].index(max1)
# else:
#     i1 = a[n - 1::n - 1][:n].index(max2)
#     j1 = n - 1 - i1
# b[n // 2][n // 2], b[i1][j1] = b[i1][j1], b[n // 2][n // 2]
#
# for i in b:
#     print(i)

# seventh
# matrix = [
#        [1, 2, 3],
#        [0, 6, 4],
#        [0, 0, 6]
#     ]
# correct = []
# for i in range(0,3):
#     for k in range(i,3):
#         correct.append(matrix[i][k])
# for i in range(0,len(correct)):
#     print(correct[i],end=" ")

# 2)
# N = int(input("Enter N: "))
# M = int(input("Enter M: "))
# array=[[int(input()) for i in range(N)] for k in range(M)]
# arr = []
# count = 0
# for i in range(0,M):
#     for k in range(0,N):
#         if i==k:
#             arr.append(array[i][k])
# for i in range(0,len(arr)):
#     count+=arr[i]
# for i in range(0,len(arr)):
#     if arr[i]%2 == 1:
#         arr[i] = arr[i]/count
#     print(arr[i],end="-")

# Eight
# 1)
# N = int(input("Enter N: "))
# M = int(input("Enter M: "))
# array=[[int(input()) for i in range(N)] for k in range(M)]
# K = int(input("Enter k: "))
# for i in range(0,M):
#     for k in range(0,N):
#         if i==k:
#             array[K][i] = array[i][i]
# for i in range(0,M):
#     for k in range(0,N):
#         print(array[i][k],end=" ")
#     print(" ")