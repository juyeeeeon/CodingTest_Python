import heapq
import sys
input = sys.stdin.readline
print = sys.stdout.write

N = int(input().rstrip())
#힙을 만들려면, []로 초기화된 리스트를 사용하거나, 
#함수 heapify()를 통해 값이 들어 있는 리스트를 힙으로 변환 할 수 있다.
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
