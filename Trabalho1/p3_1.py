import math

for i in range (-8, -16, -1):
    count = 0
    k = 1
    sum = 0

    while (True):
        x = abs(math.factorial(k)**2 / (k**2 * math.factorial(2 * k)))
        sum += x
        y = 18 * sum

        if (abs(math.pi**2 - y) >= 10**i):    
            count = count + 1
            k = k + 1

        else:
            break
    
    z = abs(math.pi**2 - y)
    print('Erro =', 10**i, '| Número de termos somados da série:', count, '| Valor aproximado de S =', '%.16f' % z)