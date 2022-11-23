# Напишите программу для. проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

X = True
Y = True
Z = True

truth = False
while not truth:

    if not (X or Y or Z) == (not X and not Y and not Z):
        print('истинно')
        X = not X
        if (X and Y and Z):
            break
    else:
        print('not истинно')

    if not X:
        Y = not Y

    if not Y and not X :
        Z = not Z
