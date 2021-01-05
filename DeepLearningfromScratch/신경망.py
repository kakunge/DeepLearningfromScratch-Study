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

#3층 신경망
def init_network():#가중치와 편향 초기화, 딕셔너리 변수 network에 저장
    network = {}
    network['W1'] = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
    network['b1'] = np.array([0.1, 0.2, 0.3])
    network['W2'] = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])
    network['b2'] = np.array([0.1, 0.2])
    network['W3'] = np.array([[0.1, 0.3], [0.2, 0.4]])
    network['b3'] = np.array([0.1, 0.2])

    return network

def forward(network, x):#입력 신호를 출력으로 변환(순방향)
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']

    a1 = np.dot(x, W1) + b1
    z1 = sigmoid(a1)
    a2 = np.dot(z1, W2) + b2
    z2 = sigmoid(a2)
    a3 = np.dot(z2, W3) + b3
    y = identity_function(a3)

    return y

network = init_network()
x = np.array([0.1, 0.5])
y = forward(network, x)
print(y)#[0.31234736 0.6863161 ]

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

#MNIST 데이터셋 - 손글씨 숫자 이미지 집합

#신경망의 추론 처리
def get_data():
    (x_train, t_train), (x_test, t_test) = \
        load_mnist(normalize=True, flatten=True, one_hot_label=False)#normalize : 입력 이미지의 픽셀을 0.0~1.0 사이의 값으로 정규화 flatten : 입력 이미지를 1차원 배열로 만들지 결정 one_hot_label : one-hot encoding 형태로 저장할지를 결정
    return x_test, t_test

def init_network_mnist():
    with open("sample_weight.pkl", 'rb') as f:
        network = pickle.load(f)

    return network

def predict(network, x):
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']

    a1 = np.dot(x, W1) + b1
    z1 = sigmoid(a1)
    a2 = np.dot(z1, W2) + b2
    z2 = sigmoid(a2)
    a3 = np.dot(z2, W3) + b3
    y = softmax(a3)

    return y

x, t = get_data()
network = init_network_mnist()

accuracy_cnt = 0

for i in range(len(x)):
    y = predict(network, x[i])
    p = np.argmax(y)
    if p == t[i]:
        accuracy_cnt += 1

print("Accuracy:" + str(float(accuracy_cnt) / len(x)))#Accuracy:0.9352

#배치 처리
x, t = get_data()
network = init_network_mnist()

batch_size = 100
accuracy_cnt = 0

for i in range(0, len(x), batch_size):
    x_batch = x[i:i+batch_size]
    y_batch = predict(network, x_batch)
    p = np.argmax(y_batch, axis=1)
    accuracy_cnt += np.sum(p == t[i:i+batch_size])

print("Accuracy:" + str(float(accuracy_cnt) / len(x)))#Accuracy:0.9352