import heapq
import sys
input = sys.stdin.readline
#print = sys.stdout.write

N = int(input())

arr = []
for _ in range(N):
    arr.append(int(input()))


sum = 0

while len(arr) > 1:
    heapq._heapify_max(arr)

    tmp1 = heapq.heappop(arr)
    heapq._heapify_max(arr)
    tmp2 = heapq.heappop(arr)
    heapq._heapify_max(arr)

    if tmp1 > 1:
        if tmp2 > 1:
            sum += tmp1 * tmp2
        elif tmp2 == 1:
            sum += tmp1
            sum += tmp2
        else:
            heapq.heappush(arr, tmp2)
            heapq._heapify_max(arr)
    
    elif tmp1 == 1:
        if tmp2 == 0:
            sum += tmp1
            heapq.heappush(arr, tmp2)
            heapq._heapify_max(arr)
        elif tmp2 < 0:
            sum += tmp1
            heapq.heappush(arr, tmp2)
            break


    elif tmp1 == 0:
        heapq.heappush(arr, tmp2)
        heapq.heappop(arr)
        heapq._heapify_max(arr)
        

    elif tmp1 < 0:
        break

    """
    if arr[0] == 0:
        tmp1 = heapq.heappop(arr)
        heapq._heapify_max(arr)
        tmp2 = heapq.heappop(arr)

        sum += tmp1*tmp2

    elif arr[0] < 0:
        break

    elif arr[0]>0 :
        if arr[1] <= 0:
            sum += heapq.heappop(arr)
        else:
            tmp1 = heapq.heappop(arr)

            heapq._heapify_max(arr)
            tmp2 = heapq.heappop(arr)

            sum += tmp1*tmp2
    """
for i in arr:
    sum += i

print(sum)