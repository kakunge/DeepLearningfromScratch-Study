import numpy as np
from dezero import Variable, Function
from dezero import as_variable
from dezero import cuda, utils


class Reshape(Function):
    def __init__(self, shape):
        self.shape = shape

    def forward(self, x):
        self.x_shape = x.shape
        y = x.reshape(self.shape)

        return y

    def backward(self, gy):
        return reshape(gy, self.x_shape)

class Transpose(Function):
    def forward(self, x):
        y = np.transpose(x)

        return y

    def backward(self, gy):
        gx = transpose(gy)

        return gx

class BroadcastTo(Function):
    def __init__(self, shape):
        self.shape = shape

    def forward(self, x):
        self.x_shape = x.shape
        xp = cuda.get_array_module(x)
        y = xp.broadcast_to(x, self.shape)
        return y

    def backward(self, gy):
        gx = sum_to(gy, self.x_shape)
        return gx
        
class Sin(Function):
    def forward(self, x):
        y = np.sin(x)

        return y

    def backward(self, gy):
        x, = self.inputs
        gx = gy * cos(x)

        return gx

class Cos(Function):
    def forward(self, x):
        y = np.cos(x)

        return y

    def backward(self, gy):
        x, = self.inputs
        gx = gy * -sin(x)

        return gx

class Tanh(Function):
    def forward(self, x):
        y = np.tanh(x)

        return y

    def backward(self, gy):
        y = self.outputs[0]()
        gx = gy * (1 - y * y)

        return gx

class Sum(Function):
    def __init__(self, axis, keepdims):
        self.axis = axis
        self.keepdims = keepdims

    def forward(self, x):
        self.x_shape = x.shape
        y = x.sum(axis=self.axis, keepdims=self.keepdims)

        return y

    def backward(self, gy):
        gy = utils.reshape_sum_backward(gy, self.x_shape, self.axis, self.keepdims)
        gx = broadcast_to(gy, self.x_shape)

        return gx

class SumTo(Function):
    def __init__(self, shape):
        self.shape = shape

    def forward(self, x):
        self.x_shape = x.shape
        y = utils.sum_to(x, self.shape)

        return y

    def backward(self, gy):
        gx = broadcast_to(gy, self.x_shape)

        return gx

class MatMul(Function):
    def forward(self, x, W):
        y = x.dot(W)

        return y

    def backward(self, gy):
        x, W = self.inputs
        gx = matmul(gy, W.T)
        gW = matmul(x.T, gy)

        return gx, gW

class MeanSquareError(Function):
    def forward(self, x0, x1):
        diff = x0 - x1
        y = (diff ** 2).sum() / len(diff)

        return y

    def backward(self, gy):
        x0, x1 = self.inputs
        diff = x0 - x1
        gx0 = gy * diff * (2. / len(diff))
        gx1 = -gx0

        return gx0, gx1



def reshape(x, shape):
    if x.shape == shape:
        return as_variable(x)
        
    return Reshape(shape)(x)

def transpose(x):
    return Transpose()(x)


def broadcast_to(x, shape):
    if x.shape == shape:
        return as_variable(x)
    return BroadcastTo(shape)(x)

def sphere(x, y):
    z = x ** 2 + y ** 2

    return z

def matyas(x, y):
    z = 0.26 * (x ** 2 + y ** 2) - 0.48 * x * y

    return z

def goldstein(x, y):
    z = (1 + (x + y + 1)**2 * (19 - 14*x + 3*x**2 - 14*y + 6*x*y + 3*y**2)) * (30 + (2*x - 3*y)**2 * (18 - 32*x + 12*x**2 + 48*y - 36*x*y + 27*y**2))

    return z

def rosenbrock(x0, x1):
    y = 100 * (x1 - x0 ** 2) ** 2 + (1 - x0) ** 2

    return y

def sin(x):
    return Sin()(x)

def cos(x):
    return Cos()(x)

def tanh(x):
    return Tanh()(x)

def sum(x, axis=None, keepdims=False):
    return Sum(axis, keepdims)(x)

def sum_to(x, shape):
    if x.shape == shape:
        return as_variable(x)
    return SumTo(shape)(x)

def matmul(x, W):
    return MatMul()(x, W)

def mean_square_error(x0, x1):
    return MeanSquareError()(x0, x1)