import numpy as np

class Variable:
    def __init__(self, data):
        if data is not None:
            if not isinstance(data, np.ndarray):
                raise TypeError('{}은(는) 지원하지 않습니다.'.format(type(data)))

        self.data = data
        self.grad = None#역전파에 대응하기 위한 미분값 저장
        self.creator = None
        self.generation = 0

    def set_creator(self, func):
        self.creator = func
        self.generation = func.generation + 1

    #역전파 자동화
    '''
    def backward(self):
        f = self.creator#1. 함수를 가져온다
        if f is not None:
            x = f.input#2. 함수의 입력을 가져온다
            x.grad = f.backward(self.grad)#3. 함수의 backward 메서드를 호출한다
            x.backward()#하나 앞 변수의 backward 메서드를 호출한다
    '''

    #반복문을 이용한 구현
    def backward(self):
        if self.grad is None:
            self.grad = np.ones_like(self.data)
        funcs = [self.creator]
        while funcs:
            f = funcs.pop()
            gys = [output.grad for output in f.outputs]
            gxs = f.backward(*gys)
            if not isinstance(gxs, tuple):
                gxs = (gxs,)
            for x, gx in zip(f.inputs, gxs):
                #같은 변수 중복 사용
                if x.grad is None:
                    x.grad = gx
                else:
                    x.grad = x.grad + gx

                if x.creator is not None:
                    funcs.append(x.creator)

    def cleargrad(self):
        self.grad = None

def as_array(x):
    if np.isscalar(x):
        return np.array(x)
    return x

class Function(object):
    '''
    def __call__(self, input):
        x = input.data
        y = self.forward(x)
        output = Variable(as_array(y))
        output.set_creator(self)#출력 변수에 창조자 설정
        self.input = input#입력 변수를 기억
        self.output = output#출력 저장
        
        return output
    '''

    #__call__ 메서드의 인수와 반환값을 리스트로 변경
    def __call__(self, *inputs):
        xs = [x.data for x in inputs]
        ys = self.forward(*xs)
        if not isinstance(ys, tuple):
            ys = (ys,)
        outputs = [Variable(as_array(y)) for y in ys]
        self.generation = max([x.generation for x in inputs])
        for output in outputs:
            output.set_creator(self)
        self.inputs = inputs
        self.outputs = outputs

        return outputs if len(outputs) > 1 else outputs[0]

    def forward(self, x):
        raise NotImplementedError()

    def backward(self, gy):
        raise NotImplementedError()

class Square(Function):
    def forward(self, x):
        y = x ** 2

        return y

    def backward(self, gy):
        x = self.inputs[0].data
        gx = 2 * x * gy

        return gx

class Exp(Function):
    def forward(self, x):
        y = np.exp(x)

        return y
    
    def backward(self, gy):
        x = self.inputs[0].data
        gx = np.exp(x) * gy

        return gx

class Add(Function):
    def forward(self, x0, x1):
        y = x0 + x1

        return (y,)
    
    def backward(self, gy):
        return gy, gy



def square(x):
    return Square()(x)

def exp(x):
    return Exp()(x)

def add(x0, x1):
    return Add()(x0, x1)