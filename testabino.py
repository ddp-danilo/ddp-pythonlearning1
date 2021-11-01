def fatorial (nfato):
    if nfato == 1 or nfato == 0:
        nfato = 1
    else:
        y = nfato
        while y > 1:
            y -= 1
            nfato *= y
    return nfato

def coeficientebinomial(n, p):
    return fatorial(n) / (fatorial(p) * fatorial(n - p))


def testafatorial():
    print("5 3: ", coeficientebinomial(5, 3))
    if coeficientebinomial(5, 3) == 10:
        print('ok')
    else:
        print('ugh!')
    print("10 6:", coeficientebinomial(10, 6))
    if coeficientebinomial(10, 6) == 8505:
        print('ok')
    else:
        print('ugh!')

testafatorial()
