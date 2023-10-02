p = int(input())
v = int(input())
t = int(input())

if t < v < p:
    print(F'          Петя          ')
    print(F'  Вася  ')
    print(F'                  Толя  ')
    print(F'   II      I      III ')
elif v < t < p:
    print(F'          Петя          ')
    print(F'  Толя  ')
    print(F'                  Вася  ')
    print(F'   II      I      III ')
elif p < t < v:
    print(F'          Вася          ')
    print(F'  Толя  ')
    print(F'                  Петя  ')
    print(F'   II      I      III ')
elif t < p < v:
    print(F'          Вася          ')
    print(F'  Петя  ')
    print(F'                  Толя  ')
    print(F'   II      I      III ')
elif v < p < t:
    print(F'          Толя          ')
    print(F'  Петя  ')
    print(F'                  Вася  ')
    print(F'   II      I      III ')
elif p < v < t:
    print(F'          Толя          ')
    print(F'  Вася  ')
    print(F'                  Петя  ')
    print(F'   II      I      III ')