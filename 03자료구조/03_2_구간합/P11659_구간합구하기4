import sys
# input()보다 sys.stdin.readline()이 더 빠르고 메모리도 적게 소모
# 매번 sys.stdin.readline()을 적는 것보다
#  input = sys.stdin.readline 으로 정의한 후 input()을 사용하는 것이 더 편함
input = sys.stdin.readline
N, M = map(int, input().split())
arr = list(map(int, input().split()))

#시간초과
"""
for i in range(M):
    S, E = map(int, sys.stdin.readline().split())
    print(sum(arr[S-1:E])) #여기서 sum()과 arr[:]에서 시간이 오래 걸림 -> 합배열 사용

"""
prifix_sum = [0]
tmp = 0
for i in arr:
    tmp += i
    prifix_sum.append(tmp)

for i in range(M):
    s, e = map(int, input().split())
    print(prifix_sum[e] - prifix_sum[s-1])