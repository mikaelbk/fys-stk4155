from numpy import *
from matplotlib.pyplot import *

# a, b and c are the polynomial coefficients. n is number of datapoints
a = 1.5
b = -7
c = 12
n = 100

# function definition of second order polynomial
def pol2(x):
	return a*x**2 + b*x + c

# x is independent variable while y is response variable (with noise)
x = sort(20*(random.rand(n)-0.5))
y = pol2(x) + (10*max(x)*(random.rand(n)-0.5))

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
plot(x,pol2(x),'b',label = "measurements w/o noise")
plot(x,y,'bo',label = "measurements")
plot(x,yPredict,'r', label = "regression")
legend(loc = "best")
show()