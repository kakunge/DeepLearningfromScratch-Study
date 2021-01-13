#계산 그래프 : 계산 과정을 그래프로 나타낸 것
#순전파 : 계산 그래프의 출발점부터 종착점으로의 전파
#역전파 : 순전파의 반대 방향으로 전파
#국소적 계산 : 자신과 관련된 작은 계산

#곱셈 계층
class mulLayer:
    def __init__(self):
        self.x = None
        self.y = None

    def forward(self, x, y):#순전파
        self.x = x
        self.y = y
        out = x * y

        return out
    
    def backward(self, dout):#역전파
        dx = dout * self.y
        dy = dout * self.x

        return dx, dy

#덧셈 계층
class addLayer:
    def __init__(self):
        pass

    def forward(self, x, y):#순전파
        out = x * y

        return out
    
    def backward(self, dout):#역전파
        dx = dout * 1
        dy = dout * 1

        return dx, dy