'''
#1
n = int(input())
data = list(map(int, input().split()))
data.sort()

result = 0
cnt = 0

for i in data:
    cnt += 1
    if cnt >= i:
        result += 1
        cnt = 0

print(result)
'''
'''
#2
data = input()
result = int(data[0])

for i in range(1, len(data)):
    num = int(data[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num

print(result)
'''
'''
#3
data = input()
cnt_zero = 0
cnt_one = 0

if data[0] == '0':
    cnt_one += 1
else:
    cnt_zero += 1

for i in range(len(data)-1):
    if data[i] != data[i+1]:
        if data[i] == '1':
            cnt_zero += 1
        else:
            cnt_one += 1

print(cnt_zero, cnt_one)
print("result: ",  min(cnt_zero, cnt_one))
'''
'''
#4
n = int(input())
coins = list(map(int, input().split()))
coins.sort()

target = 1
for coin in coins:
    if target < coin:
        break
    target += coin

print(target)
'''
'''
#5
n, m =map(int, input().split())
k = list(map(int, input().split()))

cnt = 0
for i in range(n):
    for j in range(i+1, n):
        if k[i] != k[j]:
            cnt += 1
        else:
            continue

print(cnt)

#sol2)
#weight table
array = [0] * 11
for x in k:
    array[x] += 1
result = 0

for i in range(1, m+1):
    n -= array[i]
    result *= array[i] * n

print(result)
'''
'''
#6
import heapq

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
    q= []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i+1))
    
    leftover = len(food_times)
    time = 0
    previous = 0

    while time + (q[0][0] - previous) * leftover <= k:
        now = heapq.heappop(q)[0]
        time += (now - previous) * leftover
        leftover -= 1
        previous = now
    
    result = sorted(q, key = lambda x : x[1])
    return result[(k-time)%leftover][1]
'''

#solution
def solution(food_times, k):
    result = 0
    length = len(food_times)
    if sum(food_times) <= k:
        return -1
    for i in range(sum(food_times)):
        if food_times[i % length] != 0:
            food_times[i % length] -= 1
            if food_times[i % length] == 0:
                continue
            if (i + 1) > k:
                if food_times[i % length] != 0:
                    result = (i % length) + 1
                    return result
                    break
                else:
                    for j in range(sum(food_times)):
                        i += 1
                        if food_times[i % length] != 0:
                            result = (i % length) + 1
                            break
    
food_times = list(map(int, input().split()))
k = int(input())

print(solution(food_times, k))
                                       
