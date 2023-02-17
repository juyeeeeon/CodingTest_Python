import sys
input = sys.stdin.readline
print = sys.stdout.write
"""
def radixSort(arr:list, maxSize:int):
    output = [0]*len(arr)
    jarisu = 1
    count = 0

    while count != maxSize:
        bucket = [0]*10 #0~9
        for i in range(len(arr)):
            bucket[int((arr[i]/jarisu)%10)]+=1 #자릿수의 개수

        for i in range(1,10): #합배열 만들기
            bucket[i] += bucket[i-1]
        
        for i in range(len(arr)-1, -1, -1):
            output[bucket[int((arr[i]/jarisu)%10)] - 1] = arr[i]
            bucket[int((arr[i]/jarisu)%10)]-=1

        for i in range(len(arr)):
            arr[i] = output[i]

        jarisu*=10
        count+=1

"""

N = int(input())

""" arr에 담을 때 시간초과 발생 -> arr에 담지 않고 푸는 방법을 생각해야 함
arr = [0]*N

for i in range(N):
    arr[i] = int(input())

radixSort(arr, 5)
"""

count = [0]*10001
for _ in range(N):
    count[int(input())]+=1

for i in range(len(count)):
    while count[i] != 0:
        print(str(i)+'\n')
        count[i]-=1
