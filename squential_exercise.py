#부품찾기
'''
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

n = int(input())
#storage = list(map(int, input().split()))
storage = set(map(int, input().split()))
#storage.sort()

m = int(input())
request = list(map(int, input().split()))


for i in request:
    result = binary_search(storage, i, 0, n-1)
    if result == None:
        print("no", end=' ')
    else:
        print("yes", end=' ')

for i in request:
    if i in storage:
        print("yes", end=' ')
    else:
        print("no", end=' ')
'''

#떡볶이 떡 만들기
n, m = map(int, input().split())
x = list(map(int, input().split()))

start = 0
end = max(x)

height = 0
while start <= end:
    total = 0
    mid = (start+end) // 2
    for i in x:
        if i > mid:
            total += (i-mid)
    if total < m:
        end = mid - 1
    else:
        height = mid
        start = mid + 1

print(height)