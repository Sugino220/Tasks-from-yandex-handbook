a = int(input())
b = int(input())
c = []
if a < b:
    for i in range(a, b + 1):
        c.append(i)
    print(*c)
elif a > b:
    for i in range(a, b - 1, -1):
        c.append(i)
    print(*c)
else:
    print(a)