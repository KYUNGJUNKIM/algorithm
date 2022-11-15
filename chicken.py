from itertools import combinations

n, m = map(int, input().split())
chicken, house= [], []

for r in range(n):
    data = list(map(int, input().split()))
    for c in range(n):
        if data[c] == 1:
            house.append((r,c))
        elif data[c] == 2:
            chicken.append((r,c))

candidates = list(combinations(chicken, m))

def total(candidate):
    result = 0
    for x, y in house:
        temp = int(1e9)
        for a, b in candidate:
            temp = min(temp, abs(x-a)+abs(y-b))
        result += temp
    return result

minimum = int(1e9)
for candidate in candidates:
    minimum = min(minimum, total(candidate))

print(minimum)
