#  Esse programa usa '#' para desenhar um quadrado vazio.
largura  = int(input("digite a Largura: "))
altura = int(input("digite a altura: "))
al = altura
while al > 0:
    ll = largura
    while ll > 0:
        if al == 1 or al == altura or ll == 1 or ll == largura:
            print("#", end='')
        else:
            print(end=' ')
        ll -= 1
    print()
    al -= 1
