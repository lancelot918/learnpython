def f123():
    yield 1
    yield 2
    yield 3

def func():
    x = 1
    while True:
        y = (yield x)
        x += y

for item in f123():
    print (item) 

geniter = func()
print(next(geniter))
print(geniter.send(3))