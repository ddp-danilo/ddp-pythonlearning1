def multiplo_de_3(sm): #faz a soma de todos os algarismos e checa se é multiplo de 3
    sd = 0
    while sm != 0:
        sd += sm % 10
        sm //= 10
    if ((sd % 3) == 0):
        return True
    else:
        return False

def multiplo_de_cinco(c):#retorna true se o número for multiplo de cinco
    if ((c % 10) == 5) or ((c % 10) == 0):
        return True
    else:
        return False

def e_par (pa):#retorna true se pa for par
    if (((pa % 10) % 2) == 0):
        return True
    else:
        return False

def p35(p35):#checa se p35 é par e multiplo de cinco e multiplo de três se sim retorna 'true'
    if e_par(p35) or  multiplo_de_cinco(p35) or multiplo_de_3(p35):
        return True
    else:
        return False
def tpr(tpr):#faz a a divisão de n pelos primos para checar se número(tpr) é primo
    primo = 7
    while (primo < tpr):
        if ((tpr % primo) == 0):#checa se a divisão do numero(tpr) por primo é exata
            return False
        if ((tpr // primo) <= primo):
            return True
        else:
            primo += 1
    else:
        return False
ultimo_primo = 2
def e_primo(pr):#testa se pr é primo. 
    if (pr == 2) or (pr == 3) or (pr == 5) or (pr == 7) or (pr == 11):# checa se pr é igual a  2 ou 3 ou 5 ou 11e retorna true
        return True
    if not p35(pr) and tpr(pr):
        return True
    else:
        return False

def éPrimo(k):# acha o primo mais proximo abaixo de k
    if (k >= 2):
        while k >= 2 and not e_primo(n):
            k -= 1
        return k
