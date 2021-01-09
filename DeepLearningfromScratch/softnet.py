import sys, os
sys.path.append(os.pardir)
import numpy as np
from 신경망 import softmax
from 신경망_학습 import cross_entropy_error_batch
from 수치미분 import numerical_gradient

class simpleNet:
    def __init__(self):
        self.W = np.random.randn(2,3) # 정규분포로 초기화

    def predict(self, x):
        return np.dot(x, self.W)

    def loss(self, x, t):
        z = self.predict(x)
        y = softmax(z)
        loss = cross_entropy_error_batch(y, t)

        return loss

