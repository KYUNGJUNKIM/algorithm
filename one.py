n, k = map(int, input().split())
cnt = 0

'''
while n >= k:
    while n % k != 0:
        n -= 1
        cnt += 1
    n = n // k
    cnt += 1

while n > 1:
    n -= 1
    cnt += 1

print(cnt)
'''

#답지 풀이

result = 0

while True:
    target = (n // k) * k
    result += (n-target)
    n = target
    if n < k:
        break
    result += 1
    n = n // k

result += (n - 1)
print(result)
