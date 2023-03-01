from collections import deque
import sys

input = sys.stdin.readline

arr = list(input().split('-'))

ans = 0

for i in range(len(arr)):
    tmp = arr[i].split('+')
    
    sum = 0
    for j in tmp:
        sum += int(j)
    
    if i==0:
        ans += sum
    else:
        ans -= sum

print(ans)

"""
내가 푼 방식식
arr = list(input().rstrip())

myqueue = deque()

num = 0
for i in arr:
    if i.isdecimal():
        num = num*10 + int(i)
    else:
        myqueue.append(num)
        num = 0
        myqueue.append(i)

myqueue.append(num)

ans = 0

minus = []
mFlag = False

while myqueue:
    tmp = myqueue.popleft()

    if tmp == '-':
        if mFlag:
            ans -= sum(minus)
            minus = []
        else:
            mFlag = True

    elif type(tmp) == int:
        if mFlag:
            minus.append(tmp)
        else:
            ans += tmp

ans -= sum(minus)

print(ans)
"""