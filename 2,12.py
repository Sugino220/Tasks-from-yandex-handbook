a = sorted(list((input(), input(), input())))
if int(a[2]) >= int(a[1]) + int(a[0]):
    print('NO')
else:
    print('YES')