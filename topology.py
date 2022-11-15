from collections import deque

n, e = map(int, input().split())
degree = [0] * (n+1)
graph = [[] for i in range(n+1)]

for i in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    degree[b] += 1
'''
def topology():
    result = []
    q = deque()
    for i in range(1, n+1):
        if degree[i] == 0:
            q.append(i)
    while q:
        now = q.popleft()
        result.append(now)
        for i in graph[now]:
            degree -= 1
            if degree[i] == 0:
                q.append(i)
    for i in result:
        print(i, end=' ')

topology()
'''
print(graph)
print(degree)
