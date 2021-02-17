import numpy as np
from set import *

x = Variable(np.array(3.0))
y = add(x, x)
y.backward()

print(y.data)#6.0
print(x.grad)#2.0

x.cleargrad()
y = add(add(x, x), x)
y.backward()

print(y.data)#9.0
print(x.grad)#3.0