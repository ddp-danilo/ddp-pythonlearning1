n = 1
end = True
lista =[]
while end:
    n = input("Digite números inteiros e digite 0 para Terminar:")
    if n.isnumeric():
        n = int(n)
        if n == 0:
            end = False
        else:
            lista.append(n)
    else:
        print("Digito inválido tente novamente.")
l = len(lista) - 1
for pt in lista:
    print(lista[l])
    l -= 1
