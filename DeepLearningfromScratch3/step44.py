import numpy as np
from dezero import Variable, Parameter

x = Variable(np.array(1.0))
p = Parameter(np.array(2.0))
y = x * p

print(isinstance(x, Parameter))#False
print(isinstance(p, Parameter))#True
print(isinstance(y, Parameter))#False

