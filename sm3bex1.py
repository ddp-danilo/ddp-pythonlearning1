import math
x1 = int(input('x1: '))
y1 = int(input('y1: '))
x2 = int(input('x2: '))
y2 = int(input('y2: '))
nr = (x1 - x2) ** 2 + (y1 - y2) ** 2
if math.sqrt(nr) >= 10:
    print('longe');
else:
    print('perto')
