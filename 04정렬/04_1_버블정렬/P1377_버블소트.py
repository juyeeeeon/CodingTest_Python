"""
def swap(a:int, b:int):
    global arr
    tmp = arr[a]
    arr[a] = arr[b]
    arr[b] = tmp
"""

import sys
input = sys.stdin.readline
write = sys.stdout.write

N = int(input())
"""
arr = []


for i in range(N):
    arr.append(int(input()))


#bubble sort(O(n^2)) 시간초과
for i in range(N):
    changed = False
    for j in range(1, N-i):
        if arr[j-1] > arr[j]:
            changed = True
            swap(j-1, j)
    
    if changed == False:
        print(i+1)
        break
"""

# 버블소트로 원래 위치까지 가려면
# 원래 위치가 더 뒤쪽이면 한 번만에 갈 수 있지만
# 원래 위치가 더 앞쪽이면 떨어진 거리만큼을 반복해함을 이용
arr = []
for i in range(N):
    arr.append( (int(input()), i) ) #(입력값, 입력 당시의 idx)

arr.sort()
max = 0
for i in range(N):
    #입력 당시의 idx - 정렬 후 idx의 차가 가장 큰 것을 출력
    if (arr[i][1] - i) > max:
        max = arr[i][1] - i

print(max+1) #문제에서 1부터 시작하므로 +1
