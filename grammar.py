data = dict()
data['사과'] = "Apple"
data['바나나']= "Banana"
data['코코넛']= "Coconut"
'''
key_list = data.keys()
value_list = data.values()
print(key_list)
print(value_list)

for key in key_list:
    print(data[key])
'''
'''
i = 1
result = 0
while i <= 9:
    if i % 2 == 1:
        result += i
    i += 1
print(result)
'''

from itertools import product
data = ['A', 'B', 'C']
result = list(product(data, repeat=2))
from itertools import combinations_with_replacement
result = list(combinations_with_replacement(data, 2))

import heapq
def heapsort(array):
    h = []
    result = []
    for value in array:
        heapq.heappush(h, value)
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result
'''
array = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(array)
'''
def heapsort_reverse(array):
    h = []
    result = []
    for value in array:
        heapq.heappush(h, -value)
    for i in range(len(h)):
        result.append(-heapq.heappop(h))
    return result

#인덱스 간의 개수 세기
from bisect import bisect_left, bisect_right
def count_range(a, left, right):
    left_idx = bisect_left(a, left)
    right_idx = bisect_right(a, right)
    return (right_idx - left_idx)
'''
a = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]
print(count_range(a, 4, 4))
'''
from collections import Counter
counter = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])
'''
print(dict(counter))
'''
#90도 회전시키기
def rotate_90(a):
    row = len(a)
    col = len(a[0])
    result = [[0] * row for i in range(col)]
    for x in range(row):
        for y in range(col):
            result[y][row-1-x] = a[x][y]
    return result

#소수의 판별
def prime(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True
import math
def prime_check(x):
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True
'''
#에라토스테네스의 체
import math
n = 1000
array = [True for i in range(n+1)]

for i in range(2, int(math.sqrt(n))+1):
    if array[i] == True:
        j = 2
        while i * j <= n:
            array[i*j] = False
            j += 1
for i in range(2, n+1):
    if array[i]:
        print(i, end=' ')
'''
'''
#two pointers
n, m = 5, 5
data = [1, 2, 3, 2, 5]

cnt = 0
total = 0
end = 0

for start in range(n):
    while total < m and end < n:
        total += data[end]
        end += 1
    if total == m:
        cnt += 1
    total -= data[start]
print(cnt)

# two pointers_2
n, m = 3, 4
a = [1, 3, 5]
b = [2, 4, 6, 8]

result = [0] * (n+m)
i, j, k = 0, 0, 0
while i < n or j < m:
    if j >= m or (i < n and a[i] <= b[j]):
        result[k] = a[i]
        i += 1
    else:
        result[k] = b[j]
        j += 1
    k += 1
for i in result:
    print(i, end =' ') 
'''
'''
#prefix
n = 5 
data = [10, 20, 30, 40, 50]

total = 0
prefix = [0]
for i in data:
    total += i
    prefix.append(total)

left, right = 3, 4
print(prefix[right]-prefix[left-1])

#소수 구하기
import math
m, n = map(int, input().split())
array = [True for i in range(1000001)]
for i in range(2, int(math.sqrt(n))+1):
    if array[i] == True:
        j = 2
        while i * j <= n:
            array[i*j] = False
            j += 1
for i in range(m, n+1):
    if array[i]: 
        print(i)
'''
'''
#password
from itertools import combinations
l, c = map(int, input().split())
vowels = ('a', 'e', 'i', 'o', 'u')

data = input().split()
data.sort()

for password in combinations(data, l):
    cnt = 0
    for x in password:
        if x in vowels:
            cnt += 1
    if 1 <= cnt <= l-2:
        print(''.join(password))
'''
#JSON
import json

user = {
    "id": "gildong",
    "password": "198237",
    "age": 30,
    "hobby": ["football", "programming"]
}
#with open("user.json", "w", encoding="utf-8") as file:
json_data = json.dumps(user, indent=4) #4칸의 들여쓰기 적용
print(json_data)
data = json.loads(json_data) #json decoding
print(data)