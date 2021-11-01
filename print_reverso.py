n = 1
numeros = []
while n > 0:
    n = int(input("Digite um número inteiros"))
    if n > 0:
        numeros.append(n)
l = len(numeros) - 1
while l >= 0:
    print(numeros[l])
    l -= 1
