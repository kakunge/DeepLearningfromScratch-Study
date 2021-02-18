from set import *

for i in range(10):
    x = Variable(np.random.randn(10000))
    y = square(square(square(x)))