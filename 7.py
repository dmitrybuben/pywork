# 7. Проверить истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат

X=0 
Y=0
Z=0
if(X==0, Y==0, Z==0):
    i = (not(X or Y or Z) == (not X) and (not Y) and (not Z))
if(X==0, Y==0, Z==1):
    b = (not(X or Y or Z) == (not X) and (not Y) and (not Z))
if(X==0, Y==1, Z==1):
    c = (not(X or Y or Z) == (not X) and (not Y) and (not Z))
if(X==1, Y==1, Z==1):
    d = (not(X or Y or Z) == (not X) and (not Y) and (not Z))
if(X==1, Y==0, Z==0):
    e = (not(X or Y or Z) == (not X) and (not Y) and (not Z))
if(X==1, Y==1, Z==0):
    f = (not(X or Y or Z) == (not X) and (not Y) and (not Z))
if(X==1, Y==0, Z==1):
    g = (not(X or Y or Z) == (not X) and (not Y) and (not Z))
if(X==0, Y==1, Z==0):
    h = (not(X or Y or Z) == (not X) and (not Y) and (not Z))
if(i and b and c and d and e and f and g and h) == True:
    print('Утверждение истинно')
else:
    print('Утверждение ложно')
