import sys
input = sys.stdin.readline

def binarySearch(arr:list, k:int, left:int, right:int)->int:
    while left <= right:
        pivot = int((left+right)/2)
        if arr[pivot] > k:
            right = pivot-1
        elif arr[pivot] < k:
            left = pivot+1
        elif arr[pivot] == k:
            return 1
    return 0

N = int(input())
arrN = list(map(int, input().split()))
M = int(input())
arrM = list(map(int, input().split()))

arrN.sort()

for key in arrM:
    print(binarySearch(arrN, key, 0, N-1))