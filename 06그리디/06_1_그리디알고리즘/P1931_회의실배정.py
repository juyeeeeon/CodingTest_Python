import sys
input = sys.stdin.readline
#print = sys.stdout.write

N = int(input())

arr = [[0, 0] for _ in range(N)]

for i in range(N):
    s, e = map(int, input().split())
    # 종료시간 우선 정렬이 우선이기 때문에 0번째에 종료시간을 먼저 저장.
    arr[i][0] = e
    arr[i][1] = s

arr.sort()

count = 1
prevEnd = arr[0][0]

for i in range(1, N):
    if arr[i][1] >= prevEnd:
        prevEnd = arr[i][0]
        count += 1

print(count)
