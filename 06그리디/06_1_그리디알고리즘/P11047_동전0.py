import sys
input = sys.stdin.readline
#print = sys.stdout.write

N, K = map(int, input().split())

coins = []
for _ in range(N):
    coins.append(int(input()))

cnt = 0

for i in range(N-1, -1, -1):
    if K >= coins[i]:
        cnt+=int(K/coins[i])
        K%=coins[i]

print(cnt)