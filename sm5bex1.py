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

def fizzbuzz(fzbz):
    if multiplo_de_cinco(fzbz) or multiplo_de_3(fzbz):
        if multiplo_de_cinco(fzbz) and multiplo_de_3(fzbz):
            return 'FizzBuzz'
        if multiplo_de_3(fzbz):
            return 'Fizz'
        if multiplo_de_cinco(fzbz):
            return 'Buzz'
    else:
        return fzbz
