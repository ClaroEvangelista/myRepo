def gensquares(n):
    for x in range(n):
        yield x ** 2


for y in gensquares(10):
    print(y, end=' ')