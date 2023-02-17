import sys
input = sys.stdin.readline

N = int(input().rstrip())
A = list(map(int, input().split()))

myStack = [] #값이 아닌 idx를 저장
ans = [-1]*N #[idx]에 해당하는 오큰수 저장

for i in range(N): # i는 idx
    while myStack and A[myStack[-1]]<A[i]:
        ans[myStack.pop()] = A[i]
        

    myStack.append(i)

for i in range(N):
    print(ans[i], end=' ')