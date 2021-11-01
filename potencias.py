prt = 0
pot = 0
tim = 0
pot = int(input('Digite o numero a ser elevado por: '))
print('Quantas potencias de', pot, 'você quer:')
tim = int(input())
print('Potencias de',pot)
while prt < tim:
    prt = prt +1;
    print(prt, '=', prt ** pot);
