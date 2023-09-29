goods_name = input()
price = int(input())
weight = int(input())
money = int(input())
a = 35 - len(str(weight)) - len(str(price)) - 16
whitespace = ' ' * a

print(F'{"Чек":=^35}')
print(F'Товар:{goods_name:>29}')
print(F'Цена:{whitespace}{weight}кг * {price}руб/кг')
print(F'Итого:{price * weight:>26}руб')
print(F'Внесено:{money:>24}руб')
print(F'Сдача:{money - (price * weight):>26}руб')
print('=' * 35)