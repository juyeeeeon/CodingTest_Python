import sys
input = sys.stdin.readline
print = sys.stdout.write

def DFS(node:int):
    visited[node] = True

    for new_node in arr[node]:
        if not visited[new_node]:
            DFS(new_node)


N, M = map(int, input().split())

visited = [False]*(N+1)
arr = [[] for _ in range(N+1)]

for i in range(M):
    s, e = map(int, input().split())
    arr[s].append(e)
    arr[e].append(s)

count = 0

for i in range(1, N+1):
    if not visited[i]:
        count+=1
        DFS(i)

print(str(count))