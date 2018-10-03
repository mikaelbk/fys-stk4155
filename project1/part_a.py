from numpy import *
from matplotlib.pyplot import *

n = 1e3

def franke(x,y):
	f  = 3/4 * exp( -(9*x-2)**2/4 -(9*y-2)**2/4 )
	f += 3/4 * exp( -(9*x+1)**2/49 -(9*y+1)/10 )
	f += 1/2 * exp( -(9*x-7)**2/4 -(9*y-3)**2/4 )
	f -= 1/5 * exp( -(9*x-4)**2 -(9*y-7)**2 )
	return f

x = np.arange(0, 1, 0.05)
y = np.arange(0, 1, 0.05)
x, y = np.meshgrid(x,y)


f = franke(x,y) + random.rand(len(x),len(y))
xb = array([x,y,x**2,y**2,x*y]).T #[x,y,x^2,y^2,xy]

beta = linalg.inv(xb.T.dot(xb)).dot(xb.T).dot(f)