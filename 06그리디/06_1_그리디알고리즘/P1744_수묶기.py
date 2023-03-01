import heapq
import sys
input = sys.stdin.readline
#print = sys.stdout.write

N = int(input())

p_queue = []
n_queue = []
one = 0
zero = 0

sum = 0

for _ in range(N):
    tmp = int(input())
    if tmp > 1:
        heapq.heappush(p_queue, tmp)
    elif tmp < 0:
        heapq.heappush(n_queue, tmp)
    elif tmp == 1:
        one+=1
    else:
        zero+=1

while len(p_queue) > 1:
    heapq._heapify_max(p_queue)
    tmp1 = heapq.heappop(p_queue)
    heapq._heapify_max(p_queue)
    tmp2 = heapq.heappop(p_queue)
    sum += tmp1 * tmp2

if len(p_queue) > 0:
    sum += heapq.heappop(p_queue)

while len(n_queue) > 1:
    tmp1 = heapq.heappop(n_queue)
    tmp2 = heapq.heappop(n_queue)
    sum += tmp1 * tmp2

if len(n_queue) > 0:
    if zero == 0:
        sum+= heapq.heappop(n_queue)

sum += one

print(sum)