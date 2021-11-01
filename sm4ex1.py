ipt = int(input('Digite o valor de n: '))

if ipt == 0:
    print(1);
else:
    n = ipt
    while ipt > 1:
        ipt -= 1;
        n = n * ipt;
    print(n)
