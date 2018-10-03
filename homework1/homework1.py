from numpy import *
from matplotlib.pyplot import *

x = random.rand(100)
x = sort(x)
y = 5*x*x+0.1*random.randn(100)

def funcY(x):
	return 5*x*x


scatter(x,y)
grid()
plot(x,funcY(x))

show()