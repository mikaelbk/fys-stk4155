from __future__ import division
from numpy import *
from matplotlib.pyplot import *
from mpl_toolkits.mplot3d import Axes3D

# a, b and c are the polynomial coefficients. n is number of datapoints
a = 1.5
b = -7
c = 12
n = 100

# function definition of second order polynomial
def pol2(x):
	return a*x**2 + b*x + c

# Franke's function: 2D function used when testing interpolation and fitting algorithms
def franke(x,y):
	f  = 3/4 * exp( -(9*x-2)**2/4 -(9*y-2)**2/4 )
	f += 3/4 * exp( -(9*x+1)**2/49 -(9*y+1)/10 )
	f += 1/2 * exp( -(9*x-7)**2/4 -(9*y-3)**2/4 )
	f -= 1/5 * exp( -(9*x-4)**2 -(9*y-7)**2 )

# x is independent variable while y is response variable (with noise)
"""
x = sort(20*(random.rand(n)-0.5))
y = pol2(x) + (10*max(x)*(random.rand(n)-0.5))"""

# Make data
x = arange(0,1,0.05)
y = arange(0,1,0.05)
x,y = meshgrid(x,y)
print(x)

# defining the X matrix as [[x^2],[x],[1]]
# where each of the three elements are column vectors
xb = array([x**2,x,ones(n)]).T

# here's where the magic happens
# through linear algebra this should give coefficients of the polynomial
# based on minimizing the sum of the square of residuals
beta = linalg.inv(xb.T.dot(xb)).dot(xb.T).dot(y)

# predicted y values based on the coefficients found (beta)
yPredict = xb.dot(beta)

#plotting
fig = figure()
ax = fig.gca(projection='3d')

#plotting
"""
plot(x,pol2(x),'b',label = "measurements w/o noise")
plot(x,y,'bo',label = "measurements")
plot(x,yPredict,'r', label = "regression")
legend(loc = "best")
show()"""