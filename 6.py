n = int(input('add number\n'))

arr = []
for i in range(n):
    res = 1
    for j in range(i + 1):
        res *= (j + 1)
    arr.append(res)
print(arr)
