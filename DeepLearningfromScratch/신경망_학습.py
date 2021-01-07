import sys, os
sys.path.append(os.pardir)
import numpy as np
from dataset.mnist import load_mnist

#학습 : 훈련 데이터로부터 가중치 매개변수의 최적값을 자동으로 획득하는 것
#손실 함수(비용 함수) : 신경망에서 최적의 매개변수 값을 탐색하는데에 사용하는 지표

#평균 제곱 오차
def mean_squared_error(y, t):
    return 0.5 * np.sum((y-t)**2)

#교차 엔트로피 오차
def cross_entropy_error(y, t):
    delta = 1e-7
    return -np.sum(t * np.log(y + delta))#np.log() 함수에 0을 입력하면 -inf가 되어서 계산을 진행할 수 없기 때문에 delta를 더해준다.

#미니배치 : 데이터의 양이 많을 때 모든 데이터의 손실 함수를 일일이 구하는 것이 힘들기 때문에 데이터의 일부를 골라서 전체로 근사하는 것

(x_train, t_train), (x_test, t_test) = \
    load_mnist(normalize=True, one_hot_label=True)

print(x_train.shape)#(60000, 784) : 훈련 데이터 60000개, 입력 데이터 784(28*28)개
print(t_train.shape)#(60000, 10) : 정답 레이블 10줄

train_size = x_train.shape[0]
batch_size = 10
batch_mask = np.random.choice(train_size, batch_size)
x_batch = x_train[batch_mask]
t_batch = t_train[batch_mask]