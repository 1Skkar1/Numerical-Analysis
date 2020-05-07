import math as math
import numpy as np

def main():
	f = lambda x: np.power(math.e, -1/(1+x**2))
	nPoints = 8 # 7 for problem 2a) Or 8 for problem 2d) [change accordingly]
	createPoints(f, nPoints)

def createPoints(f, nPoints):
	xPoints = np.around(np.linspace(-4,4,nPoints),3)
	yPoints = []

	for i in xPoints:
		yPoints.append(round(f(i),3))
    
	points = zip(xPoints,yPoints)
	print ("CONJUNTO DE PONTOS: \n", tuple(points))

main()