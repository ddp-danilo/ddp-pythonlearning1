#Programa que fica pedindo números inteiros e mostra seu factorial 
n = 1
while n > 0:
    n = int(input("Digite um numero inteiro!"))
    y = n - 1
    while y > 1:
        n = n*y
        y -= 1
    if n != 0:
        print(n)
    else:
        print("1")

