madi = 0
msub = 0
mmulti = 0 
mdivis = 0
star = 0
sair = 0

while star <= 0 or star > 5: 
    print('Calculadora'); 
    print('1 - Adição'); 
    print('2 - Subtração'); 
    print('3 - Multiplicação'); 
    print('4 - Divisão'); 
    print('5 - Sair'); 
    star = int(input('Digite o numero de sua escolha e aperte Enter: '));

    while star == 1:
        print('Adição');
        d1 = float(input('Digite o primeiro numero da soma e aperte enter: '));
        d2 = float(input('Agora o Segundo: '));
        print('A soma deu:', d1 + d2);
        print('0 - Voltar ');
        print('1 - Repetir');
        print('5 - Sair');
        star = int(input('Digite o número desejado e aperte enter: '));
    if star < 0 or star > 5:
        print('Digito errado')
if star == 5: 
    print('Saindo'); 
    exit();

