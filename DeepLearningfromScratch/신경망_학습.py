import numpy as np

#학습 : 훈련 데이터로부터 가중치 매개변수의 최적값을 자동으로 획득하는 것
#손실 함수(비용 함수) : 신경망에서 최적의 매개변수 값을 탐색하는데에 사용하는 지표

#평균 제곱 오차
def mean_squared_error(y, t):
    return 0.5 * np.sum((y-t)**2)

#교차 엔트로피 오차
def cross_entropy_error(y, t):
    delta = 1e-7
    return -np.sum(t * np.log(y + delta))#np.log() 함수에 0을 입력하면 -inf가 되어서 계산을 진행할 수 없기 때문에 delta를 더해준다.

