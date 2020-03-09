import math

for i in range (-8, -16, -1):
    count = 0
    k = 1
    sum = 0

    while (True):
        x = ((-1)**(k-1)) / (k**2)
        sum = sum + x

        if (abs(x) >= 10**i):
            count = count + 1
            k = k + 1   

        else:
            break

    y = 12 * sum    
    print('Erro =', 10**i, '| Número de termos somados da série:', count, '| Valor aproximado de S =', '%.32f' % y)