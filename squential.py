import sys

#순차탐색
'''
def sequential_search(n, target, array):
    for i in range(n):
        if array[i] == target:
            return i+1

print("생성할 원소 개수를 입력한 다음 한 칸 띄고 찾을 문자열을 입력하세요.")
data = input().split()
n = int(data[0])
target = data[1]

print("앞서 적은 원소 개수만큼 문자열을 입력하세요.")
array = input().split()

print(sequential_search(n, target, array))
'''

#이진탐색
def binary_search(array, target, start, end):
    '''
    if start > end:
        return None
    mid = (start+end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid+1, end)
    '''
    while start <= end:
        mid = (start+end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n-1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result+1)

input_data = sys.stdin.readline().rstrip()
print(input_data)
