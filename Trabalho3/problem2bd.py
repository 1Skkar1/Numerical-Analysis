import math as math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

style.use('seaborn-darkgrid')

def main():
	f = lambda x: np.power(math.e, -1/(1 + x**2))
	choice = input("Exercise to be solved:\n1) Exercise 2.b) [nPoints = 7]\n2) Exercise 2.d) [nPoints = 8]\n")
	if (choice == '1'):
		titleLines = 'graph2b_Lines.png'
		titleErrors = 'graph2b_Errors.png'
		nPoints = 7
		interpolation = lambda x: 0.943000 - 0.040245 * (x + 4.000000) - 0.028704 * (x + 4.000000) * (x + 2.857000) - 0.012277 * (x + 4.000000) * (x + 2.857000) * (x + 1.714000) + 0.014682 * (x + 4.000000) * (x + 2.857000) * (x + 1.714000) * (x + 0.571000) - 0.004669 * (x + 4.000000) * (x + 2.857000) * (x + 1.714000) * (x + 0.571000) * (x - 0.571000) + 0.000681 * (x + 4.000000) * (x + 2.857000) * (x + 1.714000) * (x + 0.571000) * (x - 0.571000) * (x - 1.714000) - 0.000000 * (x + 4.000000) * (x + 2.857000) * (x + 1.714000) * (x + 0.571000) * (x - 0.571000) * (x - 1.714000) * (x - 2.857000)
		spline1 = lambda x: -4.375*10**(-3)*x**(3) - 5.2506*10**(-2)*x**(2) - 2.4651*10**(-1)*x + 5.1702*10**(-1)
		spline2 = lambda x: -3.1625*10**(-2)*x**(3) - 2.7053*10**(-1)*x**(2) - 8.2797*10**(-1)*x + 1.0589*10**(-4)	
		spline3 = lambda x: 1.2370*10**(-1)*x**(3) + 3.5061*10**(-1)*x**(2) + 6.2400*10**(-64)*x + 3.6800*10**(-1)
		spline4 = lambda x: -1.2370*10**(-1)*x**(3) + 3.5061*10**(-1)*x**(2) + 6.2400*10**(-64)*x + 3.6800*10**(-1)
		spline5 = lambda x: 3.1625*10**(-2)*x**(3) - 2.7053*10**(-1)*x**(2) + 8.2797*10**(-1)*x + 1.0589*10**(-4)
		spline6 = lambda x: 4.3755*10**(-3)*x**(3) - 5.2506*10**(-2)*x**(2) + 2.4651*10**(-1)*x + 5.1702*10**(-1)
		points = createPoints(f, nPoints)
		printLinesB(titleLines, points, interpolation, spline1, spline2, spline3, spline4, spline5, spline6, f)
		print("> Polinomial Interpolator and Cubic Spline Graph created...")
		printErrorsB(titleErrors, interpolation, spline1, spline2, spline3, spline4, spline5, spline6, f)
		print("> Error Graph created...")

	elif (choice == '2'):
		titleLines = 'graph2d_Lines.png'
		titleErrors = 'graph2d_Errors.png'
		nPoints = 8
		interpolation = lambda x: 0.943000 - 0.044261 * (x + 4.000000) - 0.035684 * (x + 4.000000) * (x + 2.667000) - 0.001215 * (x + 4.000000) * (x + 2.667000) * (x + 1.333000) + 0.010835 * (x + 4.000000) * (x + 2.667000) * (x + 1.333000) * (x - 0.000000) - 0.004806 * (x + 4.000000) * (x + 2.667000) * (x + 1.333000) * (x - 0.000000) * (x - 1.333000) + 0.001202 * (x + 4.000000) * (x + 2.667000) * (x + 1.333000) * (x - 0.000000) * (x - 1.333000) * (x - 2.667000)
		spline1 = lambda x: -1.8280*10**(-3)*x**(3) - 2.1936*10**(-2)*x**(2) - 1.2560*10**(-1)*x + 6.7458*10**(-1)
		spline2 = lambda x: -4.1085*10**(-2)*x**(3) - 3.5841*10**(-1)*x**(2) - 1.0869*x - 2.4091*10**(-1)
		spline3 = lambda x: 9.2506*10**(-2)*x**(3) + 3.2852*10**(-1)*x**(2) + 9.0482*10**(-2)*x + 4.3178*10**(-1)
		spline4 = lambda x: 5.1180*10**(-64)*x**(3) + 1.7005*10**(-1)*x**(2) - 4.7770*10**(-64)*x + 4.1456*10**(-1)
		spline5 = lambda x: -9.2506*10**(-2)*x**(3) + 3.2852*10**(-1)*x**(2) - 9.0482*10**(-2)*x + 4.3178*10**(-1)
		spline6 = lambda x: 4.1085*10**(-2)*x**(3) - 3.5841*10**(-1)*x**(2) + 1.0869*x - 2.4091*10**(-1)
		spline7 = lambda x: 1.8280*10**(-3)*x**(3) - 2.1936*10**(-2)*x**(2) + 1.2560*10**(-1)*x + 6.7458*10**(-1)
		points = createPoints(f, nPoints)
		printLinesD(titleLines, points, interpolation, spline1, spline2, spline3, spline4, spline5, spline6, spline7, f)
		print("> Polinomial Interpolator and Cubic Spline Graph created...")
		printErrorsD(titleErrors, interpolation, spline1, spline2, spline3, spline4, spline5, spline6, spline7, f)
		print("> Error Graph created...")

