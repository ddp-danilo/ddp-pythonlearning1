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


def test_4():
    assert fizzbuzz(4) == 4
def test_60():
    assert fizzbuzz(22) == 22
def test_75():
    assert fizzbuzz(38) == 38
def test_96():
    assert fizzbuzz(96) == 'Fizz'
def test_3():
    assert fizzbuzz(3) == 'Fizz'
def test_102():
    assert fizzbuzz(102) == 'Fizz'
def test_5():
    assert fizzbuzz(5) == 'Buzz'
def test_20():
    assert fizzbuzz(20) == 'Buzz'
