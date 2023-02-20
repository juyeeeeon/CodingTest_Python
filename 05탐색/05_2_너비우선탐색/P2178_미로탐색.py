from collections import deque
import sys
input = sys.stdin.readline
#output = sys.stdout.write

def BFS(i:int, j:int):
    queue = deque()
    queue.append((i, j))
    visited[i][j] = True

    while queue:
        now = queue.popleft()

        for k in range(4):
            x = now[0] + dx[k]
            y = now[1] + dy[k]
            if x>=0 and y>=0 and x<N and y<M:
                if arr[x][y] != 0 and not visited[x][y]:
                    visited[x][y]=True
                    arr[x][y] = arr[now[0]][now[1]] + 1
                    queue.append((x,y))
            




dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]



N, M = map(int, input().split())

arr = []

for i in range(N):
    arr.append(list(map(int, input().rstrip())))

visited = [[False]*M for _ in range(N)]
BFS(0, 0)

print(arr[N-1][M-1])