def createPoints(f, nPoints):
	xPoints = np.around(np.linspace(-4,4,nPoints),3)
	yPoints = []
	for i in xPoints:
		yPoints.append(round(f(i),3))
	points = zip(xPoints,yPoints)
	return list(points)

def printLinesB(title, points, interpolation, spline1, spline2, spline3, spline4, spline5, spline6, originalFunction):
	graph = plt.figure()
	x, y = zip(*points)
	originalP = np.arange(-4.0,4.0,0.001)
	splineP1 = np.arange(-4.0,-2.667,0.001)
	splineP2 = np.arange(-2.667,-1.333,0.001)
	splineP3 = np.arange(-1.333,0,0.001)
	splineP4 = np.arange(0,1.333,0.001)
	splineP5 = np.arange(1.333,2.667,0.001)
	splineP6 = np.arange(2.667,4,0.001)
	subplot = graph.add_subplot(111)
	plt.scatter(x, y, color='black')
	for xy in zip(x, y):
		subplot.annotate('(%s, %s)' % xy, xy=xy, textcoords='offset points', xytext=(0,0))
	plt.plot(splineP1, spline1(splineP1), 'red', label='Spline Cúbico')
	plt.plot(splineP2, spline2(splineP2), 'red')
	plt.plot(splineP3, spline3(splineP3), 'red')
	plt.plot(splineP4, spline4(splineP4), 'red')
	plt.plot(splineP5, spline5(splineP5), 'red')
	plt.plot(splineP6, spline6(splineP6), 'red')
	plt.plot(originalP, interpolation(originalP), 'royalblue', label='Interpolador Polinomial')
	plt.plot(originalP, originalFunction(originalP), 'green', label='Função f')
	plt.legend(loc='lower left')
	plt.savefig(title)
	plt.show()

def printErrorsB(title, interpolation, spline1, spline2, spline3, spline4, spline5, spline6, originalFunction):
	graph = plt.figure()
	originalP = np.arange(-4.0,4.0,0.001)
	splineP1 = np.arange(-4.0,-2.667,0.001)
	splineP2 = np.arange(-2.667,-1.333,0.001)
	splineP3 = np.arange(-1.333,0,0.001)
	splineP4 = np.arange(0,1.333,0.001)
	splineP5 = np.arange(1.333,2.667,0.001)
	splineP6 = np.arange(2.667,4,0.001)
	subplot = graph.add_subplot(111)
	plt.plot(splineP1, abs(originalFunction(splineP1) - spline1(splineP1)), 'red', label='Erro |f - p|')
	plt.plot(splineP2, abs(originalFunction(splineP2) - spline2(splineP2)), 'red')
	plt.plot(splineP3, abs(originalFunction(splineP3) - spline3(splineP3)), 'red')
	plt.plot(splineP4, abs(originalFunction(splineP4) - spline4(splineP4)), 'red')
	plt.plot(splineP5, abs(originalFunction(splineP5) - spline5(splineP5)), 'red')
	plt.plot(splineP6, abs(originalFunction(splineP6) - spline6(splineP6)), 'red')
	plt.plot(originalP, abs(originalFunction(originalP) - interpolation(originalP)), 'royalblue', label='Erro |f - s|')
	plt.legend()
	plt.savefig(title)
	plt.show()

