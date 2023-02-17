import sys
input = sys.stdin.readline

def mergeSort(arr:list, left:int, right:int):
    global buff, ans
    if left < right:
        center = int(left + (right - left)/2)

        mergeSort(arr, left, center)
        mergeSort(arr, center+1, right)

        for i in range(left, right+1):
            buff[i] = arr[i]

        k = left
        idx1 = left
        idx2 = center+1

        while idx1<=center and idx2<=right:
            if buff[idx1] > buff[idx2]:
                arr[k] = buff[idx2]
                ans += idx2-k
                k+=1
                idx2+=1
            else:
                arr[k] = buff[idx1]
                k+=1
                idx1+=1
        
        while idx1<=center:
            arr[k] = buff[idx1]
            k+=1
            idx1+=1
        while idx2<=right:
            arr[k] = buff[idx2]
            k+=1
            idx2+=1

N = int(input())
arr = list(map(int, input().split()))
buff = [0]*N
ans = 0
mergeSort(arr, 0, N-1)

print(ans)
