'''
#21
from collections import deque
n, l, r = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def process(x, y, idx):
    country = []
    country.append((x, y))
    q = deque()
    q.append((x, y))
    union[x][y] = idx
    summary = graph[x][y]
    cnt = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
        if 0<=nx<n and 0<=ny<n and union[nx][ny] == -1:
            if 1 <= abs(graph[nx][ny] - graph[x][y]) <= r:
                q.append((nx, ny))
                union[nx][ny] = idx
                summary += graph[nx][ny]
                cnt += 1
                country.append((nx, ny))
    for i, j in country:
        graph[i]][j] = summary // cnt
    return cnt

total = 0
while True:
    union = [[-1] * n for i in range(n)]
    idx = 0
    for i in range(n):
        for j in range(n):
            if union[i][j] == -1:
                process(i, j, idx)
                idx += 1
    if idx == n*n:
        break
    total += 1
print(total)    
'''
#22
from collections import deque
def get_next_pos(pos, board):
    next_pos = []
    pos = list(pos)
    pos1_x, pos1_y, pos2_x, pos2_y = pos[0][0], pos[0][1], pos[1][0], pos[1][1]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(4):
        pos1_next_x = pos1_x + dx[i]
        pos1_next_y = pos1_y + dy[i]
        pos2_next_x = pos2_x + dx[i]
        pos2_next_y = pos2_y + dy[i]
        if board[pos1_next_x][pos1_next_y] == 0 and board[pos2_next_x][pos2_next_y] == 0:
            next_pos.append({(pos1_next_x, pos1_next_y), (pos2_next_x, pos2_next_y)})
    if pos1_x == pos2_x:
        for i in [-1, 1]:
            if board[pos1_x+i][pos1_y] == 0 and board[pos2_x+i][pos2_y] == 0:
                next_pos.append({(pos1_x, pos1_y), (pos1_x+i, pos1_y)})
                next_pos.append({(pos2_x, pos2_y), (pos2_x+i, pos2_y)})
    elif pos1_y == pos2_y:
        for i in [-1, 1]:
            if board[pos1_x][pos1_y+i] == 0 and board[pos2_x][pos2_y+i] == 0:
                next_pos.append({(pos1_x, pos1_y), (pos1_x, pos1_y+i)})
                next_pos.append({(pos2_x, pos2_y), (pos2_x, pos2_y+i)})
    return next_pos

def solution(board):
    n = len(board)
    new = [[1] * (n+2) for i in range(n+2)]
    for i in range(n):
        for j in range(n):
            new[i+1][j+1] = board[i][j]
    q = deque()
    visited = []
    pos = {(1,1), (1,2)}
    q.append((pos, 0))
    visited.append(pos)
    while q:
        pos, cost = q.popleft()
        if (n, n) in pos:
            return cost
        for next_pos in get_next_pos(pos, new):
            if next_pos not in visited:
                q.append((next_pos, cost+1))
                visited.append((next_pos))
    return 0
'''
#23
n = int(input())
students = []
for i in range(n):
    students.append(input().split())

students.sort(key = lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for student in students:
    print(student[0])
'''
'''
#24
n = int(input())
location = list(mpa(int, input().split()))
location.sort()

print(location[(n-1)//2])
'''
'''
#25
def solution(n, stages):
    answer = []
    length = len(stages)
    for i in range(1, n+1):
        cnt = stages.count(i)
        if length == 0:
            fail = 0
        else:
            fail = cnt / length
        answer.append((i, fail))
        length -= cnt
    answer = sorted(answer, key = lambda x: x[1], reverse=True)
    answer = [i[0] for i in answer]
    return answer
print(solution(5, [2,1,2,6,2,4,3,3]))
'''
'''
#26
n = int(input())
data = []
for i in range(n):
    data.append(int(input()))

data.sort()
total = 0
prefix = [0]
for i in range(n):
    if n <= 2:
        total = data[0] + data[1]
    else:
        prefix.append(prefix[i]+data[i])
        total += prefix[i+1]
print(total-prefix[1])

#sol2)
import heapq
n = int(input())
heap = []
for i in range(n):
    data = int(input())
    heapq.heappus(heap, data)
result = 0
while len(heap) != 1:
    one = heapq.heappop(heap)
    two = heapq.heappop(heap)
    sum_value = one + two
    result += sum_value
    heapq.heappush(heap, sum_value)
print(result)
'''
'''
#27
#sol1)
n, x = map(int, input().split())
data = list(map(int, input().split()))

cnt = 0
for i in data:
    if i == x:
        cnt += 1
if cnt == 0:
    print(-1)
else:
    print(cnt)
#sol2)
def count_value(array, x):
    n = len(array)
    a = first(array, x, 0, n-1)
    if a == None:
        return 0
    b = last(array, x, 0, n-1)
    return b-a+1

def first(array, target, start, end):
    mid = (start+end)//2
    if (mid == 0 or target > array[mid-1]) and array[mid] == target:
        return mid
    elif array[mid] >= target:
        return first(array, target, start, mid-1)
    else:
        return fisrt(array, target, mid+1, end)

def last(array, target, start, end):
    mid = (start+end)//2
    if (mid == n-1 or target < array[mid+1]) and array[mid] == target:
        return mid
    elif array[mid] > target:
        return last(array, target, start, mid-1)
    else:
        return last(array, target, mid+1, end)
#sol3)
from bisect import bisect_left, bisect_right
def count_by_range(array, left, right):
    left_idx = bisect_left(array, left)
    right_idx = bisect_right(array, right)
    return right_idx - left_idx

n, x = map(int, input().split())
data = list(map(int, input().split()))
cnt = count_by_range(data, x, x)
if cnt == 0:
    print(-1)
else:
    print(cnt)
'''
'''
#28
def pivot(array, start, end):
    if start > end:
        return None
    mid = (start+end)//2
    if array[mid] == mid:
        return mid
    elif array[mid] > mid:
        return pivot(array, start, mid-1)
    else:
        return pivot(array, mid+1, end)

n = int(input())
data = list(map(int, input().split()))
data.sort()
idx = pivot(data, 0, n-1)
if idx == None:
    print(-1)
else:
    print(idx)
'''
'''
#29
n, c = map(int, input().split())
data = []
for i in range(n):
    data.append(int(input()))
data.sort()

start = data[1] - data[0]
end = data[-1] - data[0]
result = 0

while start <= end:
    mid = (start+end) // 2
    value = data[0]
    cnt = 1
    for i in range(1, n):
        if data[i] >= value + mid:
            value = data[i]
            cnt += 1
    if cnt >= c:
        start = mid + 1
        result = mid
    else:
        end = mid - 1
print(result)
'''

#30
from bisect import bisect_left, bisect_right
def counting(array, left, right):    
    left_idx = bisect_left(array, left)
    right_idx = bisect_right(array, right)
    return right_idx - left_idx

array = [[] for i in range(10001)]
reversed_array = [[] for i in range(10001)]

def solution(words, queries):
    answer = []
    for word in words:
        array[len(word)].append(word)
        reversed_array[len(word)].append(word[::-1])
    for i in range(10001):
        array[i].sort()
        reversed_array[i].sort()
    for query in queries:
        if query[0] != '?':
            result = counting(array[len(query)], query.replace('?', 'a'), query.replace('?', 'z'))
        else:
            result = counting(reversed_array[len(query)], query[::-1].replace('?', 'a'), query[::-1].replace('?', 'z'))
        answer.append(result)
    return answer

print(solution(['frodo', 'front', 'frost', 'frozen', 'frame', 'kakao'], ['fro??', '????o', 'fr???', 'fro???', 'pro?']))
