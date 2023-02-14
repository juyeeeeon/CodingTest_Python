import sys
input = sys.stdin.readline

N = int(input().rstrip())

count = 1 # N
startIdx = 1
endIdx = 1
sum = 1

while endIdx != N:
    if sum == N:
        count += 1
        endIdx += 1
        sum += endIdx
    elif sum > N:
        sum -= startIdx
        startIdx += 1
    else:
        endIdx += 1
        sum += endIdx

print(count)