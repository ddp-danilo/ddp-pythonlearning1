n = int(input('Digite um número inteiro: '))
primo = 11
prepr = True
nigualprimo = False
nsc = 0
nsca = n
n5 = False
if ((n % 10) == 5) or ((n % 10) == 0):
    n5 = True
while nsca != 0:
    nsc += nsca % 10
    nsca //= 10
if (n != 2) and (n > 1) and (n != 5)and (((n % 10) % 2) != 0) and ((nsc % 3) != 0) and not n5 and (n % primo != 0):
    if (((n % 10) % 2) != 0) and ((nsc % 3) != 0) and not n5 and ((n % 7) != 0) and ((n // 7) <= 7):
        nigualprimo = True
    while (n != primo) and not nigualprimo:
        if (((n % 10) % 2) != 0) and ((nsc % 3) != 0) and not n5 and ((n % primo) != 0) and ((n // primo) <= primo):
            nigualprimo = True
        else:
            prepr = False
        while not prepr: 
            p5 = False
            primo += 1
            prsoma = 0
            if ((primo % 10) == 0) or ((primo % 10) == 5):
                p5 = True
            prsca = primo
            while prsca != 0:
                prsoma += prsca % 10
                prsca //= 10
            if (((primo % 10) % 2) != 0) and ((prsoma % 3) != 0) and not p5 and ((primo % 7) != 0) and ((primo // 7) >= 7):
                prepr = True
if nigualprimo or (n == 2) or (n == 5):
    print('primo')
else:
    print('não primo')
