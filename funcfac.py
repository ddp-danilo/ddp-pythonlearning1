def fatorial (nfato):
    if nfato == 1 or nfato == 0:
        nfato = 1
    else:
        y = nfato
        while y > 1:
            y -= 1
            nfato *= y
    return nfato
n = int(input('valor de n: '))
p = int(input('valor de p: '))
print('Coeficiente binomial: ', (fatorial(n) / (fatorial(p) * fatorial(n - p))))

