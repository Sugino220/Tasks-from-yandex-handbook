goods_name = input()
price = int(input())
weight = int(input())
money = int(input())

print('Чек')
print(F'{goods_name} - {weight}кг - {price}руб/кг')
print(F'Итого: {price * weight}руб')
print(F'Внесено: {money}руб')
print(F'Сдача: {money - (price * weight)}руб')