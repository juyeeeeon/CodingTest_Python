import sys
import math
input = sys.stdin.readline

s, e = map(int, input().split())
count = 0
newE = int(math.sqrt(e)+1)

arr = [0 for _ in range(newE)]

for i in range(2, newE):
    arr[i] = i

for i in range(2, int(math.sqrt(newE)+1)):
    if arr[i] == 0:
        continue
    
    for j in range(i+i, newE, i):
        arr[j] = 0

for i in range(len(arr)):
    if arr[i] != 0:
        tmp = arr[i]

        while tmp <= e/arr[i]:
            if tmp >= s/arr[i]:
                count += 1
            
            tmp *= arr[i]
"""
# 내가 푼 방식

primes = []
for i in arr:
    if i != 0:
        primes.append(i)

for prime in primes:
    i = 2
    while True:
        tmp = prime**i
        if tmp < s:
            i+=1
            continue
        
        elif tmp >= s and tmp <= e:
            count += 1
            i+=1

        else:
            break
"""

print(count)