import math

def main():
    f = lambda x: -2 + 6*x - 4*x**2 + 0.5*x**3
    df = lambda x: 6 - 8*x + 1.5*x**2
    eps = epsilon()
    errorAbs = 10**(-6)
    intervalA = 3.5
    intervalB = 6.5
    x1 = 3.5
    x2 = 6.5
    x3 = 4.4

    print("X0 ->", x1, ":")
    FirstZeroNewtonX1 = NewtonMethod(f,df,x1,intervalB,eps)
    getApproximation(FirstZeroNewtonX1,errorAbs)
    print("X0 ->", x2, ":")
    FirstZeroNewtonX2 = NewtonMethod(f,df,x2,intervalB,eps)
    getApproximation(FirstZeroNewtonX2,errorAbs)
    print("X0 ->", x3, ":")
    FirstZeroNewtonX3 = NewtonMethod(f,df,x3,intervalB,eps)
    getApproximation(FirstZeroNewtonX3,errorAbs)

def epsilon():
    eps = 1
    while (eps + 1 > 1):
        eps = eps / 2
    eps  = 2 * eps
    return eps

def NewtonMethod(f,df,a,b,eps):
    i = 0
    x = a
    while True:
        if(df(x) == 0):
            print("Impossível encontrar uma solução")
            return
        xn = x - (f(x) / df(x))
        error = abs(xn - x)
        x = xn
        i += 1
        print(i, "ª Iteração | x ->", xn)
        if (error <= eps):
            break
        if(i==50):
            break
    print("Valor final de x -> %0.20f" % x, "| Valor de a ->", a, "| Valor de b ->", b)
    print("Erro: %0.20f" % error, "| Nº de iterações:", i)
    return x

def getApproximation(zero,error):
    if (zero == -500):
        return 
    print("Valor aproximado -> %0.6f" % zero, "±", error)

main()