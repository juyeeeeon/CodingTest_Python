import sys
input = sys.stdin.readline
#print = sys.stdout.write

def binarySearch(minSize:int, maxSize:int)->int:
    while minSize <= maxSize:
        size = int((minSize + maxSize)/2)
        sum = 0
        brNum = 0
        
        for i in range(N):
            if sum + arr[i] > size:
                brNum+=1
                sum=0
            
            sum += arr[i]


        if sum != 0:
            brNum+=1
        if brNum > M:
            minSize = size + 1
        else:
            maxSize = size - 1
    
    return minSize



N, M = map(int, input().split()) # N:강의 수, M:블루레이 수
arr = list(map(int, input().split()))

minSize = max(arr)
maxSize = sum(arr)

print(binarySearch(minSize, maxSize))
