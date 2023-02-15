import heapq
import sys
input = sys.stdin.readline
print = sys.stdout.write

N = int(input().rstrip())
heap = []

for i in range(N):
    request = int(input().rstrip())
    if request != 0:
        heapq.heappush(heap, (abs(request), request))
    else:
        if not heap:
            print("0\n")
        else:
            print(str(heapq.heappop(heap)[1])+'\n')
