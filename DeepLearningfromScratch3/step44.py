import numpy as np
from dezero import Variable, Parameter
import dezero.functions as F
import dezero.layers as L


x = Variable(np.array(1.0))
p = Parameter(np.array(2.0))
y = x * p

print(isinstance(x, Parameter))#False
print(isinstance(p, Parameter))#True
print(isinstance(y, Parameter))#False



np.random.seed(0)
x = np.random.rand(100, 1)
y = np.sin(2 * np.pi * x) + np.random.rand(100, 1)

l1 = L.Linear(10)
l2 = L.Linear(1)

def predict(x):
    y = l1(x)
    y = F.sigmoid(y)
    y = l2(y)

    return y

lr = 0.2
iters = 10000

for i in range(iters):
    y_pred = predict(x)
    loss = F.mean_squared_error(y, y_pred)

    l1.cleargrads()
    l2.cleargrads()
    loss.backward()

    for l in [l1, l2]:
        for p in l.params():
            p.data = p.data - lr * p.grad.data

    if i % 1000 == 0:
        print(loss)
#variable(0.8165178492839196)
#variable(0.24990280137248175)
#variable(0.24609873705372717)
#variable(0.23721585190665506)
#variable(0.20793215782018806)
#variable(0.12311919443942607)
#variable(0.07888168068357646)
#variable(0.07666438232326257)
#variable(0.076351491566489)
#variable(0.07617084629602781)