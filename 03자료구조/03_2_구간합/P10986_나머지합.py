import sys
input = sys.stdin.readline
N, M = map(int, input().split())

arr = list(map(int, input().split()))

#구간의 합
sumArr = [0]*N 
sumArr[0] = arr[0]
for i in range(1,N):
    sumArr[i] = sumArr[i-1] + arr[i]

answer = 0

#나머지가 0, 1, ..., M-1의 갯수를 담는 리스트
countArr = [0]*M
for i in range(N):
    remainder = sumArr[i]%M
    if remainder == 0:
        answer+=1
    countArr[remainder]+=1

for i in range(M):
    #나머지가 같은 부분합의 갯수가 2이상이면 
    if countArr[i]>=2:
        #두 부분합의 차는 나머지가 0이 되므로
        #전체 갯수 중에 2개를 뽑는 경우의 수
        answer += countArr[i]*(countArr[i]-1)/2

print(int(answer))