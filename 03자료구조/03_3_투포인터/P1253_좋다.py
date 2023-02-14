import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
arr.sort()

cnt = 0

for i in range(N):
    find = arr[i]
    startIdx = 0
    endIdx = N-1

    while startIdx < endIdx:
        sum = arr[startIdx] + arr[endIdx]

        if sum == find:
            if startIdx != i and endIdx != i:
                cnt += 1
                break
            elif startIdx == i:
                startIdx += 1
            elif endIdx == i:
                endIdx -= 1
                
        elif sum < find:
            startIdx+=1
        else:
            endIdx-=1

print(cnt)
