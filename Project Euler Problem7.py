def is_prime(n):
    count = 0
    for i in range(2, n):
        if n%i == 0:
            return False
            break
    else:
        count += 1
    if count == n-2:
        return True

def term(n):
    x = 0
    count = 0
    while count!= n:
        x += 1
        if is_prime(x) == True:
            count += 1
    print(x)

term(10001)