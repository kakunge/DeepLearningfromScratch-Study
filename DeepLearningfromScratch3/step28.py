import numpy as np
from dezero import Variable
from dezero.core_simple import rosenbrock

x0 = Variable(np.array(0.0))
x1 = Variable(np.array(2.0))
y = rosenbrock(x0, x1)
y.backward()

print(x0.grad, x1.grad)#-2.0 400.0