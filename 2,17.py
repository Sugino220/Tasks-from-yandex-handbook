import math

a = float(input())
b = float(input())
c = float(input())

if a == 0:
    print('Infinite solutions')
    
D = (b**2) - (4 * a * c)

if D >= 0:
    x1 = ((b * -1) + math.sqrt(D)) / (2 * a)
    x2 = ((b * -1) - math.sqrt(D)) / (2 * a)
    if x1 == x2:
        print(round(x2, 2))
    else:
        print(round(x2, 2), round(x1, 2))
else:
    print('No solution')