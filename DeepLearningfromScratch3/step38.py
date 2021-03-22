import numpy as np
from dezero import Variable
import dezero.functions as F

x = Variable(np.array([[1, 2, 3], [4, 5, 6]]))
y = F.reshape(x, (6,))

print(y)#[1 2 3 4 5 6]

y.backward(retain_grad=True)

print(x.grad)
#variable([[1 1 1]
#          [1 1 1]])

x.cleargrad()

y = F.transpose(x)
y.backward()

print(x.grad)
#variable([[1 1 1]
#          [1 1 1]])
