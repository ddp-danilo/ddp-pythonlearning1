soma = 0 
vez = int(input('Quantos números você quer somar: '))
quan = vez
if vez == 0:
    print(0, 'tchau');
else:
    print('Digite um dos números que quer somar e aperte enter')

    if vez == 1:
        soma = int(input(':'));
        print(soma);
    else:
        while vez > 0:
            if vez == 1:
                print('Ultimo número');
            else:
                print('Faltam', vez, 'números');
            soma = soma + int(input(': '));
            vez = vez - 1;
        print('A soma dos', quan, 'números foi', soma);
