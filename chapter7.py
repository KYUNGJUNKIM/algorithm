def sequential_search(n, target, array):
    for i in range(n):
        if array[i] == target:
            return i+1

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start+end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None
'''
n = int(input())
stock = list(map(int, input().split()))
m = int(input())
order = list(map(int, input().split()))

for i in range(m):
    result = binary_search(stock, order[i], 0, len(stock)-1)
    if result == None:
        print("NO", end=' ')
    else:
        print("YES", end=' ')
'''

'''
stock = set(map(int, input().split()))
for i in order:
    if i in stock:
        print("Yes")
    else:
        print("No")
'''
n, m = map(int, input().split())
height = list(map(int, input().split()))

start = 0
end = max(height)

result = 0
while start <= end:
    total = 0
    mid = (start+end)//2
    for x in height:
        if x > mid:
            total += x - mid
    if total < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1
print(result)

