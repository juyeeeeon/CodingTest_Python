import sys
input = sys.stdin.readline
print = sys.stdout.write

def DFS(node:int, depth:int):
    global arrive
    if depth == 5 or arrive == True:
        arrive = True
        return

    visited[node] = True

    for i in arr[node]:
        if not visited[i]:
            DFS(i, depth+1)
    
    visited[node] = False #잘못 들어간 길을 다시 false로 바꿔야 하므로 

N, M = map(int, input().split())

arr = [[] for _ in range(N)]
arrive = False
visited = [False]*N

for i in range(M):
    s, e = map(int, input().split())
    arr[s].append(e)
    arr[e].append(s)

for i in range(N):
    DFS(i, 1)
    if arrive: 
        break

if arrive:
    print(str(1)+'\n')
else:
    print(str(0)+'\n')
