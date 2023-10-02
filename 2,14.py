a = sorted(input())
if a[0] == '0' and a[1] == '0' and a[2] == '0':
    print(0, 0)
elif a[0] == '0' and a[1] == '0' and a[2] != '0':
    print((int(a[2]) * 10), (int(a[2]) * 10))
elif a[0] == '0':
    print((int(a[1]) * 10), (int(a[2] + a[1])))
else:
    print((int(a[0] + a[1])), (int(a[2] + a[1])))