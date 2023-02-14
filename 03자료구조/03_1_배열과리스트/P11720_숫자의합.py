import sys
input = sys.stdin.readline

n = input()
arr = list(map(int, input().strip()))
result = 0
for i in arr:
    result += i

print(result)