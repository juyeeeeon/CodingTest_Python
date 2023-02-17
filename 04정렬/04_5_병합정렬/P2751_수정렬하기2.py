import sys
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))

buff = [0]*N

""" 이것보다 아래것이 더 이해하기 쉬움
def mergeSort(arr:list, N:int):
    global buff
    __mergeSort(arr, 0, N-1)
    buff = None

def __mergeSort(arr:list, left:int, right:int):
    global buff

    if left < right:
        center = int((left+right)/2)
        p = 0
        j = 0
        k = left

        __mergeSort(arr, left, center)
        __mergeSort(arr, center+1, right)

        for i in range(left, center+1):
            buff[p] = arr[i]
            p+=1
        #파이썬은 for문이 끝나면 i값은 center+1이 아니라 center가 되버림
        i+=1 

        while i<=right and j<p:
            if buff[j] <= arr[i]:
                arr[k] = buff[j]
                k+=1
                j+=1
            else:
                arr[k] = arr[i]
                k+=1
                i+=1
        
        while j<p:
            arr[k] = buff[j]
            k+=1
            j+=1
"""
def mergeSort(arr:list, left:int, right:int):
    global buff

    if left < right:
        center = int(left + (right-left)/2)
        
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

#merge sort(nlgn)
mergeSort(arr, 0, N-1)

#arr.sort()
for i in arr:
    print(str(i))