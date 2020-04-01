import math

def main():
    f = lambda x: x**2 - x - math.sin(x + 0.15)
    df = lambda x: 2*x - 1 - math.cos(x + 0.15)
    f2 = lambda x: math.sqrt(x + math.sin(x + 0.15))
    eps = epsilon()
    errorAbs = 5*10**(-8)
    intervalA = 1.51
    intervalB = 1.71

    print("MÉTODO DAS BISSEÇÕES SUCCESSIVAS:")
    FirstZeroSuccBi = SuccessiveBisectionMethod(f,intervalA,intervalB,eps)
    getApproximation(FirstZeroSuccBi,errorAbs)

    print("MÉTODO ITERATIVO SIMPLES:")
    FirstZeroSimpIt = SimpleIterativeMethod(f2,intervalA,eps,100)
    getApproximation(FirstZeroSimpIt,errorAbs)

    print("MÉTODO DE NEWTON:")
    FirstZeroNewton = NewtonMethod(f,df,intervalA,intervalB,eps)
    getApproximation(FirstZeroNewton,errorAbs)

def epsilon():
    eps = 1
    while (eps + 1 > 1):
        eps = eps / 2
    eps  = 2 * eps
    return eps

def SuccessiveBisectionMethod(f,a,b,eps):
    i = 0
    x = a
    vfa = f(a)
    error = abs(b - a)
    while True:
        x = (a + b) / 2
        i += 1
        print(i, "ª Iteração | x ->", x)
        if (f(x) == 0):
            error = 0
        if (error <= eps):
            break
        if((f(x) * vfa) < 0):
            b = x
        else:
            a = x
        error = error / 2
    print("Valor final de x -> %0.20f" % x, "| Valor de a ->", a, "| Valor de b ->", b)
    print("Erro: %0.20f" % error, "| Nº de iterações:", i)
    return x

def SimpleIterativeMethod(f,x0,eps,nMax):
    x1 = f(x0)
    error = abs(x1 - x0)
    i = 0
    while (error > eps and i <= nMax):
        x0 = x1
        x1 = f(x0)
        error = abs(x1 - x0)
        i += 1
        print(i, "ª Iteração | x ->", x1)
    if i > nMax:
        print("Não foi possível ao fim de %d iterações enocntrar a solução com o erro pretendido." % nMax)
        return -500
    else:
        print("Valor final de x -> %0.20f" % x1)
        print("Erro: %0.20f" % error, "| Nº de iterações:", i)
        return x1

def NewtonMethod(f,df,a,b,eps):
    i = 0
    x = a
    while True:
        xn = x - (f(x) / df(x))
        i += 1
        print(i, "ª Iteração | x ->", xn)
        error = abs(xn - x)
        if (error <= eps):
            break
        x = xn
    print("Valor de x -> %0.20f" % x, "| Valor de a ->", a, "| Valor de b ->", b)
    print("Erro: %0.20f" % error, "| Nº de iterações:", i)
    return x

def getApproximation(zero,error):
    if (zero == -500):
        return 
    print("Valor aproximado -> %0.12f" % zero, "±", error)

main()