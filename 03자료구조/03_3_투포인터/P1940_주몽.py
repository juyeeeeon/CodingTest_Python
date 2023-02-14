import sys
input = sys.stdin.readline
N = int(input().rstrip())
M = int(input().rstrip())
arr = list(map(int, input().split()))

ans = 0
""" 내가 푼 방식
startIdx = 0
endIdx = 1

for i in range(0,len(arr)-1):
    for j in range(i+1,len(arr)):
        sum = arr[i] + arr[j]
        if sum == M :
             ans+=1

print(ans)
"""

#다른 사람이 푼 방식
#더 빠름
startIdx = 0
endIdx = N-1
arr.sort()
while startIdx < endIdx :
    if arr[startIdx] + arr[endIdx] < M:
        startIdx += 1
    elif arr[startIdx] + arr[endIdx] > M:
        endIdx -= 1
    else:
        ans+=1
        startIdx += 1
        endIdx -= 1
print(ans)
