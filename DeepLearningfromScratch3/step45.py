import numpy as np
from dezero import Variable, Model
import dezero.layers as L
import dezero.functions as F

np.random.seed(0)
x = np.random.rand(100, 1)
y = np.sin(2 * np.pi * x) + np.random.rand(100, 1)

lr = 0.2
max_iter = 10000
hidden_size = 10

class TwoLayerNet(Model):
    def __init__(self, hidden_size, out_size):
        super().__init__()
        self.l1 = L.Linear(hidden_size)
        self.l2 = L.Linear(out_size)

    def forward(self, x):
        y = F.sigmoid(self.l1(x))
        y = self.l2(y)

        return y

model = TwoLayerNet(hidden_size, 1)

for i in range(max_iter):
    y_pred = model(x)
    loss = F.mean_squared_error(y, y_pred)

    model.cleargrads()
    loss.backward()

    for p in model.params():
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