#n = int(input('Digite um número inteiro: '))
def soma_de_todos(sm): #faz a soma de todos os algarismos
    sd = 0
    while sm != 0:
        sd += sm % 10
        sm //= 10
    return sd
def maior_primo(n):
    primo = 11
    prepr = True
    nigualprimo = False
    n5 = False
    if ((n % 10) == 5) or ((n % 10) == 0):
        n5 = True
    if (n != 2) and (n > 1) and (n != 5)and (((n % 10) % 2) != 0) and ((soma_de_todos(n) % 3) != 0) and not n5 and (n % primo != 0):
        if (((n % 10) % 2) != 0) and ((soma_de_todos(n) % 3) != 0) and not n5 and ((n % 7) != 0) and ((n // 7) <= 7):
            nigualprimo = True
        while (n != primo) and not nigualprimo:
            if (((n % 10) % 2) != 0) and ((soma_de_todos(n) % 3) != 0) and not n5 and ((n % primo) != 0) and ((n // primo) <= primo):
                nigualprimo = True
            else:
                prepr = False
            while not prepr: 
                p5 = False
                primo += 1
                if ((primo % 10) == 0) or ((primo % 10) == 5):
                    p5 = True
                if (((primo % 10) % 2) != 0) and ((soma_de_todos(primo) % 3) != 0) and not p5 and ((primo % 7) != 0) and ((primo // 7) >= 7):
                    prepr = True
    if nigualprimo or (n == 2) or (n == 5):
        return True
    else:
        return False

