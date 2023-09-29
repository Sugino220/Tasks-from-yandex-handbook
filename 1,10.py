name = input()
locker_number = int(input())

print(F'Группа №{locker_number // 100}.')
print(F'{locker_number % 10}. {name}.')
print(F'Шкафчик: {locker_number}.')
print(F'Кроватка: {locker_number // 10 % 10}.')