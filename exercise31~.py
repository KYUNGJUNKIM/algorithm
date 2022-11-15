'''
#31
t = int(input())
for case in range(t):
    n, m = map(int, input().split())
    array = list(map(int, input().split()))

    cage = []
    idx = 0
    for i in range(n):
        cage.append(array[idx:idx+m])
        idx += m
    
    for j in range(1, m):
        for i in range(n):
            if i == 0:
                left_up = 0
            else:
                left_up = cage[i-1][j-1]
            if i == n-1:
                left_down = 0
            else:
                left_down = cage[i+1][j-1]
            left = cage[i][j-1]
            cage[i][j] = cage[i][j] + max(left_down, left_up, left)
    result = 0
    for i in range(n):
        result = max(cage[i][m-1], result)
    print(result)
'''
'''
#32
n = int(input())
data = []
for i in range(n):
    data.append(list(map(int, input().split())))
for i in range(1, n):
    for j in range(i+1):
        if j == 0:
            up_left = 0
        else:
            up_left = data[i-1][j-1]
        if j == i:
            up = 0
        else:
            up = data[i-1][j]
        data[i][j] = data[i][j] + max(up_left, up)
print(max(data[n-1]))
'''
'''
#33
n = int(input())
t = []
reward = []
data = [0] * (n+1)
maximum = 0

for i in range(n):
    x, y = map(int, input().split())
    t.append(x)
    reward.append(y)
for i in range(n-1, 1, -1):
    time = t[i] + i
    if time <= n:
        data[i] = max(data[time]+reward[i], maximum)
        maximum = data[i]
    else:
        data[i] = maximum
print(maximum)
'''
'''
#34
n = int(input())
array = list(map(int, input().split()))
array.reverse()

data = [1] * n
for i in range(1, n):
    for j in range(0, i):
        if array[j] < array[i]:
            data[i] = max(data[i], data[j]+1)
print(n-max(data))
'''
'''
#35
n = int(input())
ugly = [0] * n
ugly[0] = 1

m2 = m3 = m5 = 0
curr2, curr3, curr5 = 2, 3, 5

for i in range(1, n):
    ugly[i] = min(curr2, curr3, curr5)
    if ugly[i] == curr2:
        m2 += 1
        curr2 = ugly[m2] * 2
    if ugly[i] == curr3:
        m3 += 1
        curr3 = ugly[m3] * 3
    if ugly[i] == curr5:
        m5 += 1
        curr5 = ugly[m5] * 5
print(ugly[n-1])
'''
'''
#36
a = input()
a_list = []
for i in range(len(a)):
    a_list.append(a[i])
b = input()
b_list = []
for i in range(len(b)):
    b_list.append(b[i])

cnt = 0
if len(a) == len(b):
    for i in range(len(a)):
        if a[i] != b[i]:
            cnt += 1
elif len(a) < len(b):
    for i in a_list:
        if i in b_list:
            b_list.remove(i)        
    cnt += len(b_list)
else:
    for i in b_list:
        if i in a_list:
            a_list.remove(i)
    cnt += len(a_list)

print(cnt)

#sol2)
def edit(str1, str2):
    n, m = len(str1), len(str2)
    dp = [[0]*(m+1) for i in range(n+1)]
    for i in range(1, n+1):
        dp[i][0] = 0
    for j in range(1, m+1):
        dp[0][j] = 0

    for i in range(1, n+1):
        for j in range(1, m+1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])
    return dp[n][m]
'''
'''
#37
n = int(input())
m = int(input())
INF = int(1e9)
graph = [[INF] * (n+1) for i in range(n+1)]

for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

for i in range(m):
    a, b, cost = map(int, input().split())
    if cost < graph[a][b]:
        graph[a][b] = cost

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] == INF:
            print(0, end=' ')
        else:
            print(graph[a][b], end=' ')    
    print()
'''
'''
#38
n, m = map(int, input().split())
INF = int(1e9)
graph= [[INF] * (n+1) for i in range(n+1)]

for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

result = 0
for a in range(1, n+1):
    cnt = 0
    for b in range(1, n+1):
        if graph[a][b] != INF or graph[b][a] != INF:
            cnt += 1
    if cnt == n:
        result += 1
print(result)
'''
'''
#39
import heapq
import sys
inout = sys.stdin.readline
INF = int(1e9)

dx = [-1, 0 ,1, 0]
dy = [0, -1, 0, 1]

for case in range(int(input())):
    n = int(input())
graph =[]
for i in range(n):
    graph.append(list(map(int, input().split())))
distance = [[INF] * n for i in range(n)]

x, y = 0, 0
q = [(graph[x][y], x, y)]
distance[x][y] = graph[x][y]

while q:
    dist, x, y = heapq.heappop(q)
    if distance[x][y] < dist:
        continue
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx<0 or nx>=n or ny<0 or ny>=0:
            continue
        cost = dist + graph[nx][ny]
        if cost < distance[nx][ny]:
            distance[nx][ny] = cost
            heapq.heappush(q, (cost, nx, ny))

print(distance[n-1][n-1])
'''

#40
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = 1
graph = [[] for i in range(n+1)]
distance = [INF] * (n+1)

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append((b, 1))
    graph[b].append((a, 1))

def dijkstra(start):
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

dijkstra(start)

max_node = 0
max_distance = 0
result = []
for i in range(1, n+1):
    if max_distance < distance[i]:
        max_node = i
        max_distance = distance[i]
        result = [max_node]
    elif max_distance == distance[i]:
        result.append(i)
print(max_node, max_distance, len(result))