string = [input(), input(), input()]
a = []
for i in string:
    if 'зайка' in i:
        a.append(i)
print(sorted(a)[0], len(sorted(a)[0]))