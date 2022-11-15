'''
#7
n = input()
length = len(n)
total = 0

for i in range(length//2):
    total += int(n[i])
    total -= int(n[(length-1)-i])
if total == 0:
    print("lucky")
else:
    print("ready")
'''
'''
#8
string = input()
result = []
total = 0

for x in string:
    if x.isalpha():
        result.append(x)
    else:
        total += int(x)

result.sort()
if total != 0:
    result.append(str(total))
print(''.join(result))
'''
'''
#9
data = input()

def solution(data):
    answer = len(data)
    for step in range(1, (len(data)//2 + 1)):
        result = ""
        prev = data[:step]
        cnt = 1
        for j in range(step, len(data), step):
            if prev == data[j:j+step]:
                cnt += 1
            else:
                result += (str(cnt) + prev) if cnt >= 2 else prev
                prev = data[j:j+step]
                cnt = 1
        result += (str(cnt) + prev) if cnt >= 2 else prev
        answer = min(answer, len(result))
    return answer

print(solution(data))
'''

#10
def rotate_90(a):
    n = len(a)
    m = len(a[0])
    result = [[0] * n for i in range(m)]
    for i in range(n):
        for j in range(m):
            result[j][n-1-i] = a[i][j]
    return result

def check(lock):
    lock_length = len(lock) // 3
    for i in range(lock_length, lock_length*2):
        for j in range(lock_length, lock_length*2):
            if lock[i][j] != 1:
                return False
    return true

def solution(key, lock):
    n = len(lock)
    m = len(key)
    new = [[0] * (n * 3) for i in range(n+3)]
    for i in range(n):
        for j in range(n):
            new[i+n][j+n] = lock[i][j]
    for rotation in range(4):
        key = rotate_90(key)
        for x in range(n*2):
            for y in range(n*2):
                for i in range(m):
                    for j in range(m):
                        new[x+i][y+j] += key[i][j]
                if check(new) == True:
                    return True
                for i in range(m):
                    for j in range(m):
                        new[x+i][y+j] -= key[i][j]
    return False
