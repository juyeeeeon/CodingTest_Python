def swap(a:int, b:int):
    global arr
    tmp = arr[a]
    arr[a] = arr[b]
    arr[b] = tmp


import sys
input = sys.stdin.readline
print = sys.stdout.write

N = int(input())
arr = []

for i in range(N):
    arr.append(int(input()))

#bubble sort(O(n^2))
for i in range(N):
    for j in range(1, N-i):
        if arr[j-1] > arr[j]:
            swap(j-1, j)


#arr.sort() #O(nlg(n))

for i in range(N):
    print(str(arr[i])+'\n')