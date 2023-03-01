import sys
import math

input = sys.stdin.readline

s, e = map(int, input().split())

#소수구하기 -> 에라토스테네스의 체
arr = [0 for _ in range(e+1)]

for i in range(2, e+1):
    arr[i] = i

for i in range(2, int(math.sqrt(e)+1)):
    if arr[i] == 0:
        continue
    for j in range(i+i, e+1, i):
        arr[j] = 0

for i in range(s, e+1):
    if arr[i] != 0:
        print(i)