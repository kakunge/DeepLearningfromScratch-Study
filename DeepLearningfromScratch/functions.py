import sys, os
sys.path.append(os.pardir)
import numpy as np
import pickle
from dataset.mnist import load_mnist

def step_function1(x):#간단한 계단 함수
    if x > 0:
        return 1
    else:
        return 0
#넘파이 배열 사용 불가

def step_function2(x):#넘파이 배열 사용
    y = x > 0
    return y.astype(np.int)
#astype()은 넘파이 배열의 자료형을 바꿔준다

#시그모이드 함수 : 신경망에서 자주 쓰이는 활성화 함수의 하나
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

#신경망에서 활성화 함수로 선형 함수를 사용하게 되면 신경망을 여러 층으로 구성하는 이점이 없기 때문에 활성화 함수는 반드시 비선형 함수를 이용해야 한다.

#ReLU 함수 : 입력이 0을 넘으면 입력을 그대로 출력하고, 0 이하이면 0을 출력
def ReLU(x):
    return np.maximum(0, x)


#넘파이를 이용한 행렬 계산과 신경망 신호 전달
#항등 함수
def identity_function(x):
    return x

#소프트맥스 함수 : 분류에 사용되는 활성화 함수
def softmax1(a):
    exp_a = np.exp(a)
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a

    return y
#오버플로가 생기는 것을 조심해야 한다.

#개선된 소프트맥스 함수 구현
def softmax(a):
    c = np.max(a)
    exp_a = np.exp(a-c)
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a

    return y
#소프트맥스 함수의 출력은 0에서 1.0 사이의 실수이고, 출력의 총합은 1이다. 이와 같은 성질을 이용하여 출력값을 '확률'로 해석할 수 있다.

#평균 제곱 오차
def mean_squared_error(y, t):
    return 0.5 * np.sum((y-t)**2)

'''
#교차 엔트로피 오차
def cross_entropy_error(y, t):
    delta = 1e-7
    return -np.sum(t * np.log(y + delta))#np.log() 함수에 0을 입력하면 -inf가 되어서 계산을 진행할 수 없기 때문에 delta를 더해준다.



#배치 데이터에서 교차 엔트로피 오차
def cross_entropy_error_batch(y, t):
    if y.ndim == 1:
        t = t.reshape(1, t.size)
        y = y.reshape(1, y.size)
        
    batch_size = y.shape[0]
    return -np.sum(t * np.log(y + 1e-7)) / batch_size

#원-핫 인코딩이 아닐 경우

def cross_entropy_error_batch(y, t):
    if y.ndim == 1:
        t = t.reshape(1, t.size)
        y = y.reshape(1, y.size)
        
    batch_size = y.shape[0]
    return -np.sum(np.log(y[np.arange(batch_size), t] + 1e-7)) / batch_size
'''

def cross_entropy_error_batch(y, t):
    if y.ndim == 1:
        t = t.reshape(1, t.size)
        y = y.reshape(1, y.size)
    
    if t.size == y.size:
        t = t.argmax(axis=1)
        
    batch_size = y.shape[0]
    return -np.sum(np.log(y[np.arange(batch_size), t] + 1e-7)) / batch_size

def cross_entropy_error(y, t):
    if y.ndim == 1:
        t = t.reshape(1, t.size)
        y = y.reshape(1, y.size)