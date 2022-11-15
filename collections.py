class Iterator:
    def __init__(self, n):
        self.i = 0
        self.n = n
    
    def __iter__(self):
        return Iterator(self.n)

    def __next__(self):
        odd_num = self.i * 2 + 1
        if odd_num <= self.n:
            self.i += 1
            return odd_num
        else:
            raise StopIteration()
'''
odd = Iterator(14)
for x in odd:
    print(x)
'''
class MyRange:
    def __init__(self, n):
        self.n = n
        self.i = 0
    
    def __iter__(self):
        return MyRange(self.n)

    def __next__(self):
        if self.i < self.n:
            i = self.i
            self.i += 1
            return i
        else:
            raise StopIteration()
'''
mr = MyRange(3)
for y in mr:
    print(y)
'''

def gen_a(n):
    for x in range(n+1):
        if x % 2 == 0:
            yield x

'''
a = gen_a(10)
for x in a:
    print(x)
'''

