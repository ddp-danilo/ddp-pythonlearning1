def multiplo_de_3(sm): 
    sd = 0
    while sm != 0:
        sd += sm % 10
        sm //= 10
    if ((sd % 3) == 0):
        return True
    else:
        return False

def multiplo_de_cinco(c):
    if ((c % 10) == 5) or ((c % 10) == 0):
        return True
    else:
        return False

def e_par (pa):
    if (((pa % 10) % 2) == 0):
        return True
    else:
        return False

def p35(p35):
    if e_par(p35) or  multiplo_de_cinco(p35) or multiplo_de_3(p35):
        return True
    else:
        return False
def tpr(tpr):
    primo = 7
    while (primo < tpr):
        if ((tpr % primo) == 0):
            return False
        if ((tpr // primo) <= primo):
            return True
        else:
            primo += 1
    else:
        return False
ultimo_primo = 2
def e_primo(pr):
    if (pr == 2) or (pr == 3) or (pr == 5) or (pr == 7) or (pr == 11):
        return True
    if not p35(pr) and tpr(pr):
        return True
    else:
        return False

