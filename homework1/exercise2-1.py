from numpy import *
from matplotlib.pyplot import *

a = 1.5
b = -7
c = 12
n = 100

def pol2(x):
	return a*x**2 + b*x + c

x = sort(20*(random.rand(n)-0.5))
y = pol2(x) + (10*max(x)*(random.rand(n)-0.5))

xb = zeros([3,n])
xb[0] = x**2
xb[1] = x
xb[2] = ones(n)
xb = xb.T

beta = linalg.inv(xb.T.dot(xb)).dot(xb.T).dot(y)

yPredict = xb.dot(beta)

plot(x,pol2(x),'b',label = "measurements w/o noise")
plot(x,y,'bo',label = "measurements")
plot(x,yPredict,'r', label = "regression")
legend(loc = "best")
show()