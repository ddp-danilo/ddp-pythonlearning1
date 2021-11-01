#n = int(input('Digite um número inteiro: '))
def soma_de_todos(sm): #faz a soma de todos os algarismos
    sd = 0
    while sm != 0:
        sd += sm % 10
        sm //= 10
    return sd
def multiplo_de_cinco(c):#retorna true se o número for multiplo de cinco
    if ((c % 10) == 5) or ((c % 10) == 0):
        return True
    else:
        return False
def maior_primo(n):
    primo = 11
    prepr = True
    nigualprimo = False
    ultimoprimo = 11
    if n < 11:
        if (n >= 5) and (n < 7):
            return 5 
        if (n == 2):
            return 2
        if (n >= 3) and (n < 5):
            return 3
        else:
            return 7

    else:
        if (((n % 10) % 2) != 0) and ((soma_de_todos(n) % 3) != 0) and not multiplo_de_cinco(n) and ((n % 7) != 0) and ((n // 7) <= 7):
            nigualprimo = True
        while (n != primo) and not nigualprimo:
            if (((n % 10) % 2) != 0) and ((soma_de_todos(n) % 3) != 0) and not multiplo_de_cinco(n) and ((n % primo) != 0) and ((n // primo) <= primo):
                nigualprimo = True
            else:
                prepr = False
            while not prepr: 
                primo += 1
                if (((primo % 10) % 2) != 0) and ((soma_de_todos(primo) % 3) != 0) and not multiplo_de_cinco(primo) and ((primo % 7) != 0) and ((primo // 7) >= 7):
                    prepr = True
                    ultimoprimo = n

        if nigualprimo:
            return n
        else:
            return ultimoprimo

def teste_pr1():
    assert maior_primo(6) == 5
def teste_pr3():
    assert maior_primo(100) == 97
def teste_pr4():
    assert maior_primo(3) == 3
def teste_pr5():
    assert maior_primo(10) == 7
def teste_pr2():
    assert maior_primo(11) == 11
def teste_pr6():
    assert maior_primo(2) == 2
def teste_pr7():
    assert maior_primo(6) == 5
