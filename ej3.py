def suma(a, b):
    if len (a)  == 0: 
        return b
    if len (b) == 0:
        return a
    else: 
        return [a[0] + b[0]] + suma(a[1:], b[1:])

def resta(a, b):
    if len (a)  == 0: 
        return [-x for x in b] #cambiamos los elementos se signo de b
    if len (b) == 0:
        return a
    else: 
        return [a[0] - b[0]] + resta(a[1:], b[1:])
    
def pol(n, a):
    if len(a) == 1:
        if(a[0] > 0):
            if(n >= 1):
                print(f"+ {a[0]}x^{n} ", end='')
            else:
                print(f"+ {a[0]}", end='')
        elif (a[0] < 0):
            if(n >= 1):
                print(f"- {abs(a[0])}x^{n} ", end='')
            else:
                print(f"- {abs(a[0])}", end='')
        elif a[0] == 0:
               pass
    else:
        pol(n, a[-1:]) #lista con el ultimo elemento
        pol(n-1, a[:-1]) #lista con todos los elementos menos el ultimo

def multiplica_polinomios(x,y):  
    if len (x) == 0 or len(y) == 0:
       return []
    elif len(x) == 1:
         return [x[0] * e for e in y]
    elif len(y) == 1:
        return [y[0] * e for e in x]

    else:
        mitad = min(len(x) // 2, len(y) // 2)
        Pa = x[mitad:]
        Pb = x[:mitad]
        Qa = y[mitad:]
        Qb = y[:mitad]

        PaQa = multiplica_polinomios(Pa, Qa)
        PbQb = multiplica_polinomios(Pb, Qb)
        t = resta(resta(multiplica_polinomios(suma(Pa, Pb), suma(Qa, Qb)),PaQa), PbQb)
        return suma(suma([0] * (2*mitad) + PaQa, [0] * mitad + t), PbQb)

n = int(input())
x = list(map(int, input().split()))
m = int(input())
y = list(map(int, input().split()))
resultado = multiplica_polinomios(x, y)
if all(e == 0 for e in resultado):
    print("+ 0")
else:
    pol(n + m, resultado)
    print()

