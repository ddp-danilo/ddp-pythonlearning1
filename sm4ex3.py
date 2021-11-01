loo = 1
ipt = int(input('Digite um número inteiro: '))
soma = 0
while loo > 0:
    if ipt > 0:
        soma = soma + ipt % 10;
        ipt = ipt // 10;
    else:
        loo = 0;
print(soma)
