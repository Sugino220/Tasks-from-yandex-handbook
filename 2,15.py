a = input()
b = input()
c = sorted(a + b)

print(c[3] + str((int(c[1]) + int(c[2])) % 10) + c[0])