import numpy as np
from dezero import Variable

x = Variable(np.array(1.0))

print(x)#variable(1.0)

if '__file__' in globals():
    import os, sys
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

#import numpy as np
from dezero import Variable

y = (x + 3) ** 2
y.backward()

print(y)#variable(16.0)
print(x.grad)#8.0