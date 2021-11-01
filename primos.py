n = int(input('Digite o valor de n: '))
#m3 = False
#m5 = False
#m7 = False
#somadosalgarismos = n
#s = 0
#primo = 7
#neprimo = False
#if n >= 1 and n == 2 or (((n % 10)% 2) != 0):
    #a linha acima checa se n é um ou menor, se o n é 2 e se o n é um número par par
#    while a != 0:
#        s += a % 10;
#        a //= 10;
#        #Esse while soma os algarismos de n
#    un = n % 10;
    #debug
#    print((n == 2), ((s % 3) != 0), (un != 0), (un != 5), ((n // 7) == 7))
#    if (n == 2) or ((s % 3) != 0) and (un != 0) and (un != 5) or ((n // 7) <= 7) and:
#        print('primo');
    #esse if deve checar se se n é 2 ou se ele não é divisivel por 3, 5 ou 7   
#else:
#    print('não é primo');
primo = 6
prepr = False
nigualprimo = False
nsc = 0
nsca = n
n5 = False
if ((n % 10) == 5) or ((n % 10) == 0):
    #n5 = checagem para saber se n é multiplo de 5
    n5 = True
while nsca != 0:
    #nsc = soma de todos os algarismos de n
    nsc += nsca % 10
    nsca //= 10
if (((n % 10) % 2) != 0) and ((nsc % 3) != 0) and not n5:
    if (((n % 10) % 2) != 0) and ((nsc % 3) != 0) and not n5 and ((n % 7) != 0) and ((n // 7) <= 7):
        nigualprimo = True
    while (n != 2) and (n > 1) and (n != primo) and not nigualprimo:
        print('while:', (n != 2), (n > 1), (((n % 10) % 2) != 0), ((nsc % 3) == 0), not n5, (primo != n), not nigualprimo)
        print('if: ',(((n % 10) % 2) != 0), ((nsc % 3) != 0), not n5, ((n % primo) != 0), ((n // primo) <= primo))
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
                #debug
                print('Prepr:', prepr,'primo:', primo)
        #O objetivo desse while é achar todos os números primos de 7 até n 
if nigualprimo or (n == 2):
    print('primo')
else:
    print('não é primo')
