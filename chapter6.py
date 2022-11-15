'''
def quick_sort(array):
    if len(array) <= 1:
        return array
    pivot = array[0]
    tail = array[1:]

    left = [x for x in tail if x <= pivot]
    right = [x for x in tail if x > pivot]

    return quick_sort(left)+[pivot]+quick_sort(right)

print(quick_sort([5, 7, 9, 0, 3, 1, 6, 2, 4, 8]))
'''
'''
array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
cnt = [0] * (max(array)+1)

for i in range(len(array)):
    cnt[array[i]] += 1
for i in range(len(cnt)):
        print(i, end=' ')
        print(cnt[i])
'''
'''
n = int(input())
data = []
for i in range(n):
    data.append(int(input()))

data.sort(reverse=True)
print(data)
'''
'''
n = int(input())
data = []
for i in range(n):
    array = input().split()
    data.append((array[0],array[1]))

data = sorted(data, key=lambda student: student[1])
for student in data:
    print(student[0], end =' ')
'''

n, k = map(int, input().split())
first = list(map(int, input().split()))
second = list(map(int, input().split()))

first.sort()
second.sort(reverse=True)

for i in range(k):
    if first[i] < second[i]:
        first[i], second[i] = second[i], first[i]
    else:
        break

print(sum(first))