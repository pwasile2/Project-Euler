fib = 0
f1 = 1
f2 = 0
p2 = 0

while fib < 4000000:
    fib = f1 + f2
    f2 = f1
    f1 = fib
    if fib % 2 == 0:
        p2 += fib
print(p2)