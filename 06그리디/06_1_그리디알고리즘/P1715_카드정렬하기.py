#PriorityQueue로 풀면 시간초과
#PriorityQueue는 스레드 안전 클래스이고 heapq는 스레드 안전을 보장하지 않는다.
#PriorityQueue는 스레드 안전을 위한 lock을 제공하기 때문에 잠금 오버 헤드가 있어 시간초과 발생

import heapq
import sys
input = sys.stdin.readline
print = sys.stdout.write

N = int(input())
queue = []
for _ in range(N):
    heapq.heappush(queue, int(input()))

sum = 0

while len(queue) > 1:
    tmp1 = heapq.heappop(queue)
    tmp2 = heapq.heappop(queue)

    sum += tmp1 + tmp2
    heapq.heappush(queue, tmp1 + tmp2)

print(str(sum))