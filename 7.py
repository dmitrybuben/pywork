# 7. Проверить истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат

def values(X,Y,Z):
    b = (not(X or Y or Z) == (not X and not Y and not Z))
    return b

a1 = values(0,0,0)
a2 = values(0,0,1)
a3 = values(0,1,0)
a4 = values(0,1,1)
a5 = values(1,0,0)
a6 = values(1,0,1)
a7 = values(1,1,0)
a8 = values(1,1,1)

if(a1 and a2 and a3 and a4 and a5 and a6 and a7 and a8):
    print('Утверждение истинно')
else:
    print('Утверждение ложно')
