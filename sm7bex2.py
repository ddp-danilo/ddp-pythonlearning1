def é_hipotenusa(n):
    l1 = 1
    while l1 < n:
        l2 = 0
        while l2 < n:
            l2 += 1
            if (l1 + l2) >= n:# se a soma dos catetoscor igual a n
                if (l1 ** 2) + (l2 ** 2) == (n ** 2):# pitagoras reverso
                    return True
                    
        l1 += 1
    return False
def soma_hipotenusas(sh):
    l = 1
    s = 0
    while l <= sh:
        if é_hipotenusa(l):
            s += l
        l += 1
    return s
