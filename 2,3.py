Petya = int(input())
Vasya = int(input())
Tolya = int(input())

if Tolya < Petya > Vasya:
    print('Петя')
elif Tolya < Vasya > Petya:
    print('Вася')
else:
    print('Толя')