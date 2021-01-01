#간단한 AND게이트 구현

def AND(x1, x2):#x1, x2는 입력값
    w1, w2, theta = 0.5, 0.5, 0.7#w1, w2는 가중치, theta는 임계값
    tmp = x1*w1 + x2*w2
    if tmp <= theta:
        return 0
    elif tmp > theta:
        return 1
