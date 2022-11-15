#이미 계산된 결과를 memoization하기 위해 리스트 초기화
d = [0] * 100

def fib(x):
    print('f('+str(x)+')', end=' ')
    if x == 1 or x == 2:
        return 1
    if d[x] != 0:
        return d[x]
    d[x] = fib(x-1) + fib(x-2)
    return d[x]

'''
d[1] = 1
d[2] = 1
n = 99
for i in range(3, n+1):
    d[i] = d[i-1] + d[i-2]

print(d[n])
'''
'''
#1로 만들기
x = int(input())
d = [0] * 30001

for i in range(2, x+1):
    d[i] = d[i-1] + 1
    if i % 2 == 0:
        d[i] = min(d[i], d[i//2] + 1)
    if i % 3 == 0:
        d[i] = min(d[i], d[i//3] + 1)
    if i % 5 == 0:
        d[i] = min(d[i], d[i//5] + 1)
    
print(d[x])
'''
'''
#개미전사
n = int(input())
array = list(map(int, input().split()))

d = [0] * 100

d[0] = array[0]
d[1] = max(array[0], array[1])
for i in range(2, n):
    d[i] = max(d[i-1], d[i-2]+array[i])

print(d[n-1]) # i = (n-1)
'''
'''
#바닥공사
n = int(input())
d= [0] * 1001

d[1] = 1
d[2] = 3
result = 0
for i in range(3, n+1):
    d[i] = (d[i-1] + d[i-2]*2)
    result = d[i] % 796796

print(result)
'''
#효율적인 화폐 구성
n, m = map(int, input().split())
coin = list(map(int, input().split()))

d = [10001] * (m+1)

d[0] = 0
for i in range(n):
    for j in range(coin[i], m+1):
        d[j] = min(d[j], d[j-coin[i]]+1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])



