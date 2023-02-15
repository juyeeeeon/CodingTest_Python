from collections import deque
import sys
input = sys.stdin.readline

N, L = map(int, input().split())
#arr = [0] + list(map(int, input().split()))
arr = list(map(int, input().split()))

#0번째 idx가 que의 맨 앞
myDeque = deque()

for i in range(N):
    tmp = arr[i]
    while myDeque and myDeque[-1]>tmp:
        myDeque.pop()
    myDeque.append(tmp)

    #윈도우의 크기보다 커진 단계에서 arr와 비교한 후 popleft
    if i>=L and myDeque[0]==arr[i-L]:
        myDeque.popleft()
    
    print(myDeque[0], end=' ')

""" 시간초과
startIdx = 1-L+1
if startIdx<=0: startIdx = 1
endIdx = 1

minVal = min(arr[startIdx:endIdx+1])
print(minVal,end=' ')

for i in range(2, len(arr)):
    startIdx = i-L+1
    if startIdx<=0: startIdx = 1
    endIdx = i

    if arr[endIdx]<=minVal : minVal = arr[endIdx]
    if arr[startIdx-1] == minVal : minVal = min(arr[startIdx:endIdx+1])

    print(minVal, end=' ')

"""