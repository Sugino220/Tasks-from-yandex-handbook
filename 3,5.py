c = 0
while (price := float(input())) != 0:
    if price >= 500:
        c += price * 0.90
    else:
        c += price
print(c)