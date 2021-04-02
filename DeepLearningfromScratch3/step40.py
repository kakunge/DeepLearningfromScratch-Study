import numpy as np
from dezero import Variable

x0 = Variable(np.array([1, 2, 3]))
x1 = Variable(np.array([10]))
y = x1 + x0

print(y)#variable([11 12 13])

y.backward()

print(x.grad)