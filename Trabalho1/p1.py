import math

for i in range (-8, -16, -1):
    count = 0
    k = 1
    sum = 0

    while (True):
        x = abs(math.factorial(k)**2 / (k**2 * math.factorial(2 * k)))
        
        if (x >= 10**i):
            sum += x
            count = count + 1
            k = k + 1

        else:
            break
    
    y = 18 * sum
    print('Erro =', 10**i, '| Número de termos somados da série:', count, '| Valor aproximado de S =', '%.16f' % y)
