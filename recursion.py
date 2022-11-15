def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def fib(idx):
    if idx == 0:
        return 0
    elif idx == 1:
        return 1
    else:
        return fib(idx-1) + fib(idx-2)

def exp(a, n):
    if n == 0:
        return 1
    else:
        return a * exp(a, n-1)

def check_symmetry(sequence):
    length = len(sequence)

    if length <= 1:
        return True
    elif sequence[0] != sequence[(length-1)]:
        return False
    else:
        return check_symmetry(sequence[1:length-1])
'''
print(check_symmetry("aabbaa"))
print(check_symmetry([1,2,3,2,1])) 
print(check_symmetry((2,4,3,2)))
'''

def check_symmetry2(sequence):
    return helper(sequence, 0, len(sequence)-1)

def helper(sequence, low, high):
    if high <= low:
        return True
    elif sequence[low] != sequence[high]:
        return False
    else:
        return helper(sequence, low+1, high-1)

'''
print(check_symmetry2('aabbbaa'))
print(check_symmetry2([1,2,3,2,1]))
'''

import os

def calc_size(path):
    size = 0

    if os.path.isfile(path):
        size += os.path.getsize(path)
    else:
        subs = os.listdir(path)
        for sub in subs:
            size += calc_size(path + "||" + sub)

#tail_recursion
def factorial_tail(n):
    return factorial_helper(n,1)

def factorial_helper(n, result):
    if n == 0:
        return result
    else:
        return factorial_helper(n-1, (n * result))

print(factorial_tail(5))

def fib_tail(idx):
    return fib_helper(idx, 0, 1)

def fib_helper(idx, prev, curr):
    if idx < 2:
        return curr
    else:
        return fib_helper(idx-1, curr, prev+curr)

print(fib_tail(8))