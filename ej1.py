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

if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    if all(x == 0 for x in a):
        print("+ 0")
    else:
        pol(n, a)
        print()