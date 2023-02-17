import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

#insertion sort(O(n^2))
for i in range(1,N):
    tmp = arr[i]
    prev = i-1
    while (prev>=0) and tmp < arr[prev]:
        arr[prev+1] = arr[prev]
        prev-=1
    arr[prev+1] = tmp

#arr.sort()

#합배열 만들기
sum = [arr[0]]
for i in range(1, len(arr)):
    sum.append(sum[-1]+arr[i])

#합배열 총합 구하기
ans = 0
for i in sum:
    ans += i

print(ans)
