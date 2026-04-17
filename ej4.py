def fAux(v, n):
    if len(v) == 1: 
        if v[0] == n:
            return v[0]
        else:
            return -1


    else: 
        m = len(v) // 2
        l1 = v[:m]
        l2 = v[m:]
        x = fAux(l1, n)
        y = fAux(l2, n + m)

    return max(x, y) 
    


def f(v):
    return fAux(v, 0)

a = list(map(int, input().split()))
print(f(a))
