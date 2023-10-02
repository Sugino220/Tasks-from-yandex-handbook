a = int(input())
b = int(input())
c = int(input())

if (a * a + b * b == c * c) or (a * a + c * c == b * b) or (c * c + b * b == a * a):
    print("100%")
elif (a * a + b * b < c * c) or (a * a + c * c < b * b) or (c * c + b * b < a * a):
    print("велика")
else:
    print("крайне мала")