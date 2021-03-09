import numpy as np
from dezero import Variable
from dezero import _dot_var, _dot_func

x = Variable(np.random.randn(2, 3))
x.name = "x"

print(_dot_var(x))#140366370624704 [label="x", color=orange, style=filled]
print(_dot_var(x, verbose=True))#140366370624704 [label="x: (2, 3) float64", color=orange, style=filled]

x0 = Variable(np.array(1.0))
x1 = Variable(np.array(1.0))
y = x0 + x1
txt = _dot_func(y.creator)

print(txt)
#140646185869808 [label="Add", color=lightblue, style=filled, shape=box]
#140646144455008 -> 140646185869808
#140646185869760 -> 140646185869808
#140646185869808 -> 140646185869664