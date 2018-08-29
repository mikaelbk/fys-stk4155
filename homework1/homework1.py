from numpy import *
from matplotlib.pyplot import *

x = np.random.rand(100,1)
y = 5*x*x+0.1*np.random.randn(100,1)
def funcY(x):
	return 5*x*x+0.1


scatter(x,y)

show()

print(y)