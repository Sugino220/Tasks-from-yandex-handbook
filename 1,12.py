a = int(input())
b = int(input())
c = 0
d = 1

while a > 0:
    c += (a % 10 + b % 10) % 10 * d
    d *= 10
    a //= 10
    b //= 10

print(c)