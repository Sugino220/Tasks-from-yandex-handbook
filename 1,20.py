N = int(input())
M = int(input())
k1 = int(input())
k2 = int(input())

a = N * (k1 - M) / (k1 - k2)
print(int(N - a), int(a))