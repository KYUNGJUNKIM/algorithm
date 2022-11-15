from itertools import permutations
from itertools import combinations
from collections import deque

'''
def solution(n, weak, dist):
    length = len(weak)
    for i in range(length):
        weak.append(weak[i] + n)
    answer = len(dist) + 1
    for start in range(length):
        for friend in list(permutations(dist, len(dist))):
            cnt = 1
            position = weak[start] + friend[cnt-1]
            for idx in range(start, start+length):
                if position < weak[idx]:
                    cnt += 1
                    if cnt > len(dist):
                        break
                    position = weak[start] + friend[cnt-1]
            answer = min(answer, cnt)
    if answer > len(dist):
        return -1
    return answer

print(solution(12, [1,3,4,9,10], [3,5,7]))
'''
'''
def possible(answer):
    for x, y, stuff in answer:
        if stuff == 0:
            if y ==0 or [x, y-1, 0] in answer or [x-1, y, 1] in answer or [x, y, 1] in answer:
                continue
            return False
        elif stuff == 1:
            if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer or ([x-1, y, 1] in answer and [x+1, y, 1] in answer):
                continue
            return False
    return True

def solution(n, bulid_frame):
    answer = []
    for frame in bulid_frame:
        x, y, stuff, operate = frame
        if operate == 0:
            answer.remove([x, y, stuff])
            if not possible(answer):
                answer.append([x, y, stuff])
        if operate == 1:
            answer.append([x, y, stuff])
            if not possible(answer):
                answer.remove([x, y, stuff])
    return sorted(answer) 

print(solution(5, [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]))
'''
'''
n, m, k, x = map(int, input().split())
graph = [[] for i in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

distance = [-1] * (n+1)
distance[x] = 0

q = deque([x])
while q:
    now = q.popleft()
    for node in graph[now]:
        if distance[node] == -1:
            distance[node] = distance[now] + 1
            q.append(node)

check = False
for i in range(1, n+1):
    if distance[i] == k:
        print(i)
        check = True
if check == False:
    print(-1)
'''
'''
n, m = map(int, input().split())
data = []
graph = [[0] * m for i in range(n)]

for i in range(n):
    data.append(list(map(int, input().split())))

dx = [-1, 0 ,1, 0]
dy = [0, 1, 0, -1]

result = 0

def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if graph[nx][ny] == 0:
                graph[nx][ny] = 2
                virus(nx, ny)

def get_score():
    score = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                score += 1
    return score

def dfs(cnt):
    global result
    if cnt == 3:
        for i in range(n):
            for j in range(m):
                graph[i][j] = data[i][j]
        for i in range(n):
            for j in range(m):
                if graph[i][j] == 2:
                    virus(i, j)
        result = max(result, get_score())
        return
    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                data[i][j] = 1
                cnt += 1
                dfs(cnt)
                data[i][j] = 0
                cnt -= 1

dfs(0)
print(result)
'''
'''
n, k = map(int, input().split())
graph = []
data = []

for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] == 0:
            data.append((graph[i][j], 0, i, j))

data.sort()
q = deque(data)

target_s, target_x, target_y = map(int, input().split())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

while q:
    virus, s, x, y = q.popleft()
    if s == target_s:
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx and nx < n and 0 <= ny and ny < m:
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus
                q.append(virus, s+1, nx, ny)

print(graph[target_x - 1][target_y - 1])
'''
'''
def balance(p):
    cnt = 0
    for i in range(len(p)):
        if p[i] == '(':
            cnt += 1
        else:
            cnt -= 1
        if cnt == 0:
            return i

def check_proper(p):
    cnt = 0
    for i in p:
        if i == '(':
            cnt += 1
        else:
            if cnt == 0:
                return False
            cnt -= 1
    return True

def solution(p):
    answer = ''
    if p == '':
        return answer
    idx = balance(p)
    u = p[:idx+1]
    v = p[idx+1:]
    if check_proper(u):
        answer = u + solution(v)
    else:
        answer = '('
        answer += solution(v)
        answer += ')'
        u = list(u[1:-1])
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
        answer += "".join(u)
    return answer        

print(solution(")("))
'''
'''
n= int(input())
data = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

minimum = int(1e9)
maximum = int(-1e9)

def dfs(i, now):
    global minimum, maximum, add, sub, mul, div
    if i == n:
        minimum = min(minimum, now)
        maximum = max(maximum, now)
    else:
        if add > 0:
            add -= 1
            dfs(i+1, now+data[i])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(i+1, now-data[i])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(i+1, now*data[i])
            mul += 1
        if div > 0:
            div -= 1
            dfs(i+1, now/data[i])
            div += 1

dfs(1, data[0])
print(maximum, minimum)
'''
'''
n = int(input())
board = []
teachers = []
spaces = []

for i in range(n):
    board.append(list(input().split()))
    for j in range(n):
        if board[i][j] == "T":
            teachers.append((i, j))
        if board[i][j] == "X":
            spaces.append((i, j))

def screen(x, y, direction):
    if direction == 0:
        while y >= 0:
            if board[x][y] == "S":
                return True
            if board[x][y] == "O":
                return False
            y -= 1
    if direction == 1:
        while y < n:
            if board[x][y] == "S":
                return True
            if board[x][y] == "O":
                return False
            y += 1    
    if direction == 2:
        while x >= 0:
            if board[x][y] == "S":
                return True
            if board[x][y] == "O":
                return False
            x -= 1
    if direction == 3:
        while x < n:
            if board[x][y] == "S":
                return True
            if board[x][y] == "O":
                return False
            x += 1
    return False

def process():
    for x, y in teachers:
        for i in range(4):
            if screen(x, y, i):
                return True
    return False

find = False

for data in combinations(spaces, 3):
    for x, y in data:
        board[x][y] = "O"
    if not process():
        find = True
        break
    for x, y in data:
        board[x][y] = "X"

if find:
    print("YES")
else:
    print("NO")
'''

n, l, r = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
result = 0

def process(x, y, idx):
    country = []
    country.append((x, y))
    q = deque()
    q.append((x, y))
    space[x][y] = idx
    total = graph[x][y]
    cnt = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and space[nx][ny] == -1:
                if 1 <= abs(graph[nx][ny]-graph[x][y]) <= r:
                    q.append((nx, ny))
                    space[nx][ny] =idx
                    total += graph[nx][ny]
                    cnt += 1
                    country.append((nx, ny))
    for i, j in country:
        graph[i][j] = total // cnt
    return cnt

summary = 0

while True:
    space = [[-1]*n for i in range(n)]
    idx = 0
    for i in range(n):
        for j in range(n):
            if space[i][j] == -1:
                process(i, j, idx)
                idx += 1
    if idx == n * n:
        break
    summary += 1

print(summary)

