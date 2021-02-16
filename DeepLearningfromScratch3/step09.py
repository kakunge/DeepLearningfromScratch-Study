import numpy as np
from set import *

def square(x):
    return Square()(x)

def exp(x):
    return Exp()(x)

x = Variable(np.array(0.5))
a = square(x)
b = exp(a)
y = square(b)
# y = square(exp(square(x)))

y.grad = np.array(1.0)
y.backward()
print(x.grad)#3.297442541400256