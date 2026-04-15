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

def sumaPolinomios(n, a, m, b):
    def suma(a, b):
        if len (a)  == 0: 
            return b
        if len (b) == 0:
            return a
        else: 
            return [a[0] + b[0]] + suma(a[1:], b[1:])

    res = suma(a, b)
    if all(x == 0 for x in res):
        print("+ 0", end='')
    else:
        pol(max(len(a) - 1, len(b) - 1), res)

def restaPolinomios(n, a, m, b):
    def resta(a, b):
        if len (a)  == 0: 
            return [-x for x in b] #cambiamos los elementos se signo de b
        if len (b) == 0:
            return a
        else: 
            return [a[0] - b[0]] + resta(a[1:], b[1:])

    res = resta(a, b)
    if all(x == 0 for x in res):
        print("+ 0", end='')
    else:
        pol(max(len(a) - 1, len(b) - 1), res)


