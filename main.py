a = [4, 4]
if len(a) == 0:
    print(None)
elif len(a) == 1:
    print(a[0])
else:
    m = None  # минимальное
    n = None  # предминимальное
    g = None  # пред-предминимальное
    for i in a:
        if i != m and i != n and i != g:    #эллемент не встречался в списке ранее
            if m is None or i < m:
                g = n
                n = m
                m = i
            elif n is None or i < n:
                g = n
                n = i
            elif g is None or i < g:
                g = i
    print(g)
