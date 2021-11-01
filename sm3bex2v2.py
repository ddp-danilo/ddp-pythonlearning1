import math
a = int(input('a'))
b = int(input('b'))
c = int(input('c'))
delta = (b ** 2) - 4*a*c
if delta < 0:
        print('esta equação não possui raízes reais');
else:
    deroot = math.sqrt(delta)
    x1 = ((-b) + deroot) / 2*a
    x2 = ((-b) - deroot) / 2*a
    if delta == 0:
        if x1 == x2:
            print('a raiz desta equação é', x1 );
        else:
            print('a raiz dupla desta equação é', x1, x2);
    if delta > 0:
        if x1 < x2:
            print('as raízes desta equação são', x1, 'e', x2);
        else:
            print('as raízes desta equação são', x2, 'e', x1);