def printLinesD(title, points, interpolation, spline1, spline2, spline3, spline4, spline5, spline6, spline7, originalFunction):
	graph = plt.figure()
	x, y = zip(*points)
	originalP = np.arange(-4.0,4.0,0.001)
	splineP1 = np.arange(-4.0,-2.857,0.001)
	splineP2 = np.arange(-2.857,-1.714,0.001)
	splineP3 = np.arange(-1.714,-0.571,0.001)
	splineP4 = np.arange(-0.571,0.571,0.001)
	splineP5 = np.arange(0.571,1.714,0.001)
	splineP6 = np.arange(1.714,2.857,0.001)
	splineP7 = np.arange(2.857,4,0.001)
	subplot = graph.add_subplot(111)
	plt.scatter(x, y, color='black')
	for xy in zip(x, y):
		subplot.annotate('(%s, %s)' % xy, xy=xy, textcoords='offset points', xytext=(0,0))
	plt.plot(splineP1, spline1(splineP1), 'red', label='Spline Cúbico')
	plt.plot(splineP2, spline2(splineP2), 'red')
	plt.plot(splineP3, spline3(splineP3), 'red')
	plt.plot(splineP4, spline4(splineP4), 'red')
	plt.plot(splineP5, spline5(splineP5), 'red')
	plt.plot(splineP6, spline6(splineP6), 'red')
	plt.plot(splineP7, spline7(splineP7), 'red')
	plt.plot(originalP, interpolation(originalP), 'royalblue', label='Interpolador Polinomial')
	plt.plot(originalP, originalFunction(originalP), 'green', label='Função f')
	plt.legend(loc='lower left')
	plt.savefig(title)
	plt.show()

def printErrorsD(title, interpolation, spline1, spline2, spline3, spline4, spline5, spline6, spline7, originalFunction):
	graph = plt.figure()
	originalP = np.arange(-4.0,4.0,0.001)
	splineP1 = np.arange(-4.0,-2.857,0.001)
	splineP2 = np.arange(-2.857,-1.714,0.001)
	splineP3 = np.arange(-1.714,-0.571,0.001)
	splineP4 = np.arange(-0.571,0.571,0.001)
	splineP5 = np.arange(0.571,1.714,0.001)
	splineP6 = np.arange(1.714,2.857,0.001)
	splineP7 = np.arange(2.857,4.0,0.001)
	subplot = graph.add_subplot(111)
	plt.plot(splineP1, abs(originalFunction(splineP1) - spline1(splineP1)), 'red', label='Erro |f - p|')
	plt.plot(splineP2, abs(originalFunction(splineP2) - spline2(splineP2)), 'red')
	plt.plot(splineP3, abs(originalFunction(splineP3) - spline3(splineP3)), 'red')
	plt.plot(splineP4, abs(originalFunction(splineP4) - spline4(splineP4)), 'red')
	plt.plot(splineP5, abs(originalFunction(splineP5) - spline5(splineP5)), 'red')
	plt.plot(splineP6, abs(originalFunction(splineP6) - spline6(splineP6)), 'red')
	plt.plot(splineP7, abs(originalFunction(splineP7) - spline7(splineP7)), 'red')
	plt.plot(originalP, abs(originalFunction(originalP) - interpolation(originalP)), 'royalblue', label='Erro |f - s|')
	plt.legend()
	plt.savefig(title)
	plt.show()

main()