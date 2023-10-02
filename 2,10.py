a = int(input())

b = (a % 10) + (a // 10 % 10)
c = (a // 100) + (a // 10 % 10)

if b > c:
    print(int(str(b) + str(c)))
else:
    print(int(str(c) + str(b)))