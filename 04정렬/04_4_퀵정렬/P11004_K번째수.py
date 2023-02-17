def quickSort(arr:list, left:int, right:int):
    if left >= right: return

    mid = partition(arr, left, right)
    quickSort(arr, left, mid-1)
    quickSort(arr, mid, right)

def partition(arr:list, left:int, right:int) -> int:
    pivot = arr[int((left+right)/2)]

    while left<=right:
        while pivot > arr[left]: left+=1
        while pivot < arr[right]: right-=1
        if left<=right:
            swap(arr, left, right)
            left+=1
            right-=1
    
    return left

def swap(arr:list, left:int, right:int):
    tmp = arr[left]
    arr[left] = arr[right]
    arr[right] = tmp


import sys
input = sys.stdin.readline

N, K = map(int, input().split())

arr = list(map(int, input().split()))

#quick sort(O(n^2))
quickSort(arr, 0, N-1)

#arr.sort()

print(arr[K-1])
