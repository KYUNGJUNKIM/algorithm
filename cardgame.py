n, m = map(int, input().split())
result = 0

'''
# 한 줄씩 입력받은 후 결과 확인하기
for i in range(n):
    data = list(map(int, input().split()))
    minimum = min(data)
    result = max(result, minimum)

print(result)
'''

for i in range(n):
    data = list(map(int, input().split()))
    minimum = 10001
    for x in data:
        minimum = min(minimum, x)
    result = max(result, minimum)

print(result)