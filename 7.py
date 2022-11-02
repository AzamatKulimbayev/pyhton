n = float(input('add number\n'))

n = n * 10000000000
n = int(n)
res = 0
while n != 0:
    res += n % 10
    n /= 10

print(res)