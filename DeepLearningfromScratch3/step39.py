import numpy as np
from dezero import Variable
import dezero.functions as F

x = Variable(np.array([[1, 2, 3], [4, 5, 6]]))
y = F.sum(x, axis=0)
y.backward()

print(y)#variable([5 7 9])
print(x.grad)
#variable([[1 1 1]
#          [1 1 1]])

x = Variable(np.random.randn(2, 3, 4, 5))
y = x.sum(keepdims=True)

print(y.shape)#(1, 1, 1, 1)