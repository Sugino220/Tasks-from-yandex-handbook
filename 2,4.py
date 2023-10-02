Petya = int(input())
Vasya = int(input())
Tolya = int(input())

if Tolya < Vasya < Petya:
    print('1. Петя')
    print('2. Вася')
    print('3. Толя')
elif Vasya < Tolya < Petya:
    print('1. Петя')
    print('2. Толя')
    print('3. Вася')
elif Tolya < Petya < Vasya:
    print('1. Вася')
    print('2. Петя')
    print('3. Толя')
elif Petya < Tolya < Vasya:
    print('1. Вася')
    print('2. Толя')
    print('3. Петя')
elif Vasya < Petya < Tolya:
    print('1. Толя')
    print('2. Петя')
    print('3. Вася')
elif Petya < Vasya < Tolya:
    print('1. Толя')
    print('2. Вася')
    print('3. Петя')