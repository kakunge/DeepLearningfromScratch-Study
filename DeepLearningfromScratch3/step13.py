import numpy as np
from set import *

x = Variable(np.array(2.0))
y = Variable(np.array(3.0))

z = add(square(x), square(y))
z.backward()

print(z.data)#13.0
print(x.grad)#4.0
print(y.grad)#6.0