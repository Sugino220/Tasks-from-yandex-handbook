c = 0
while (string := input()) != 'Приехали!':
    if 'зайка' in string:
        c += 1
print(c)