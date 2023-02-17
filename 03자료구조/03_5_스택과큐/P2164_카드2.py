from collections import deque
import sys

input = sys.stdin.readline
N = int(input().rstrip())

myDeque = deque()
for i in range(1, N+1):
    myDeque.append(i)

while len(myDeque) > 1:
    myDeque.popleft()
    myDeque.append(myDeque.popleft())


print(myDeque.pop())

