'''
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
    for j in range(i, 0, -1):
        if array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
        else:
            break
'''
'''
for i in range(len(array)):
    minimum = i
    for j in range(i+1, len(array)):
        if array[minimum] > array[j]:
            minimum = j
    array[i], array[minimum] = array[minimum], array[i]
'''
'''
def quick_sort(array, start, end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        #pivot보다 큰 데이터를 찾기 전까지 반복
        while left <= end and array[left] <= array[pivot]:
            left += 1
        #pivot보다 작은 데이터를 찾기 전까지 반복
        while right > start and array[right] >= array[pivot]:
            right -= 1
        if left > right:
            #엇갈린 상황에서는 작은 데이터와 pivot을 서로 교체
            array[right], array[pivot] = array[pivot], array[right]
        else:
            #엇갈리지 않은 상황에서는 작은 데이터와 큰 데이터를 각각 교체
            array[left], array[right] = array[right], array[left]
    #분할 후 왼쪽 부분과 오른쪽 부분에서 각각 정렬
    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)

quick_sort(array, 0, len(array)-1)
'''
'''
def quick_sort2(array):
    if len(array) <= 1:
        return array
    
    pivot = array[0]
    tail = array[1:]

    left = [x for x in tail if x <= pivot]
    right = [x for x in tail if x > pivot]

    return quick_sort2(left) + [pivot] + quick_sort2(right)
    
print(quick_sort2(array))
'''
'''
#계수정렬
array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
count = [0] * (max(array)+1)

for i in range(len(array)):
    count[array[i]] += 1

for i in range(len(count)):
    for j in range(count[i]):
        print(i, end=' ')
'''
'''
#1
n = int(input())

array = []
for i in range(n):
    array.append(int(input()))

array = sorted(array, reverse = True)

for i in array:
    print(i, end=' ')
'''
'''
#2
n = int(input())
array = []
for i in range(n):
    data = input().split()
    array.append((data[0], int(data[1])))

array = sorted(array, key=lambda student: student[1], reverse=True)

for student in array:
    print(student[0], end=' ')
'''
#3
n, k = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else:
        break

print(sum(a))

