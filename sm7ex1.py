#desenho que usa '#' para fazer quadrados
largura  = int(input("digite a Largura: "))
altura = int(input("digite a altura: "))
while altura > 0:
    ll = largura
    while ll > 0:
        print("#", end='')
        ll -= 1
    print()
    altura -= 1
