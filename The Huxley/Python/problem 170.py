cont = 0
lista = []
lista = input().split(" ")
n1, n2, n3, n4 = lista


n1 = int(n1)
if n1 != 1 and n1 != 9:
    if n1 == 2:
        cont = cont + 1
    elif n1 %2 == 1:
        cont = cont + 1

n2 = int(n2)
if n2 != 1 and n1 != 9:
    if n2 == 2:
        cont = cont + 1
    elif n2 %2 == 1:
        cont = cont + 1

n3 = int(n3)
if n3 != 1 and n1 != 9:
    if n3 == 2:
        cont = cont + 1
    elif n3 %2 == 1:
        cont = cont + 1


n4 = int(n4)
if n4 != 1 and n1 != 9:
    if n4 == 2:
        cont = cont + 1
    elif n4 %2 == 1:
        cont = cont + 1

if cont == 4:
    print(n1*n2*n3*n4)
else:
    print("SEM PRODUTO") 
