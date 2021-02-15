import numpy as np
from set import *
#Define-by-Run : 딥러닝에서 수행하는 계산들을 계산 시점에 연결하는 방식

A = Square()
B = Exp()
C = Square()

x = Variable(np.array(0.5))
a = A(x)
b = B(a)
y = C(b)

#계산 그래프 역추적
assert y.creator == C
assert y.creator.input == b
assert y.creator.input.creator == B
assert y.creator.input.creator.input == a
assert y.creator.input.creator.input.creator == A
assert y.creator.input.creator.input.creator.input == x

#y에서 b까지의 역전파
y.grad = np.array(1.0)

C = y.creator#1. 함수를 가져온다
b = C.input#2. 함수의 입력을 가져온다
b.grad = C.backward(y.grad)#3. 함수의 backward 메서드를 호출한다

#b에서 a까지의 역전파
B = b.creator
a = B.input
a.grad = B.backward(b.grad)

#a에서 x까지의 역전파
A = a.creator
x = A.input
x.grad = A.backward(a.grad)

print(x.grad)#3.297442541400256

#역전파
y.backward()
print(x.grad)#3.297442541400256