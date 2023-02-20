from collections import deque
import sys
input = sys.stdin.readline
#print = sys.stdout.write

"""
 1. 트리에서 임의의 정점 x를 잡는다.
 2. 정점 x에서 가장 먼 정점 y를 찾는다.
 3. 정점 y에서 가장 먼 정점 z를 찾는다.
 트리의 지름은 정점 y와 정점 z를 연결하는 경로다.

 (?) x는 y와 z의 가운데에 있기 때문에 y와 z의 경로가 최대길이
"""

class Edge():
    def __init__(self, vertex:int, weight:int):
        self.vertex = vertex
        self.weight = weight

def BFS(v:int):
    queue = deque()
    queue.append(v)
    visited[v] = True

    while queue:
        now = queue.popleft()
        for edge in arr[now]:
            if not visited[edge.vertex]:
                visited[edge.vertex] = True
                queue.append(edge.vertex)
                distance[edge.vertex] = distance[now] + edge.weight


V = int(input())
arr = [[] for _ in range(V+1)]
visited = [False]*(V+1)
distance = [0]*(V+1)

for i in range(1,V+1):
    tmp = list(map(int, input().split()))
    for j in range(1,len(tmp), 2):
        if tmp[j] == -1: break
        arr[tmp[0]].append(Edge(tmp[j], tmp[j+1]))

BFS(1)

max = 1
for i in range(2, V+1):
    if distance[max] < distance[i]:
        max = i

visited = [False]*(V+1)
distance = [0]*(V+1)
BFS(max)

distance.sort()
print(distance[V])