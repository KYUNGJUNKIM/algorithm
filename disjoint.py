def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

#number of nodes: x, number of lines: y 
x, y = map(int, input().split())
#Initialize parents table
parent = [0] * (x+1)

#Initialize parents as itself on parents' table
for i in range(1, x+1):
    parent[i] = i
'''
for i in range(y):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

print("A set of element: ", end=' ')
for i in range(1, x+1):
    print(find_parent(parent, i), end=' ')

print()

print("parent table: ", end=' ')
for i in range(1, x+1):
    print(parent[i], end=' ')
'''

cycle =False

for i in range(y):
    a, b = map(int, input().split())
    if find_parent(parent, a) == find_parent(parent, b):
        cycle = True
        break
    else:
        union_parent(parent, a, b)

if cycle:
    print("Cylce occured.")
else:
    print("No cylce")
       