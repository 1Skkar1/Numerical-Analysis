import matplotlib.pyplot as plt 
import numpy as np 

def main():
    graph = plt.figure()
    subplot = graph.add_subplot(111)
    x = np.arange(0, 10, 0.1)
    y = 300*(-((2.79936*10**(-9)*np.exp(0.06*x))/(np.exp(0.06*x) + 2)**2) + (3.52719*10**(-7)*np.exp(0.12*x)/(np.exp(0.06*x)+2)**3) - (5.05564*10**(-6)*np.exp(0.18*x)/(np.exp(0.06*x)+2)**4) + (0.0000235146*np.exp(0.24*x)/(np.exp(0.06*x)+2)**5) - (0.0000470292*np.exp(0.3*x)/(np.exp(0.06*x)+2)**6) + (0.0000423263*np.exp(0.36*x)/(np.exp(0.06*x)+2)**7) - (0.0000141088*np.exp(0.42*x)/(np.exp(0.06*x)+2)**8))

    plt.plot(x, y) 
    plt.show()
    plt.savefig('/OneDrive/FCUP/AN/Trabalhos/3/graph1b.png')
    plt.show()