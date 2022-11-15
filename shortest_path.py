import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

# number of nodes: n, number of routes: m
n, m = map(int, input().split())
start = int(input())
graph = [[] for i in range(n+1)]
visited = [False] * (n+1)
distance = [INF] * (n+1)

for i in range(m):
    # costs 'c' moving from 'a' to 'b'
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

'''
#Among the not visited nodes, return the smallest value
def shortest():
    minimum = INF
    #가장 최단 거리가 짧은 인덱스(노드)
    idx = 0
    for i in range(1, n+1):
        if distance[i] < minimum and not visited[i]:
            minimum = distance[i]
            idx = i
    return idx

def dijkstra(start):
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]
    for i in range(n-1):
        now = shortest()
        visited[now] = True
        for j in graph[now]:
            cost = distance[now] + d[j]
            if cost < distance[j[0]]:
                distance[j[0]] = cost

dijkstra(start)
for i in range(1, n+1):
    if distance[i] == INF:
        print('INFINITY')
    else:
        print(distance[i])
'''
def ijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

ijkstra(start)
for i in range(1, n+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])
