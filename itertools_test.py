import itertools

a = itertools.count(10)
print(a)
times = 5
for i in a:
    print((str(times) + ":"), i)
    times -= 1
    if( times <= 0 ):
        break

print("===========================")

a = itertools.cycle("ABC")
times = 5
for i in a:
    print((str(times) + ":"), i)
    times -= 1
    if( times <= 0 ):
        break

print("===========================")

a = itertools.repeat("A", 3)
times = 5
for i in a:
    print((str(times) + ":"), i)
    times -= 1
    if( times <= 0 ):
        break

print("===========================")

a = itertools.chain("AB", "CD")
times = 5
for i in a:
    print((str(times) + ":"), i)
    times -= 1
    if( times <= 0 ):
        break
