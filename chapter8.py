'''
d = [0] * 100
def fib(x):
    print("f("+str(x)+")", end=' ')
    if x == 1 or x == 2:
        return 1
    if d[x] != 0:
        return d[x]
    d[x] = fib(x-1) + fib(x-2)
    return d[x]

print(fib(9))
'''
'''
d = [0] * 100
d[1], d[2] = 1, 1
n = 99
for i in range(3, n+1):
    d[i] = d[i-1]+d[i-2]
print(d[n])
'''
'''
x = int(input())
d = [0] * 30001

for i in range(2, x+1):
    d[i] = d[i-1] + 1
    if i % 2 == 0:
        d[i] = min(d[i], d[i//2]+1)
    if i % 3 == 0:
        d[i] = min(d[i], d[i//3]+1)
    if i % 5 == 0:
        d[i] = min(d[i], d[i//5]+1)
print(d[i])
'''
'''
n = int(input())
storage = list(map(int, input().split()))
d = [0] * 100

d[0] = storage[0]
d[1] = max(storage[0], storage[1])
for i in range(2, n):
    d[i] = max(d[i-1], d[i-2]+storage[i])
print(d[n-1])
'''
'''
n= int(input())
d = [0] * 1001

d[1] = 1
d[2] = 3
for i in range(3, n+1):
    d[i] = d[i-1]+d[i-2]*2
print(d[n]%796796) 
'''

n, m = map(int, input().split())
array = []
for i in range(n):
    array.append(int(input()))

d = [10001] * (m+1)

d[0] = 0
for i in range(n):
    for j in range(array[i], m+1):
        d[j] = min(d[j], d[j-array[i]]+1)
if d[m] == 10001:
    print(-1)
else:
    print(d[m])

