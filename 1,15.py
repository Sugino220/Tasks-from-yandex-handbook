H = int(input()) * 60
M = int(input())
T = int(input())

T = H + M + T

while T > 1440:
    T -= 1440

H = T // 60
M = T % 60

if H < 10 and M < 10:
    print(F'0{H}:0{M}')
elif H < 10 and M > 10:
    print(F'0{H}:{M}')
elif H > 10 and M < 10:
    print(F'{H}:0{M}')
elif H > 10 and M > 10:
    print(F'{H}:{M}')