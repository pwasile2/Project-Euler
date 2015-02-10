x = 0
sum1 = 0
sum2 = 0
total = 0
while x < 101:
    sum1 += x ** 2
    sum2 += x
    x +=1
total = sum1 - sum2 ** 2
print(total)