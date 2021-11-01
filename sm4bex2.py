b = int(input('Digite um número inteiro: '))
tem = False

while not tem and b != 0:
    a = b % 10;
    b = b // 10;
    c = b  % 10;
    if a == c:
        tem = True;
if tem:
    print('sim');
else:
    print('não');
